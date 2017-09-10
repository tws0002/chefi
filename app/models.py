from sqlalchemy.ext.hybrid import hybrid_property
from . import bcrypt, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    _password = db.Column(db.String(128))
    emailVerified = db.Column(db.Boolean(),default=False)
    
    @hybrid_property
    def password(self):
        return self._password
    
    def testPassword(self,plaintext):
        return bcrypt.check_password_hash(self.password,plaintext)
    
    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)
    
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True
    
    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)