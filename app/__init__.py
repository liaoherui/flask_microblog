import logging
from logging.handlers import SMTPHandler, RotatingFileHandler

from flask import Flask,request,current_app
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager
from flask_mail import Mail

from flask_bootstrap import Bootstrap

from flask_moment import Moment
from flask_babel import Babel,lazy_gettext as _l
import os



#app=Flask(__name__)
#app.config.from_object(Config)


#print('Who use me: ',__name__)

db=SQLAlchemy()
migrate=Migrate()

login = LoginManager()
login.login_view='auth.login'
#login.login_message = _l('Please log in to access this page.')

mail=Mail()
bootstrap=Bootstrap()

moment=Moment()
babel=Babel()




def create_app(config_class):
	app=Flask(__name__)
	app.config.from_object(Config)
	
	db.init_app(app)
	migrate.init_app(app,db)
	login.init_app(app)
	mail.init_app(app)
	bootstrap.init_app(app)
	moment.init_app(app)
	babel.init_app(app)

	from app.auth import bp as auth_bp
	app.register_blueprint(auth_bp)

	from app.main import bp as main_bp
	app.register_blueprint(main_bp)

	if not app.debug and not app.testing:
		if not os.path.exists('logs'):
			os.mkdir('logs')
		file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
		file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
		file_handler.setLevel(logging.INFO)
		app.logger.addHandler(file_handler)
		app.logger.setLevel(logging.INFO)
		app.logger.info('Microblog startup')

	return app


@babel.localeselector
def get_locale():
	return request.accept_languages.best_match(current_app.config['LANGUAGES'])

from app import models
