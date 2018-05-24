from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(Config)
  db.init_app(app)
  migrate.init_app(app, db)
  bootstrap.init_app(app)
  
  return app

from app import routes, models,errors
