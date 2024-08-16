from flask import Flask,render_template,url_for,jsonify,request,flash,redirect
from flask_bootstrap import Bootstrap5



# Ini flask app
app = Flask(__name__)
Bootstrap5(app)


# Homepage
@app.route("/")
def home():
    return render_template("index.html")