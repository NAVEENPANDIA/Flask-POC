from backened.sql.query_functions import run_insert
from werkzeug.security import generate_password_hash
from backened.validator.validation import validate_data
import uuid
from flask import make_response, jsonify
import sqlalchemy
from marshmallow import ValidationError
import datetime

def service_register(request_data):
    
    print("Into Register")
    try:
        data_dict = validate_data(request_data)
    except ValidationError as errors:
        return{"errors": errors.messages}, 422

    print("dict:", data_dict)
    user_name = data_dict['user_name']
    print(user_name) 
    password = generate_password_hash(data_dict['password'], method='sha256', salt_length=16)
    email_address = data_dict['email_address']
    dob = data_dict['dob']
    address = data_dict['address']
    uid = uuid.uuid4().hex
    data = ({"user_name": user_name, "password": password,
                "email_address": email_address, "dob": dob, "address": address, "uid": uid})
    

    try: 
       
       insert = run_insert(data) 
    #    print(insert)
       return make_response(jsonify({'Message': 'New user Created'}),201)

    except sqlalchemy.exc.IntegrityError:
        return make_response({'message':'User already exist with this email address!'}, 409)


    