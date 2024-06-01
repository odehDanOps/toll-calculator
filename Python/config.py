import os
from pathlib import Path
from abc import ABCMeta

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class IConfig(metaclass=ABCMeta):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = str(Path(__file__).parent.parent)
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # API documentation
    APIFAIRY_TITLE = 'Toll Fee API'
    APIFAIRY_VERSION = '1.0'
    APIFAIRY_UI = 'elements'
    APIFAIRY_TAGS = ['fees']
	

class DevelopmentConfig(IConfig):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')


class ProductionConfig(IConfig):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_ECHO = False


class TestConfig(IConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
