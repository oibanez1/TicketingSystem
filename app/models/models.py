from app.__init__ import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash , check_password_hash

class User(db.Model , UserMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer , primary_key = True, autoincrement = True)
    email = db.Column(db.String(128) , unique = True, )
    password_hash = db.Column(db.String(128))
    type_of_user = db.Column(db.String(60))

    def set_pass(self , password):
        self.password_hash = generate_password_hash(password)

    def check_pass(self , password):
        return check_password_hash(self.password_hash , password)
    
    def get_id(self):
        return (self.user_id)
    
    @login.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))





