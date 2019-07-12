import os

from flask import Flask
from flask_restful import Api
from flask import Blueprint

from app.config.local_config import Config
from .models import *

# flask app config
flask_app = Flask(__name__, instance_relative_config=True)

flask_app.config.from_object(Config)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

flask_app.register_blueprint(api_bp, url_prefix='/api')

# initialise sqlalchemy
db.init_app(flask_app)
# initialise marshmallow
ma.init_app(flask_app)

# initialise blueprints
api.init_app(api_bp)

# initialise flask migrations
migrate.init_app(flask_app, db)


basedir = os.path.join(flask_app.root_path)
# delibrately added in the end to avoid circular dependencies
from app import urls
