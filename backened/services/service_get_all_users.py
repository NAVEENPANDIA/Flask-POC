from flask import jsonify
from backened.dto.user_schema import UserSchema
from backened.sql.query_functions import run_select_all


user_schema = UserSchema
users_scehma = UserSchema(many=True)
 

def get_all_users():
    
    get_all = run_select_all()

    list_all_user=[dict(row) for row in get_all]
    
    return jsonify({'Users':list_all_user, 'status': 200})
    # print("get_all",get_all)

    
    
    