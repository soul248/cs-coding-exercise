# Imports
from flask import Flask
import simplejson as json
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
api = Api(app, title="CS Coding Exercise", version="0.1", description="Users degrees of separation")

# Configurations
app.config.from_object('config')

# DataBase
db = SQLAlchemy(app)

# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    data = { "error": "404 Not Found" }
    response = app.response_class(
        response=json.dumps(data),
        status=404,
        mimetype='application/json'
    )
    return response

# Import and add the namespaces of Restx
from app.users.namespace import api as users_api
from app.relations.namespace import api as relations_api
api.add_namespace(users_api, path=f'/api/{api.version}')
api.add_namespace(relations_api, path=f'/api/{api.version}')