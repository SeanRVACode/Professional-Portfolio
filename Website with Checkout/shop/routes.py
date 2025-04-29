from shop import app
from shop.forms import LoginForm, RegistrationForm
from flask import render_template, flash, redirect, url_for, request, session
from flask_login import current_user, login_user, logout_user, login_required
from shop import db
from shop.models import User
from shop import stripe
from shop.utils.cart import Cart
from icecream import ic


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
            return redirect(url_for("login"))
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
    else:
        # TODO Fix this to go to actual register page. Currently for debugging purposes.
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(
                username=form.username.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Congratulations, you are now a registered user!", "success")
            return redirect(url_for("login"))
        return render_template("register.html", form=form)


@app.route("/add_to_cart", methods=["POST"])
@login_required
def add_to_cart_route():
    product_id = request.form.get("item_id")
    ic(product_id)
    if not product_id:
        # Handle missing product_id (e.g., flash error)
        flash("Non-Valid Product ID", "danger")
        return redirect(url_for("index"))

    if "cart_details" not in session:
        # Set up cart details
        session["cart_details"] = {}

    if "cart" not in session:
        # Set up cart
        session["cart"] = {}

    try:
        product_details = stripe.get_single_product(product_id)
        if not product_details:
            flash("Invalid Item ID", "danger")
            return redirect(url_for("index"))

    except Exception as e:
        ic(e)
        flash("Unable to validate product. Please try again later.", "danger")

    cart = Cart(session)
    cart.add_to_cart(product_id, product_details)
    return redirect(url_for("index"))


@app.route("/update_cart", methods=["POST"])
@login_required
def update_cart():
    product_id = request.form.get("product_id")
    action = request.form.get("action")
    cart = Cart(session)
    cart.update_cart(product_id_str=product_id, action=action)
    return redirect(url_for("index"))


@app.route("/checkout", methods=["POST"])
@login_required
def stripe_checkout():
    cart = Cart(session)
    try:
        ic("Starting Checkout Session")
        checkout_session = stripe.create_checkout_session(
            line_items=cart.convert_to_line_item(),
            mode="payment",
            success_url=url_for(
                "success", _external=True
            ),  # By having _external=True this ensures that flask generates full URLs including the domain which is what stripe requires.
            cancel_url=url_for("cancel", _external=True),
        )
    except Exception as e:
        ic(e)

    return redirect(checkout_session.url, code=303)


@app.route("/myaccount", methods=["GET", "POST"])
@login_required
def account():
    return render_template("account.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/cancel")
def cancel():
    # Send them back to the home page instead of cancel page.
    return redirect(url_for("index"))
