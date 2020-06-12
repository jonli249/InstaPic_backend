import unittest, json, datetime, base64, uuid
from unittest.mock import patch

from app.main import db
from app.test.base import BaseTestCase
from app.main.model.post import Post

#For testings images 
from PIL import Image 
from io import BytesIO

def register_user(self):
    return self.client.post(
        '/user/',
        data=json.dumps(dict(
            username='username',
            password='123456'
        )),
        content_type='application/json'
    )


def make_post(token, post, self):
    return self.client.post(
        '/post/',
        headers={
        	'Authorization': token,
        	'Content-Type': 'multipart/form-data'
        },
        data=post
    )

def get_posts(self, jwt):
    return self.client.get(
        '/post/',
        headers=dict(
            Authorization=jwt
        )
    )



class TestPostService(BaseTestCase):
    
    def test_post_model(self):
        """ Test for making new post """
        with self.client:
            reg = register_user(self)
            auth_data = json.loads(reg.data.decode())
            token = auth_data['Authorization']
            
            testFile = BytesIO()
            image = Image.open('/Users/jonathanli/Desktop/Projects/InstaPic/InstaPic_backend/app/test/test.png')            
            testFile.name  = 'test.png'

            post_data = dict(
                image=testFile,
                caption='Test Caption'
            )
            resp = make_post(token, post_data, self)
            data = json.loads(resp.data)
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Success! Post Added to DB.')
            self.assertTrue(resp.content_type == 'application/json')
            self.assertEqual(resp.status_code, 201)
            
    def test_post_model_no_cap(self):
        """ Test for making new post -no caption """
        with self.client:
            reg = register_user(self)
            auth_data = json.loads(reg.data.decode())
            token = auth_data['Authorization']
            
            testFile = BytesIO()
            image = Image.open('/Users/jonathanli/Desktop/Projects/InstaPic/InstaPic_backend/app/test/test.png')            
            testFile.name  = 'test.png'

            post_data = dict(
                image=testFile,
            )
            resp = make_post(token, post_data, self)
            data = json.loads(resp.data)
            self.assertTrue(data['message'] == 'The browser (or proxy) sent a request that this server could not understand.')
            self.assertTrue(resp.content_type == 'application/json')
            self.assertEqual(resp.status_code, 400)

    def test_post_model_no_image(self):
        """ Test for making new post -no image"""
        with self.client:
            reg = register_user(self)
            auth_data = json.loads(reg.data.decode())
            token = auth_data['Authorization']
        

            post_data = dict(
                caption='This post does not work - no caption'
            )
            resp = make_post(token, post_data, self)
            data = json.loads(resp.data)
            self.assertTrue(data['message'] == 'The browser (or proxy) sent a request that this server could not understand.')
            self.assertTrue(resp.content_type == 'application/json')
            self.assertEqual(resp.status_code, 400) 

    def test_post_model_wrong_file(self):
        """ Test for making new post -wrong file type """
        with self.client:
            reg = register_user(self)
            auth_data = json.loads(reg.data.decode())
            token = auth_data['Authorization']
            

            post_data = dict(
                image= (BytesIO(b'Wrong file type with pdf uh oh!'),'wrong_file.txt'),
                caption =' Wrong file type'
            )
            resp = make_post(token, post_data, self)
            data = json.loads(resp.data)
            self.assertTrue(data['message'] == 'Use a valid file type')
            self.assertTrue(resp.content_type == 'application/json')
            self.assertEqual(resp.status_code, 400)

    
    '''
    ##Irrelevant, Delete Features Not in Final Product
    def test_delete_post_without_auth(self):
        with self.client:
            response = delete_post(self, 0, '')
            self.assertEqual(response.status_code, 401)

    def test_delete_post_as_owner(self):
        with self.client:
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            auth = data_register['Authorization']
            resp_make = make_post(self, auth)
            data_make = json.loads(resp_make.data.decode())
            self.assertEqual(resp_make.status_code, 200)
            resp_delete = delete_post(self, data_make['id'], auth)
            self.assertEqual(resp_delete.status_code, 200)
    '''


if __name__ == '__main__':
    unittest.main()