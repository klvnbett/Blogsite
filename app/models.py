from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db, login_manager


class User(UserMixin,db.Model):
    '''
    '''
    __tablename__="user"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255))
    password_secure=db.Column(db.String(255))
    location=db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    
    blog = db.relationship('Blog', backref='user', lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password atribute')

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
    This is a class to define news details objects
    '''
    def __init__(self,id, quote,author):
        self.id = id
        self.quote=quote
        self.author=author

class Blog(db.Model):
    __tablename__ = 'blog'
    
    comment = db.relationship('Comment', backref='comments', lazy='dynamic')

    id = db.Column(db.Integer, primary_key=True)
    blog_category = db.Column(db.String(255))
    blog_title=db.Column(db.String(255))
    blog_content=db.Column(db.String(255))
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"))
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()
        

class Comment(db.Model):
    __tablename__="comments"
   
    id=db.Column(db.Integer, primary_key=True)
    comment_data=db.Column(db.String(255))
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    blog_id=db.Column(db.Integer,db.ForeignKey("blog.id"))
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_comment(cls,id):
        comments = Comment.query.filter_by(blog_id=id).all()
        return comments
    
    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()
    
    def __repr__(self):
        return f"Comment {self.comments}, {self.posted}"
    
    # @classmethod
    # def get_comments(cls,id):
    #     response = []
    #     for comment in cls.all_comments:
    #         if comment.blog_id==id:
    #             response.append(comment)
    #     return response
            
    
    
 
