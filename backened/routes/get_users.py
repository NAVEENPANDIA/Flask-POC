from flask import Blueprint
from backened.services.service_get_all_users import get_all_users




user_bp = Blueprint('user_bp', __name__)






@user_bp.route('/user', methods=['GET'])
def get_users():
    all_users = get_all_users()
    
    return all_users

  
   














