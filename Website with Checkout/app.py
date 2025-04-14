from flask import Flask, get_flashed_messages, render_template
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text


load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = "development"
Bootstrap5(app)


# Create Database
class Base(DeclarativeBase):  # TODO Figure out what this does and why
    pass


# Config App
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"  # TODO Need to finish this with an actual database?
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Shop Table
class Products(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    name: Mapped[str] = mapped_column()
    amount: Mapped[int] = mapped_column()
    price: Mapped[float] = mapped_column()
    source: Mapped[str] = mapped_column()


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    # FIXME Currently rendering checkout.html for testing purposes
    products = get_products()
    return render_template("store.html", products=products)


@app.route("/checkout")
def cart():
    return render_template("checkout.html")


def get_products():
    products = db.session.execute(db.select(Products).order_by(Products.name)).scalars()
    return products
