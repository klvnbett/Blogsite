from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,SelectField,IntegerField
from wtforms.validators import Required


class BlogForm(FlaskForm):
blog_category=SelectField('choose category' ,validators=[required()],choices=[('select blog category','select blog category'),('Tech','Tech'),('others','others')])
blog_title=StringField('Title',validators=[Required()])
blog_content=TextAreaField('Content',validators=[Required()])
submit =SubmitField('Submit')