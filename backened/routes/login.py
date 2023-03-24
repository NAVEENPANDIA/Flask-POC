from backened.dto.user_schema import UserSchema
from backened.services.service_login import service_login
from flask import request


user_schema = UserSchema()
users_scehma = UserSchema(many=True)

from flask import Blueprint

login_bp = Blueprint('login_bp',__name__)





@login_bp.route('/user/login', methods=['POST'])
def login():
    request_data = request.get_json()
    data = service_login(request_data)
    return data
