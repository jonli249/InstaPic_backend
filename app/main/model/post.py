from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt
from user import User

class Post(db.Model):
    """ Pics Model for storing Instapic posts with image and description """
    __tablename__ = "posts"

    #Post ID
    id = db.Column(id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    user = db.relationship('User',foreign_keys=user_id,lazy='select')
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    #Image Details 
    image = db.Column(db.String())
    caption = db.Column(db.String(2200)) #2200 - same as Instagram
    posted_on = db.Column(db.DateTime,nullable=False)

    def __repr__(self):
        return "<Post '{}'>".format(self.id)
    



