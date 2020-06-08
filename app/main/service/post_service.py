import uuid
import datetime
import io 
import base64

from app.main import db
from app.main.model.post import Post

from flask import jsonify
from sqlalchemy import desc, asc 

def post_new_post(data,user):
    newPost = Post(
        user_id = user.id,
        image = data['image'],
        caption = data['caption'],
        posted_on = datetime.datetime.utcnow
    )
    save_changes(newPost)
    newPost.username = newPost.user.username
    return newPost

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

def save_changes(data):
    db.session.add(data)
    db.session.commit()

