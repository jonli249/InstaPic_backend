from flask_restplus import Api
from flask import Blueprint


from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.post_controller import api as post_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Instapic API',
          version='1.0',
          description='A Flask RESTful API service for Instapic'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(post_ns, path='/post')


