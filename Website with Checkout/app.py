from flask import Flask, get_flashed_messages, render_template
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

app = Flask(__name__)
Bootstrap5(app)


# Create Database
class Base(DeclarativeBase):  # TODO Figure out what this does and why
    pass


# Config App
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"  # TODO Need to finish this with an actual database?

# Shop Table


@app.route("/")
def home():
    # FIXME Currently rendering checkout.html for testing purposes
    return render_template("store.html")


@app.route("/checkout")
def cart():
    return render_template("checkout.html")


def get_products():
    # Need to finish this function
    pass
