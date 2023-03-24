from flask import Blueprint, request
from backened.dto.user_schema import UserSchema
from backened.services.decorators import token_required
from backened.services.service_profile import service_profile




user_schema = UserSchema()
users_scehma = UserSchema(many=True)



getuid_bp = Blueprint('getuid_bp', __name__) 



@getuid_bp.route('/user/<uid>', methods=['GET'])
@token_required
def profile_view(data, uid):
    
    profile_data = service_profile(data, uid)
    return profile_data
     





