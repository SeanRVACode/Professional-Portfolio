from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
from shop.api.stripe_payment import Stripe

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
bootstrap = Bootstrap5(app)
# TODO Verify this is the correct way to initialize Stripe later.
stripe = Stripe()
load_dotenv()

# We import the routes here to avoid circular imports
from shop import models, routes


if __name__ == "__main__":
    print(__name__)
