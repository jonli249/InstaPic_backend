import uuid
import datetime
import io 
import base64
import os

from app.main import db
from app.main.model.post import Post
from app.main.model.user import User

from flask import jsonify
from sqlalchemy import desc, asc 

from werkzeug.utils import secure_filename
from uuid import uuid4

from app.main.config import os_store    

def post_new_post(request):
    auth_token = request.headers.get('Authorization')
    data = request.form
    if auth_token:
        resp = User.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            user = User.query.filter_by(id=resp).first()
            image_url = save_image(request.files['image'])
            new_post = Post(
                public_id=str(uuid.uuid4()),
                post_owner=user.username,
                image=image_url,
                caption=data['caption'],
                posted_on=datetime.datetime.utcnow(),

            )
            save_changes(new_post)

            response_object = {
                'status': 'success',
                'message': 'Success! Post Added to DB.'
            }
            return response_object, 201
        response_object = {
            'status': 'fail',
            'message': resp
        }
        return response_object, 401
    else:
        response_object = {
            'status': 'fail',
            'message': 'Valid Auth Token Required'
        }
        return response_object, 401

'''
def delete_post(id,user_id):
    delPost = Post.query.filter_by(id=id,user_id=user_id).first_or_404(description="Post Not Found")
    db.session.delete(delPost)
    db.session.commit()

    #!!!!
    response = {
        'message': 'Post Deleted',
        'status': 'Success'
    }

    return response, 200
'''

def get_all_posts():
    posts = Post.query.order_by(desc(Post.posted_on)).all()
    #reformat this
    return list(map(format_username_posts,posts)) 

######
def get_posts_paginated(max_posts,page):
    posts = Post.query.order_by(desc(Post.posted_on)).paginate(page,max_posts,False).items
    return list(map(format_username_posts,posts)) 


def format_username_posts(post):
    #Accounts for contigency where username is not displayed correct
    post.username = post.user.username
    return post


#######
def save_image(image):
    file = secure_filename(image.filename) #Ensures secucre filename
    uid = uuid4().__str__()[:8]
    final_filname = f"{uid}-{file}"

    if not os.path.exists(os_store):
        os.makedirs(os_store)
    # Save the file
    path = os.path.join(os_store, final_filname)
    image.save(path)
    return final_filname

def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()

