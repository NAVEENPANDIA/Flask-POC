




# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         data = request.headers['Authorization']
#         token = str.replace(str(data), 'Bearer ', '')
#         if not token:
#             return jsonify({'message': 'Token is missing'}), 401
#         try:    
#             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
#         except jwt.InvalidTokenError:
#             return make_response({'message':'Invalid Token!'}, 403)
#         return f(data, *args, **kwargs)

#     return decorated