import datetime
from app import db
from sqlalchemy.dialects import mysql
from marshmallow import Schema, fields, validate

##### MODEL #####
class User(db.Model):
    __tablename__ = 'users'

    id         = db.Column(mysql.INTEGER(11, unsigned=True), primary_key=True)
    name       = db.Column(mysql.VARCHAR(100), nullable=False)
    last_name  = db.Column(mysql.VARCHAR(100), nullable=False)
    email      = db.Column(mysql.VARCHAR(100), nullable=False)
    created_at = db.Column(mysql.DATETIME, nullable=False, default=datetime.datetime.now)

##### SCHEMAS #####
class UserPutSchema(Schema):
    name            = fields.Str()
    last_name       = fields.Str()
    email           = fields.Str(validate=validate.Email())
    
class UserGetSchema(Schema):
    id              = fields.Int(dump_only=True)
    name            = fields.Str()
    last_name       = fields.Str()
    email           = fields.Str(validate=validate.Email())
    created_at      = fields.DateTime(dump_only=True)