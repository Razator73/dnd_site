from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Optional

from app import imagefiles
from app.models import User, Role


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


# noinspection PyMethodMayBeStatic
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-enter Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username already taken. Please try something else.')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email already taken. Please try something else.')


class EditUserForm(FlaskForm):
    roles = [r.name for r in Role.query.all()]
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    role = SelectField('Role', choices=roles, validators=[DataRequired()])
    profile_picture = FileField('Upload Profile Picture',
                                validators=[FileAllowed(imagefiles, 'Images only'), Optional()])
    submit = SubmitField('Update')

    def __init__(self, user, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.user = user

    def validate_username(self, username):
        if username.data != self.user.username and User.query.filter_by(username=username.data).first():
            raise ValidationError('Username is already taken. Please use a different username')

    def validate_email(self, email):
        if email.data != self.user.email and User.query.filter_by(email=email.data).first():
            raise ValidationError('Email is already taken. Please use a different email')
