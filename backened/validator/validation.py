import json



from backened.dto.user_schema import UserSchema

user_schema = UserSchema()
users_scehma = UserSchema(many=True)


def validate_data(request_data):
    
    # request_data = request.get_json()
    print("data", request_data)
    
    get_data = user_schema.loads(json.dumps(request_data))
    print("1111",type(get_data))
    return get_data
    

def dump_data(data):
    return user_schema.dump(data)


# def valid_profile_data(data):
#     parsed_json_to_pydict = json.loads(data['payload'])['uid']
#     print("uid", parsed_json_to_pydict)
#     return parsed_json_to_pydict
