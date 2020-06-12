from flask_restplus import Namespace, fields
from werkzeug.datastructures import FileStorage

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='The username'),
        'password': fields.String(required=True, description='The user password '),
    })

class PostDto:
    api = Namespace('post', description='post related operations')
    post_upload = api.model('post_upload', {
        'post_owner': fields.String(required=True, description='owner of post'),
        'image': fields.String(required=True,description='Image URI for Post'),
        'caption': fields.String(required=True, description='Caption'),
        'posted_on': fields.DateTime(required=True,description='Posted on DateTime')
    })
    upload_parser = api.parser()
    upload_parser.add_argument('caption',required=True)
    upload_parser.add_argument('image',type=FileStorage,location='files',required=True)
