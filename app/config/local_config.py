from .base_config import BaseConfig


class Config(BaseConfig):

    POSTGRES_USER = ''
    POSTGRES_PASSWORD = ''
    POSTGRES_HOST = 'localhost'
    POSTGRES_DATABASE = 'shorten_url'
    # SQLALCHEMY_DATABASE_URI = "postgresql://root:root@localhost/token_problem"
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_DATABASE)
    FLASK_DEBUG = True
    FLASK_ENV = "development"