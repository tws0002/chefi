import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'myFunckyBabyBoyLikesSlayer6533'
BCRYPT_LOG_ROUNDS = 12

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# email server
MAIL_SERVER = 'smtp.losart3d.com'
MAIL_PORT = 1025
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['carlos@losart3d.com']
