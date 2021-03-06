from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskwebapp.config import app_config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login' #function name of the route
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    from flaskwebapp.users.routes import users
    from flaskwebapp.posts.routes import posts
    from flaskwebapp.main.routes import main
    from flaskwebapp.errors.handlers import errors

    from flaskwebapp.users.api.routes import usersAPI
    from flaskwebapp.posts.api.routes import postsAPI

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    
    app.register_blueprint(usersAPI)
    app.register_blueprint(postsAPI)

    return app