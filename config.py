import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost/app3'
    FLASK_RUN_PORT = 5001
    SQLALCHEMY_TRACK_MODIFICATIONS = False

