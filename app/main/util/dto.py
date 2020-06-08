from flask_restplus import Namespace, fields


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
        'image': fields.String(required=True, description='The image on the post'),
        'caption': fields.String(required=True, description='The caption on the post'),
    })
    post_description= api.model('post_description', {
        'username': fields.String(required=True, description='owner of post'),
        'id': fields.Integer(required=True, description='post id (for creation)'),
        'image': fields.String(required=True,description='Image URI for Post'),
        'caption': fields.String(required=True, description='Caption'),
        'posted_on': fields.DateTime(required=True,description='Posted on DateTime')
    })
    post_delete = api.model('post_delete', {
        'id': fields.Integer(required=True, description='Post ID (for deletion)'),
    })

