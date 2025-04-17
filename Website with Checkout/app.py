from flask import Flask, render_template, session, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from stripe_payment import Stripe
from icecream import ic

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = "development"
Bootstrap5(app)


# Create Database
class Base(DeclarativeBase):  # TODO Figure out what this does and why
    pass


# Ini Stripe
stripe = Stripe()

# Config App
app.permanent_session_lifetime = timedelta(minutes=30)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    r"sqlite:///D:\Databases\Checkout Database\instance\project.db"  # Points to Portable Hard Drive
)
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
    products = get_products()

    return render_template("store.html", products=products["data"])


@app.route("/checkout")
def checkout():
    subtotal = 0
    if "cart" in session:
        cart_items = []
        for item in session["cart"]:
            ic("this is the item ", item)
            item_descriptions = Products.query.filter_by(id=item).first()
            ic(session["cart"][item])
            cart_items.append(
                {
                    "name": item_descriptions.name,
                    "price": item_descriptions.price,
                    "quantity": session["cart"][item],
                    "subtotal": session["cart"][item] * item_descriptions.price,
                }
            )
            ic(cart_items)
            subtotal += session["cart"][item] * item_descriptions.price
            ic(subtotal)
    else:
        return redirect(url_for("home"))
    return render_template("checkout.html", cart_items=cart_items, subtotal=subtotal)


@app.route("/cart", methods=["POST"])
def add_to_cart():
    item_id = request.form.get("item_id")
    # product = Products.query.filter_by(id=item_id).first()
    # Convert item_id to string since dictionary keys must be strings
    item_id_str = str(item_id)
    if "cart" not in session:
        session["cart"] = {}
    if item_id_str in session["cart"]:
        session["cart"][item_id_str] += 1
    else:
        session["cart"][item_id_str] = 1

    session.modified = True
    ic(session["cart"])
    # product = Products.query.filter(Products.id == id)
    return redirect(url_for("home"))


def get_products():
    products = stripe.get_products()
    # products = db.session.execute(db.select(Products).order_by(Products.name)).scalars()
    return products
