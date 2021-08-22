import os

class Config:
    SECRET_KEY = os.environ('SECRET KEY')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:read432q@localhost/blogs'
    DEBUG = True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}