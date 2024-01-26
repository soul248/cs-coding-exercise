from flask_restx import Namespace, Resource, fields
from marshmallow import ValidationError
from app import db
from app.relations.model_relations import Relation, DeegreesSchema
import sys
api = Namespace('Relations', description='Relations related operations')

deegrees_schema = DeegreesSchema()
deegrees_model = api.model(
    "Relation",
    {
        "user1_id" : fields.Integer(required=True, description="Id of starting user"),
        "user2_id" : fields.Integer(required=True, description="Id of destiny user")
    }
)

@api.route("/relation/deegrees-of-separation")
class relations_deegrees_of_separation(Resource):
    ##############################
    ### Deegrees of separation ###
    ##############################
    @api.doc("Calculate the deegrees of separation between two users")
    @api.expect(deegrees_model, validate=True)
    def post(self):
        try:
            data = deegrees_schema.load(api.payload)
        except ValidationError as error:
            return {"success": False, "message": "Incorrect deegrees info provided"}, 400

        try:
            deegrees_counter, deegrees_chain = self.calculate_deegrees(data['user1_id'], data['user2_id'], 1, [])
            
            if deegrees_counter:
                deegrees_chain = ",".join(str(num) for num in deegrees_chain)
                return {"success": True, "message": f"Connection found at {deegrees_counter} deegrees with chain {deegrees_chain}"}
            
            return {"success": True, "message": "Didn't find connection between the two users"}
        
        except:
            return {"success": False, "message": "Unexpected error"}, 500

    def calculate_deegrees(self, user1_id, user2_id, deegrees_counter, deegrees_chain):
        deegrees_chain.append(user1_id)

        relation = db.session.query(Relation).filter_by(user1_id=user1_id,user2_id=user2_id).scalar()
        if relation:
            deegrees_chain.append(user2_id)
            return deegrees_counter, deegrees_chain
        
        connections = db.session.query(Relation).filter(Relation.user1_id==user1_id, Relation.user2_id.not_in(deegrees_chain))
        for connection in connections:
            return self.calculate_deegrees(connection.user2_id, user2_id, deegrees_counter+1, deegrees_chain)
        
        return False, False