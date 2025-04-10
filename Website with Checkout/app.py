from flask import Flask, get_flashed_messages, render_template
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
Bootstrap5(app)


@app.route("/")
def home():
    # FIXME Currently rendering checkout.html for testing purposes
    return render_template("checkout.html")
