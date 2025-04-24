from shop import app
from shop.forms import LoginForm
from flask import render_template, flash, redirect, url_for, request, session
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
from shop import db
from shop.models import User
from shop import stripe
from shop.utils.cart import Cart


@app.route("/")
@app.route("/index")
def index():
    products = stripe.get_products()
    return render_template("store.html", products=products["data"])


@app.route("/login", methods=["GET", "POST"])
def login():
    # Prevents logged-in users from accessing the login page.
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


@app.route("/logout")
def logout():
    # TODO Verify that the user actually gets logged out.
    if current_user.is_authenticated:
        logout_user()
        # TODO should I clear the cart session on logout?
        flash("You have been logged out", "success")
    else:
        flash("You were not logged in", "warning")
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    # TODO Fix this to go to actual register page. Currently for debugging purposes.
    return redirect(url_for("index"))


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart_route():
    product_id = request.form.get("product_id")
    if not product_id:
        # Handle missing product_id (e.g., flash error)
        flash("Non-Valid Product ID", "danger")
        return redirect(url_for("index"))

    product_data = stripe.get_single_product(product_id)
    cart = Cart(session)
    cart.add_to_cart(product_id, product_data)
