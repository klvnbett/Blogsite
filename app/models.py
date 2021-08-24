from . import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Blog(db.Model):
    __tablename__ = 'blog'

    id=db.Column(db.Integer, primary_key=True)
    blog_category=db.Column(db.String(255))
    blog_title=db.Column(db.String(255))
    blog_content=db.Column(db.String(255),min_length=100)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_blog(self):
        db.session.add(self)
        db.session.commit()


class User(UserMixin,db.Model):
    __tablename__="users"

    id =db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255))
    password_secure=db.Column(db.String(255))
    location=db.Column(db.String(255))

    blog =db.relationship('Blog',backref='users',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

        
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    def __repr__(self):
        return f'User{self.username}'


class Quotes:

    '''
    This is a class that defines the quotes details objects
    '''

    def __init__(self,id,quote,author):

        self.id=id
        self.quote=quote
        self.author=author