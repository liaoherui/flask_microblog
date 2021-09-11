from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,ValidationError,Length
from app.models import User


class EmptyForm(FlaskForm):
	submit=SubmitField('Submit')


class EditProfileForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	about_me = TextAreaField('About_me', validators=[Length(min=0, max=140)])
	submit = SubmitField('Submit')

class PostForm(FlaskForm):
	post = TextAreaField('Say something', validators=[DataRequired(), Length(min=1, max=140)])
	submit = SubmitField('Submit')

