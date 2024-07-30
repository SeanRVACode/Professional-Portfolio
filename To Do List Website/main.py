from flask import Flask,render_template,url_for,flash,redirect,abort,request
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
from forms import LoginForm, RegisterForm, TodoForm
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
    task: Mapped[str] = mapped_column(db.String(100),nullable=False)
    # description: Mapped[str] = mapped_column(db.String(250))
    completed: Mapped[bool] = mapped_column(db.Boolean,nullable=False,default=False)
    user_id: Mapped[int] = mapped_column(db.Integer,db.ForeignKey('users.id'))
    user: Mapped["User"] = relationship("User",back_populates="todos")
    
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


with app.app_context():
    db.create_all()




@app.route("/",methods=['GET','POST'])
def home():
    if current_user.is_authenticated:
        todos = current_user.todos
        form = TodoForm()
        if form.validate_on_submit():
            new_todo = Todo(
                task= form.task.data,
                user = current_user
            )
            flash('To-Do item added!','success')
            db.session.add(new_todo)
            db.session.commit()
            return redirect(url_for('home'))
        return render_template('index.html',todos=todos,form=form)
    else:
        return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and check_password_hash(user.password,form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        elif not user:
            flash("That email does not exist within our system.",'danger')
            redirect(url_for('login'))
        elif not check_password_hash(user.password,form.password.data):
            flash("Password is incorrect. Please try again.",'danger')
            return redirect(url_for('login'))
    return render_template('login.html',form=form)


@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        email_exist = User.query.filter_by(email=email).first()
        print('Test this: ',email_exist)
        if email_exist:
            flash("Email already registered. Please login.",'danger')
            return redirect(url_for('login'))
        elif not email_exist:
            new_user = User(
                name = form.name.data,
                email = form.email.data,
                password = generate_password_hash(form.password.data,method='scrypt',salt_length=8)
            )
            db.session.add(new_user)
            db.session.commit()
            
            # Log the user in
            login_user(new_user)
            return redirect(url_for('home'))
    return render_template('register.html',form=form)

# @app.route('/todos',methods=['GET','POST'])
# @login_required
# def todos():
#     form = TodoForm()
#     if form.validate_on_submit():
#         new_todo = Todo(
#             task = form.task.data,
#             user = current_user
#         )
#         flash('To-Do item added!','success')
#         db.session.add(new_todo)
#         db.session.commit()
#         return redirect(url_for('todos'))
#     page = request.args.get('page',1,type=int)
#     user_todos = current_user.todos
#     return render_template('todos.html',form=form,todos=user_todos)
        
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/complete/<int:todo_id>')
@login_required
def complete(todo_id):
    source = request.args.get('source','home')
    todo = Todo.query.get_or_404(todo_id)
    if todo.user != current_user:
        abort(403)
    todo.completed = not todo.completed
    db.session.commit()
    if source == 'index':
        return redirect(url_for('home'))
 

@app.route('/delete/<int:todo_id>')
@login_required
def delete(todo_id):
    source = request.args.get('source','home')
    todo = Todo.query.get_or_404(todo_id)
    if todo.user != current_user:
        abort(403)
    db.session.delete(todo)
    db.session.commit()
    if source == 'index':
        return redirect(url_for('home'))
 