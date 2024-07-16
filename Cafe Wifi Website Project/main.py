from ast import Sub
from types import MappingProxyType
from flask import Flask,render_template,url_for,jsonify,request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm,va
from wtforms import StringField, SubmitField,URLField,TimeField,BooleanField
from wtforms.validators import DataRequired,url
import csv
import os.path
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import URL, Integer, String, Boolean
import json




# Ini database
class Base(DeclarativeBase):
    pass
    
db = SQLAlchemy(model_class=Base)

# Ini app
app = Flask(__name__)

db_name = 'cafes.db'
TOP_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(TOP_DIR,db_name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_path
db.init_app(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)

# db.Model is a base class for all models in SQLAlchemy when using flask-sqlalchemy. 
# It allows cafe to be recognized as a database model.
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    name: Mapped[str] = mapped_column(String(250),unique=True,nullable=False)
    map_url: Mapped[str] = mapped_column(String(500),nullable=False)
    img_url: Mapped[str] = mapped_column(String(500),nullable=False)
    location: Mapped[str] = mapped_column(String(250),nullable=False)
    seats: Mapped[str] = mapped_column(String(250),nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean,nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean,nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean,nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean,nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250),nullable=True)
    
    def to_dict(self):
        return {column.name: getattr(self,column.name) for column in self.__table__.columns}

class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name',validators=[DataRequired()])
    map_url = URLField('Cafe Map URL',validators=[DataRequired(),url()])
    img_url = URLField('Cafe Picture URL',validators=[DataRequired(),url()])
    location = StringField('Cafe Address',validators=[DataRequired()])
    seats = StringField('Number of Seats',validators=[DataRequired()])
    has_toilet = BooleanField('Has Toilets?',validators=[DataRequired()])
    has_wifi = BooleanField('Has WiFi?',validators=[DataRequired()])
    has_sockets = BooleanField('Has Sockets?',validators=[DataRequired()])
    can_take_calls = BooleanField('Can you take calls?',validators=[DataRequired()])
    coffee_price = StringField('Coffee Price',validators=[DataRequired()])
    submit = SubmitField('Submit')
    

# Create application context
# Flask needs an application context to work with databases.
# This ensures that db.create_all() runs within the correct context

with app.app_context():
    # db.create_all() creates all tables defined by the models in the database.
    # If the table already exist it does nothing.
    db.create_all()
    

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/cafes')
def cafes_list():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    # cafes_json_list = [cafe for cafe in cafes]
    print(cafes)
    return render_template('cafes.html',cafes=cafes)



@app.route('/add',methods=['POST'])
def add_cafe():
    
    form = CafeForm()
    if form.validate_on_submit():
        print('True')
        form_data = {field.name: field.data for field in form}
        new_cafe = Cafe(
            name=form_data['name'],
            map_url=form_data['map_url'],
            img_url=form_data['img_url'],
            location=form_data['location'],
            seats=form_data['seats'],
            has_toilet=form_data['has_toilet'],
            has_wifi=form_data['has_wifi'],
            
        )
    
