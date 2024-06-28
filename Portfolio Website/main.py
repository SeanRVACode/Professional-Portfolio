from datetime import date
from flask import Flask, abort, render_template, redirect,url_for,flash
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)

@app.route('/')
def home():
    thumb_path = '.static/assets/img/portfolio/thumbnails/'
    full_path = '.static/assets/img/portfolio/fullsize/'
    return render_template('index.html',thumb_path=thumb_path,full_path=full_path)

# Handles the redirect for thumbnail images so I don't have to type url_for a ton
@app.route('/assets/img/portfolio/thumbnails/<img>')
def thumbnails(img):
    return redirect(f'/static/assets/portfolio/thumbnails/{img}')

@app.route('/assets/img/portfolio/fullsize/<img>')
def fullsize(img):
    return redirect(f'/static/assets/portfolio/fullsize/img')