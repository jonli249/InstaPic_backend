from flask import request,send_from_directory
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required,token_required,accepted_files
from ..util.dto import PostDto
from ..service.post_service import get_all_posts, get_posts_paginated, post_new_post #,delete_post

api = PostDto.api
post_model = PostDto.post_upload
uploader = PostDto.upload_parser



@api.route('/')
class PostList(Resource):
    @api.doc('Gets All Posts')
    @token_required
    @api.marshal_list_with(PostDto.post_upload, envelope='data')
    @api.response(200,'Got the posts')
    def get(self):
    
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
        

    @api.doc('Upload New Post')
    @token_required
    @accepted_files
    @api.expect(PostDto.upload_parser, validate=True) 
    @api.response(200,'Uploaded post Successfully')
    def post(self):
        """Uploads post """
        data = request.json
        return post_new_post(request=request)


@api.route('/<path:filename>')
class Post(Resource):
    @api.doc('Gets the image')
    def get(self, file):
        os_store = os.path.join(basedir, 'images')
        return send_from_directory(os_store, file)


