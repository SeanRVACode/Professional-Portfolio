from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
import sqlalchemy as sa
from app import db
from app.models import User


class LoginForm(FlaskForm):
    username = StringField("UserName", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    username = StringField("UserName", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = db.session.query(User).filter(User.username == username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")

        def validate_email(self, email):
            user = db.session.query(User).filter(User.email == email.data).first()
            if user is not None:
                raise ValidationError("Please use a different email address.")
