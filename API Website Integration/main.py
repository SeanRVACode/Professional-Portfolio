from flask import Flask,redirect,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)