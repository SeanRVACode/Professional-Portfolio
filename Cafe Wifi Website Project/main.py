from ast import Sub
from types import MappingProxyType
from flask import Flask,render_template,url_for,jsonify,request,flash,redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,URLField,TimeField,BooleanField
from wtforms.validators import DataRequired,url
import os.path
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import URL, Integer, String, Boolean




# Ini database
class Base(DeclarativeBase):
    pass
    
db = SQLAlchemy(model_class=Base)

# Ini app
app = Flask(__name__)

db_name = 'instance\cafes.db'
TOP_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(TOP_DIR,db_name)
print(db_path)
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
    
    has_toilet: Mapped[bool] = mapped_column(Boolean,nullable=False,default=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean,nullable=False,default=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean,nullable=False,default=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean,nullable=False,default=False)
    seats: Mapped[str] = mapped_column(String(250),nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250),nullable=True)
    
    def to_dict(self):
        return {column.name: getattr(self,column.name) for column in self.__table__.columns}

class CafeForm(FlaskForm):
    name = StringField('Cafe Name',validators=[DataRequired()])
    map_url = URLField('Cafe Map URL',validators=[DataRequired(),url()])
    img_url = URLField('Cafe Picture URL',validators=[DataRequired(),url()])
    location = StringField('Location',validators=[DataRequired()])
    
    has_toilet = BooleanField('Has Toilets?',default=False)
    has_wifi = BooleanField('Has WiFi?',default=False)
    has_sockets = BooleanField('Has Sockets?',default=False)
    can_take_calls = BooleanField('Can you take calls?',default=False)
    seats = StringField('Number of Seats',validators=[DataRequired()])
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
    cafes_list = [[cafe.id,cafe.name,cafe.map_url,cafe.img_url,cafe.location,cafe.has_sockets,cafe.has_toilet,cafe.has_wifi,cafe.can_take_calls,cafe.seats,cafe.coffee_price] for cafe in cafes]
    headers = [column.name for column in Cafe.__table__.columns]
    return render_template('cafes.html',cafes=cafes_list,headers=headers)



@app.route('/add',methods=['POST','GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        form_data = {field.name: field.data for field in form}
        print(form_data['name'])
        exist = Cafe.query.filter_by(name=form_data['name']).first()
        
        if exist:
            flash('Cafe already exist!','danger')
            return render_template('addcafe.html',form=form)
        else:
            print('True')
            
            new_cafe = Cafe(
                name=form_data['name'],
                map_url=form_data['map_url'],
                img_url=form_data['img_url'],
                location=form_data['location'],
                seats=form_data['seats'],
                has_toilet=bool(form_data['has_toilet']),
                has_wifi=bool(form_data['has_wifi']),
                has_sockets=bool(form_data['has_sockets']),
                can_take_calls=bool(form_data['can_take_calls']),
                coffee_price=form_data['coffee_price'],
                
            )
            with app.app_context():
                db.session.add(new_cafe)
                db.session.commit()
            flash('Cafe Added!','success')
            return redirect(url_for('cafes_list'))
    return render_template('addcafe.html',form=form)
    

@app.route('/edit_cafe/<int:cafe_id>',methods=['GET','POST'])
def edit_cafe(cafe_id):
    cafe = db.session.get(Cafe,cafe_id)
    form = CafeForm(obj=cafe)
    if form.validate_on_submit():
        form.populate_obj(cafe)
        db.session.commit()
        flash('Cafe updated successfully!','success')
        return redirect(url_for('cafes_list'))
    return render_template('edit_cafe.html',cafe=cafe,form=form,cafe_id=cafe.id)

@app.route('/delete_cafe/<int:cafe_id>',methods=['GET','POST','DELETE'])
def delete_entry(cafe_id):
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        flash('Cafe deleted successfully!','success')
        return redirect(url_for('cafes_list'))
    else:
        flash('Cafe not found.','error')
    return redirect(url_for('cafes_list'))