from app.handlers.test import Hello
from app import api


api.add_resource(Hello, '/hello')