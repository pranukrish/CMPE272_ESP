from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import DataRequired 


class CreateTweet(FlaskForm):
	tweet = StringField('Tweet You want to Create : ', validators=[DataRequired()])
	submit = SubmitField('Create')

class SearchForm(FlaskForm):
	userId = StringField("Enter twitter id :", validators=[DataRequired()])
	search = SubmitField('Search')


class DeleteForm(FlaskForm):
	deleteTweetId = StringField("Enter tweet id that you want to delete : ", validators=[DataRequired()])
	delete = SubmitField('Delete')