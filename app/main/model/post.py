from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt

class Post(db.Model):
    """ Pics Model for storing Instapic posts with image and description """
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    user = db.relationship('User',foreign_keys=user_id,lazy='select')
    image = db.Column(db.String())
    caption = db.Column(db.String(2200)) #Same as Instagram 
    posted_on = db.Column(db.DateTime,nullable=False)

    def __repr__(self):
        return "<Post '{}'>".format(self.id)
    



