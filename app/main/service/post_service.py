import uuid
import datetime
import io 
import base64

from app.main import db
from app.main.model.post import Post
from app.main.model.user import User

from flask import jsonify
from sqlalchemy import desc, asc 

from werkzeug.utils import secure_filename
from uuid import uuid4

def post_new_post(request):
    auth_token = request.headers.get('Authorization')
    data = request.form
    if auth_token:
        ret = User.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            user = User.query.filter_by(id=ret).first()
            image_url = save_image(request.files['image'])
            new_post = Post(
                id=str(uuid.uuid4()),
                caption=data['caption'],
                user=user.username,
                image=image_url,
                posted_on=datetime.datetime.utcnow(),

            )
            save_changes(new_post)
            response_object = {
                'status': 'success',
                'message': 'Successfully added post to db.'
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
            'message': 'Provide a valid auth token.'
        }
        return response_object, 401

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
    filename = secure_filename(image.filename) #secure filename 
    unique_id = uuid4().__str__()[:8]
    unique_filename = f"{unique_id}-{filename}"

    os_store = os.path(basedir,'images')
    if not os.path.exists(os_store):
        os.makedirs(os_store)
    # Save the file
    path = os.path.join(os_store, unique_filename)
    image.save(path)
    return unique_filename

def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()

