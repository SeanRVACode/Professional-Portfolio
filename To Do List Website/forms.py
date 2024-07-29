from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,StringField,SubmitField
from wtforms.validators import DataRequired,URL
from flask_ckeditor import CKEditorField



# WTForm for Registration
class RegisterForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = EmailField("Email",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Register")
    
# WTForm for login
class LoginForm(FlaskForm):
    email = EmailField("Email",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Log In")

