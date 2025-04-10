from flask import Flask, get_flashed_messages
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return "<p> Hello World!</p>"
