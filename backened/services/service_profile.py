from backened.sql.query_functions import run_select_where_uid
from flask import jsonify, make_response
import json





def service_profile(data,uid):
    print("Into Profile")
    parsed_json_to_pydict_uid_value = json.loads(data['payload'])['uid']
    # data_dict = valid_profile_data(data)
    profile_data = ({"uid": uid})   

    if uid == parsed_json_to_pydict_uid_value:
        # print('fetch',data)
        print("user_details")
        
        profile_info = run_select_where_uid(profile_data)
        return profile_info
        
    else:
        return make_response(jsonify({'Message': 'Login Required'}), 400)