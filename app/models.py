from . import db
from datetime import datetime

class Blog(db.Model):
    __tablename__ = 'blog'