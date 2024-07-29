from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
import os
import secrets
from dotenv import load_dotenv
from flask_login import UserMixin,login_required,login_user,LoginManager,current_user,logout_user
from flask_bootstrap import Bootstrap5
from sqlalchemy import ForeignKey,Integer,String,Text,Boolean
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from forms import LoginForm
from flask_ckeditor import CKEditor



# Load environment file
load_dotenv()

# Set up DB Path
DB_NAME = r'instance\todo_app.db'
TOP_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(TOP_DIR,DB_NAME)



# ----------------- Flask App -------------------- #
app = Flask(__name__)
secret_key = os.getenv('secret_key')
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_path
ckeditor = CKEditor(app)
Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)

# ----------------- Set up Databases -------------------- #

db = SQLAlchemy(app)

# User Database
class User(UserMixin,db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(db.Integer,primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100),nullable=False)
    email:Mapped[str] = mapped_column(db.String(100),unique=True,nullable=False)
    password:Mapped[str] = mapped_column(db.String(1000),nullable=False)
    
    # One-to-many relationship: User -> Todo
    todos: Mapped[list['Todo']] = relationship("Todo",back_populates='user')

# Todo list database    
class Todo(db.Model):
    __tablename__ = 'todos'
    id: Mapped[int] = mapped_column(db.Integer,primary_key=True)
    title: Mapped[str] = mapped_column(db.String(100),nullable=False)
    description: Mapped[str] = mapped_column(db.String(250))
    completed: Mapped[bool] = mapped_column(db.Boolean,nullable=False,default=False)
    user_id: Mapped[int] = mapped_column(db.Integer,db.ForeignKey('users.id'))
    user: Mapped["User"] = relationship("User",back_populates="todos")
    
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


with app.app_context():
    db.create_all()




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and check_password_hash(user.password,form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        elif not user:
            flash("That email does not exist within our system.")
            redirect(url_for('login'))
        elif not check_password_hash(user.password,form.password.data):
            flash("Password is incorrect. Please try again.")
            return redirect(url_for('login'))
    return render_template('login.html',form=form)
