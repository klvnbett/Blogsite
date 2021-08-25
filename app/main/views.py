from flask_login import current_user,login_required
from flask import render_template,request,redirect,url_for
from .. import db
from .. requests import get_quote
from .. models import Blog,Quotes
from . import main
from . forms import BlogForm

@main.route('/')

def index():
    """
    Root function that returns index page and the date
    """
    title ='Welcome to the Best Quotes in Town'
    quote=get_quote()

    return render_template('index.html',quote=quote)


@main.route('/home',methods=['GET','POST'])
@login_required
def main():
    blog_form=BlogForm()
    if blog_form.validate_on_submit():
        blog_category=blog_form.blog_category.data
        blog_title=blog_form.blog_title.data
        blog_content=blog_form.blog_content.data

        new_blog=Blog(blog_category=blog_category,blog_title=blog_title,blog_content=blog_content)


        new_blog.save_blog()
        db.session.add(new_blog)
        db.session.commit()
        
        return redirect(url_for('main.main'))
    else:
        blogs=Blog.query.order_by(Blog.posted).all()
    return render_template('main/main.html',blog_form=blog_form, blogs=blogs)

@main.route('/home/comment/</int:id')
@login_required
def comments(id):
    comment_form=comment()
    if blog_form.validate_on_submit:
        comment=comment_form.blog_comment.data


    return render_template('main_templates/comment.html',comment_form=comment_form)




