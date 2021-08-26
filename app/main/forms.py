from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,SelectField,IntegerField
from wtforms.validators import Required


class BlogForm(FlaskForm):
        blog_category=SelectField('Category',validators=[Required()],choices=[('Select your blog category','Select your blog category'),('Technology','Technology'),('Sports','Sports'),('Politics','Politics'),('Adventure','Adventure'),('Agriculture','Agriculture'),('Business',"Business"),('Others',"Others")])
        blog_title=StringField('Title',validators=[Required()])
        blog_content=TextAreaField('Content',validators=[Required()])
        submit =SubmitField('Submit')

class CommentForm(FlaskForm):
    comment_data=TextAreaField('Write your comment',validators=[Required()])
    submit=SubmitField('Post your Reservations')
class DeleteBlog(FlaskForm):
    submit=SubmitField('Delete')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('What are your intresets.',validators = [Required()])
    submit = SubmitField('Submit')