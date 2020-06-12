from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt

class Post(db.Model):
    """ Post Model for storing Instapic posts with image and description """
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100),unique=True)
    post_owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image = db.Column(db.String())
    caption = db.Column(db.String(500)) 
    posted_on = db.Column(db.DateTime,nullable=False)

    def __repr__(self):
        return "<Post '{}'>".format(self.id)
    



