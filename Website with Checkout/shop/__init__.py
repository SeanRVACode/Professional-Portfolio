from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# We import the routes here to avoid circular imports
from shop import models, routes


if __name__ == "__main__":
    print(__name__)
