from flask import Blueprint
from backened.dto.user_schema import UserSchema
from backened.services.service_register import service_register
from flask import request

user_schema = UserSchema()
users_scehma = UserSchema(many=True)


register_bp = Blueprint('register', __name__)





@register_bp.route('/user/register', methods=['POST'])

def user_register():
    
    request_data = request.get_json()
    print("333333333333333333333",request_data)
    insert = service_register(request_data)
    print("insertrtttttttttttttt:",insert)
    print(type(insert))
    return insert
    
