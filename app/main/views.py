from flask import render_template, request, redirect, url_for,abort
from flask_login import current_user, login_required

from .. import db,photos
from ..models import Blog, Quotes,Comment,User
from ..requests import get_quote
from . import main
from ..email import mail_message
from .forms import BlogForm,CommentForm

#views

@main.route('/',methods=['GET'])
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    title='Welcome to blogging site'
    quote = get_quote()
    return render_template('index.html',quote=quote)


@main.route('/home',methods=['GET','POST'])
@login_required
def main_page():
    blog_form=BlogForm()
    if blog_form.validate_on_submit():
        blog_category=blog_form.blog_category.data
        blog_title=blog_form.blog_title.data
        blog_content=blog_form.blog_content.data
        
        new_blog=Blog(blog_category=blog_category,blog_title=blog_title,blog_content=blog_content)
       
        
        new_blog.save_blog()
        db.session.add(new_blog)
        db.session.commit()
        
        return redirect(url_for('main.main_page'))
    else:
        blogs=Blog.query.order_by(Blog.posted).all()
    return render_template('main_templates/main.html',blog_form=blog_form, blogs=blogs)


@main.route('/new_comment/<int:blog_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(blog_id):
    
    blogs = Blog.query.filter_by(id = blog_id).first()
    form = CommentForm()
    
    comm =Comment.get_comment(blog_id)
    
    if form.validate_on_submit():
        comment = form.comment_data.data
        new_comment = Comment(comment_data=comment,user_id=current_user.id, blog_id=blog_id)
        new_comment.save_comment()
        

        return redirect(url_for('main.new_comment',blog_id=blog_id))
    title='New Blog'
    return render_template('main_templates/new_comment.html',comment=comm,title=title,comment_form = form,blog_id=blog_id)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
        
    return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
