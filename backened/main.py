from flask import Flask
from .routes.get_users import user_bp
from .routes.register import register_bp
from .routes.login import login_bp
from .routes.get_user_uid import getuid_bp
import logging
from backened.sqlalchemy_db import db
def create_app():
    
    app = Flask(__name__)

    logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@172.17.0.2:3306/flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app =app
    db.init_app(app)
    app.config["DEBUG"] = True
    app.config['TESTING'] = True
    app.register_blueprint(user_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(getuid_bp)
    

    return app











