from app.handlers.test import Hello
from app.handlers.url import Urlapi
from app import api


api.add_resource(Hello, '/hello')
api.add_resource(Urlapi, '/create')
