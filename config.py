import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/bookmodel'

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/bookmodel'

class DevConfig(Config):

    DEBUG = True

config_options = {
'test':TestConfig,
'development':DevConfig,
'production':ProdConfig
}
