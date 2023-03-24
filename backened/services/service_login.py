from backened.sql.query_functions import run_select_where
from werkzeug.security import check_password_hash
from backened.validator.validation import validate_data
from flask import jsonify, make_response

from marshmallow import ValidationError
import jwt
import json

def service_login(request_data):
    print("Into Login")
    try:
        data_dict = validate_data(request_data)
        # print("zzzzzzzz", type(data_dict))
    except ValidationError as errors:
        return{"errors": errors.messages}, 422

    user_name = data_dict['user_name']
    password = data_dict['password']
    data = ({"user_name": user_name})
    
    
    
    try:
        login_response = run_select_where(data)
        
        
        # print("yyyyyyyyy :", type(login_response['user_name']))
    except IndexError:
        # print("datayyyyyyyyy :", login_response)
        return make_response(jsonify({'message':'Could not verify user. Please SignUp First!'}), 404, {'WWW-Authenticate': 'Basic-realm= "No user found!"'})

    if login_response['user_name'] != data_dict['user_name']:
        return make_response(jsonify({'message':'User Name mismatch. Please SignUp First!'}), 404, {'WWW-Authenticate': 'Basic-realm= "No user found!"'})

    if check_password_hash(login_response['password'], data_dict['password']):
        token = jwt.encode( {"payload": json.dumps(login_response, indent=4, sort_keys=True, default=str)},
                           "mysecret", 'HS256')
        return make_response(jsonify({'token': token}), 201)

    return make_response(jsonify({'message':'Could not verify password!'}), 403, {'WWW-Authenticate': 'Basic-realm= "Wrong Password!"'})