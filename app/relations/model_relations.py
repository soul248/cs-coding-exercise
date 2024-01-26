import datetime
from app import db
from sqlalchemy.dialects import mysql
from marshmallow import Schema, fields, validate

##### MODEL #####
class Relation(db.Model):
    __tablename__ = 'relations'

    id         = db.Column(mysql.INTEGER(11, unsigned=True), primary_key=True)
    user1_id   = db.Column(mysql.INTEGER(11, unsigned=True), nullable=False)
    user2_id   = db.Column(mysql.INTEGER(11, unsigned=True), nullable=False)
    created_at = db.Column(mysql.DATETIME, nullable=False, default=datetime.datetime.now)

##### SCHEMAS #####
class DeegreesSchema(Schema):
    user1_id = fields.Int()
    user2_id = fields.Int()