from shop import app
from shop.models import User, StoredPaymentMethod, Order


# from flask import Flask, render_template, session, request, redirect, url_for, flash
# from flask_bootstrap import Bootstrap5
# from dotenv import load_dotenv
# from datetime import timedelta
# from stripe_payment import Stripe
# from icecream import ic
# from shop.forms import LoginForm
# from flask_login import LoginManager, UserMixin
# from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


# load_dotenv()
# app = Flask(__name__)
# app.config.from_object(Config)


# # Ini Database
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


# Bootstrap5(app)

# # Ini Stripe
# stripe = Stripe()

# # Config App
# app.permanent_session_lifetime = timedelta(minutes=30)

# # Ini Login Manager
# # login = LoginManager(app)


# @app.route("/")
# def home():
#     products = get_products()

#     return render_template("store.html", products=products["data"])


# @app.route("/login", methods=["GET", "POST"])
# def login_page():
#     form = LoginForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data
#         remember_me = form.remember_me.data
#         flash(f"Welcome, {username}!", "success")
#         return redirect(url_for("home"))
#     return render_template("login.html", form=form)


# @app.route("/register")
# def register():
#     pass


# @app.route("/checkout")
# def checkout():
#     subtotal = 0
#     if "cart" in session:
#         cart_items = []
#         for item in session["cart"]:
#             ic("this is the item ", item)
#             item_descriptions = stripe.get_single_product(id=item)
#             ic(session["cart"][item])
#             cart_items.append(
#                 {
#                     "name": item_descriptions.name,
#                     "price": session["cart_details"][item]["price"],
#                     "quantity": session["cart"][item],
#                     "subtotal": session["cart"][item] * session["cart_details"][item]["price"],
#                 }
#             )
#             ic(cart_items)
#             subtotal += session["cart"][item] * session["cart_details"][item]["price"]
#             ic(subtotal)
#     else:
#         flash("Your cart is empty. Add items to continue", "Warning")
#         return redirect(url_for("home"))
#     return render_template("checkout.html", cart_items=cart_items, subtotal=subtotal)


# @app.route("/create_checkout_session", methods=["POST"])
# def stripe_checkout():
#     try:
#         ic("Trying checkout_session")
#         ic(session["cart"])
#         checkout_session = stripe.create_checkout_session(
#             line_items=convert_to_line_item(),
#             mode="payment",
#             success_url=url_for(
#                 "success", _external=True
#             ),  # by having _external=True this ensures that Flask generates full URLs including the domain which is what stripe requires.
#             cancel_url=url_for("home", _external=True),  # Takes you back to the store home page
#         )
#         ic(checkout_session)
#     except Exception as e:
#         return str(e)

#     return redirect(checkout_session.url, code=303)


# @app.route("/success")
# def success():
#     return render_template("success.html")


# @app.route("/cancel")
# def cancel():
#     return render_template("cancel.html")


# @app.route("/cart", methods=["POST"])
# def add_to_cart() -> str:
#     item_id = request.form.get("item_id")

#     if not item_id:
#         flash("No product selected. Please choose a product.", "error")
#         return redirect(url_for("home"))

#     if "cart_details" not in session:
#         # Set up cart details
#         session["cart_details"] = {}

#     item_id_str = str(item_id)
#     try:
#         product_data = stripe.get_single_product(id=item_id_str)
#         if not product_data:
#             flash("The selected product is invalid. Please try again.", "error")
#             return redirect(url_for("home"))

#     except Exception as e:
#         ic(e)
#         flash("Unable to validate product. Please try again later.", "error")
#         return redirect(url_for("home"))

#     if "cart" not in session:
#         session["cart"] = {}
#     if item_id_str in session["cart"]:
#         session["cart"][item_id_str] += 1
#     else:
#         session["cart"][item_id_str] = 1
#         # Store Product Details
#         session["cart_details"][item_id_str] = {
#             "name": product_data.name,
#             "price": stripe.get_price(product_data.default_price),
#         }

#     ic(session["cart_details"])
#     session.modified = True
#     flash(f"{product_data.name} added to cart!", "success")
#     ic(session["cart"])
#     # product = Products.query.filter(Products.id == id)
#     return redirect(url_for("home"))


# @app.route("/update_cart", methods=["POST"])
# def update_cart():
#     product_id = request.form.get("product_id")
#     action = request.form.get("action")
#     if product_id and action and "cart" in session:
#         if action == "increase":
#             session["cart"][product_id] += 1
#         elif action == "decrease":
#             if session["cart"][product_id] > 1:
#                 session["cart"][product_id] -= 1
#             else:
#                 # Remove the item completely
#                 session["cart"].pop(product_id)
#         elif action == "remove":
#             # Completely removes the item regardless of quantity
#             session["cart"].pop(product_id)

#         session.modified = True

#     return redirect(url_for("home"))


# def get_products() -> list:
#     products = stripe.get_products()
#     # products = db.session.execute(db.select(Products).order_by(Products.name)).scalars()
#     return products


# def convert_to_line_item() -> list:
#     line_items = [
#         {"price": stripe.get_single_product(item_id)["default_price"], "quantity": quantity}
#         for item_id, quantity in session["cart"].items()
#     ]

#     # line_items = []
#     # ic(f"Current Items in Cart:{session['cart']}")
#     # for _ in session["cart"]:
#     #     ic(_)
#     #     line_item = {"price": stripe.get_single_product(_)["default_price"], "quantity": session["cart"][_]}
#     #     line_items.append(line_item)
#     # ic(line_items)
#     return line_items
