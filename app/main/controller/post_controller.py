from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required,token_required
from ..util.dto import PostDto
from ..service.post_service import get_all_posts, get_posts_paginated, post_new_post,delete_post

api = PostDto.api

@api.route('/')
class PostList(Resource):
    @api.doc('Gets All Posts')
    @admin_token_required
    @api.marshal_list_with(PostDto.post_description, envelope='data')
    @api.response(200,'Got the posts')
    def get(self):
        ##################
        """List all posts"""
        pagesize = request.args.get('pagesize', default=0, type=int)
        page = request.args.get('page', default=0, type=int)

        try:
            if pagesize is not 0:
                page = page or 1
                return get_posts_paginated(pagesize, page)

            return get_all_posts()
        except Exception as e:
            return []
        

    @api.doc('create a new user')
    @token_required
    @api.expect(PostDto.post_upload, validate=True) 
    @api.marshal_list_with(PostDto.post_description)
    @api.response(200,'Uploaded post')
    def post(self,user):
        """Uploads post """
        data = request.json
        return post_new_post(data=data,user=user)


    @api.doc('Deletes a post')
    @token_required 
    @api.expect(PostDto.post_delete, validate=True)
    @api.response(200, 'Deleted Post')
    def delete(self,user):
        """Deletes a post by user """
        data = request.json
        return delete_post(data['id'],user.id)
