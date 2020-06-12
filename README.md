#### Instapic Backend (Flask RESTful API ) - Reap Coding Challenge 

### Production API Link 
https://instapic-backend-jonli.herokuapp.com/

### Terminal commands

    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all


### Making App and Viewing Swagger  ###


    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


### API Documentation ###

### Create a user 

*Endpoint:* `/user/`

*Method:* `POST`

*Authorization*: `token`

### Get All Users

*Endpoint:* `/user/`

*Method:* `GET`

*Authorization*: `token`

### Authorization

*Endpoint:* `/auth/login`

*Method:* `POST`

*Arguments:*

* username: String 
* password: String

### Authorization Logout

*Endpoint:* `/auth/logout`

*Method:* `POST`

*Arguments:*

None

### Post 

*Endpoint:* `/post/`

*Method:* `POST`

*Arguments:*

* caption: String 
* image: file

### Get Posts 

*Endpoint:* `/post/`

*Method:* `GET`

*Arguments:*


### Get Post 

*Endpoint:* `/post/`

*Method:* `GET`

*Arguments:*










### Authorization with Tokens ###

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"

    For testing authorization, url for getting all user requires an admin token while url for getting a single
    user by public_id requires just a regular authentication.



### Resources
Used following resource as boilerplate for the API
```
https://github.com/cosmic-byte/flask-restplus-boilerplate.git
```
