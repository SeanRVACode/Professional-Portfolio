from shop import app
from shop.forms import LoginForm
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
import sqlalchemy as sa
from shop import db
from shop.models import User
from shop import stripe


@app.route("/")
@app.route("/index")
def index():
    products = stripe.get_products()
    return render_template("store.html", products=products["data"])


@app.route("/login", methods=["GET", "POST"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password", "danger")
            return redirect(url_for("login_page"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("index"))
    return render_template("login.html", form=form)


@app.route("/add_to_cart",methods=["POST"])
def add_to_cart()