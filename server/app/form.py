from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from server.app.init import db
from server.app.models.model import User


class LoginForm(FlaskForm):
    id = StringField('id', validators=[DataRequired('id is null')])
    password = PasswordField('password', validators=[DataRequired('password is null')])
    login = SubmitField('login')
    logout = SubmitField('logout')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = db.session.query(User).filter(User.email == email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
