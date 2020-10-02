import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'elon_musk_is_the_king'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir , 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # app.config['MYSQL_HOST'] = 
    # app.config['MYSQL_USER'] = 
    # app.config['MYSQL_PASSWORD'] = 
    # app.config['MYSQL_DB'] = 
