from flask import jsonify, request, make_response
from functools import wraps
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data_header = request.headers['Authorization']
        print("data_headerrrrrrrrrrrrrrrrr", request.headers['Authorization'])
        
        token = str.replace(str(data_header), 'Bearer ', '')
        print("sdsdsdsd", token)
        if not token:
            return jsonify({'Message':'Token is missing'}), 401
        try:    
            data = jwt.decode(token, "mysecret", algorithms=['HS256'])
        except jwt.InvalidTokenError:
            return make_response({'Message':'Invalid Token!'}, 403)
        return f(data, *args, **kwargs)

    return decorated