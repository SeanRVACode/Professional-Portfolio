from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
import sqlalchemy as sa
from shop import db
from shop.models import User


class LoginForm(FlaskForm):
    username = StringField("UserName", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    username = StringField("UserName", validators=[DataRequired()])

    # Personal Info
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])

    # # Address Info
    # address_line1 = StringField("Address Line 1", validators=[DataRequired()])
    # address_line2 = StringField("Address Line 2")
    # city = StringField("City", validators=[DataRequired()])
    # state = StringField("State", validators=[DataRequired()])
    # postal_code = StringField("Postal Code", validators=[DataRequired()])
    # country = StringField("Country", validators=[DataRequired()])

    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        user = db.session.query(User).filter(User.email == email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email address.")


class AccountForm(FlaskForm):
    new_email = EmailField("New Email")
    new_password = PasswordField("New Password")
    confirm_password = PasswordField("Confirm Password")
    submit = SubmitField("Update")

    # TODO add address information to form

    def confirm_email(self, new_email):
        if new_email == db.session.query(User).filter(User.email).first():
            raise ValidationError("Please use a different email address.")

    def check_password_match(self, new_password, confirm_password):
        if new_password != confirm_password:
            raise ValidationError("Passwords do not match.")
