from flask import Flask
from app.db import init_db

def create_app():
    app = Flask(__name__)
    

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    init_db(app)


    from app.routes import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
