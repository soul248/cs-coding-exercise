from flask_restx import Namespace, Resource, fields
from marshmallow import ValidationError
from app import db
from app.users.model_users import User, UserPutSchema, UserGetSchema

api = Namespace('Users', description='Users related operations')

user_put_schema = UserPutSchema()
user_get_schema = UserGetSchema()

user_model = api.model(
    "User",
    {
        "name"       : fields.String(required=True, description="Name"),
        "last_name"  : fields.String(required=True, description="Last Name"),
        "email"      : fields.String(required=True, description="Email"),
    }
)

@api.route("/user")
class user_create(Resource):
    ##############
    ### CREATE ###
    ##############
    @api.doc("Insert a new user")
    @api.expect(user_model, validate=True)
    def put(self):
        try:
            data = user_put_schema.load(api.payload)
        except ValidationError as error:
            return {"success": False, "message": "Incorrect user info provided"}, 400

        try:
            user = db.session.query(User.id).filter_by(email=data['email']).scalar()    
            if user:
                return {"success": False, "message": "Mail already registered"}

            user = User(name=data["name"], last_name=data["last_name"], email=data["email"])

            db.session.add(user)
            db.session.commit()

            return {"success": True, "message": "User created", "user": user_get_schema.dump(user)}
        
        except:
            return {"success": False, "message": "Unexpected error"}

@api.route("/user/<int:id>")
class user_read(Resource):
    
    ############
    ### READ ###
    ############
    @api.doc("Get a specific user")
    def get(self, id):
        user = User.query.get(id)
        if not user:
            return {"success": False, "message": "User not found"}

        return {"success": True, "user": user_get_schema.dump(user)}
    
    ##############
    ### UPDATE ###
    ##############
    @api.doc("Update a specific user")
    @api.expect(user_model, validate=True)
    def post(self, id):
        try:
            data = user_put_schema.load(api.payload)
        except ValidationError as error:
            return {"success": False, "message": "Incorrect user info provided"}, 400

        try:
            user = db.session.query(User.id).filter_by(email=data['email']).scalar() 
            if user:
                return {"success": False, "message": "Mail already registered"}

            user = User.query.get(id)    
            if not user:
                return {"success": False, "message": "User not found"}

            user.name=data["name"]
            user.last_name=data["last_name"]
            user.email=data["email"]

            db.session.commit()

            return {"success": True, "message": "User updated", "user": user_get_schema.dump(user)}
        
        except:
            return {"success": False, "message": "Unexpected error"}
    
    ##############
    ### DELETE ###
    ##############
    @api.doc("Delete a specific user")
    def delete(self, id):
        user = User.query.get(id)
        if not user:
            return {"success": False, "message": "User not found"}
        
        db.session.delete(user)
        db.session.commit()

        return {"success": True, "message": "User deleted"}