from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from config import config
from flask_login import LoginManager
import sqlite3
from flask_migrate import Migrate

# bootstrap = Bootstrap()
# db = SQLAlchemy()
# migrate = Migrate()
# bcrypt = Bcrypt()
# login_manager = LoginManager()
# login_manager.login_view = 'main.login'


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	#conn = sqlite3.connect('databaseBMT.db')
	#conn.execute('CREATE TABLE IF NOT EXISTS users (first_name TEXT, last_name TEXT, email TEXT, password_hash TEXT)')
	
	# bootstrap.init_app(app)
	# db.init_app(app)
	# bcrypt.init_app(app)
	# login_manager.init_app(app)
	# migrate.init_app(app, db)
	
	from Flask_IIS.main import views

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app