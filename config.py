import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dunyung1:iamyung1@localhost/bookmodel'

    MAIL_SERVER = 'smtp.googlemail.com'

    MAIL_PORT = 587

    MAIL_USE_TLS = True

    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")

    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dunyung1:iamyung1@localhost/bookmodel'

class DevConfig(Config):

    DEBUG = True

config_options = {
'test':TestConfig,
'development':DevConfig,
'production':ProdConfig
}
