from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from website.models import User, Dataset

# form for registration
class Register(FlaskForm):
    username = StringField('Email', validators=[DataRequired(), Length(min=5, max=60)])    
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That email has already been used')

# form for logging in
class Login(FlaskForm):
    username = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Sign In')  