from functools import wraps

from flask import request

from app.main.service.auth_helper import Auth
from app.main.service.user_service import get_one_user


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        else: 
            user_id = token.get('user_id')
            user_rn = get_

        return f(*args, **kwargs)

    return decorated


def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        admin = token.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response_object, 401

        return f(*args, **kwargs)
    
    return decorated

def accepted_files(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        file = request.files['image']
        if not '.' in file.filename or not file.filename.rsplit('.', 1)[1].lower() in file_types:
            response_object = {
                'status': 'fail',
                'message': 'Use a valid file type'
            }
            return response_object, 400

        return f(*args, **kwargs)

    return decorated
