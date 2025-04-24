from shop import app
from shop.forms import LoginForm
from flask import render_template, flash, redirect, url_for


@app.route("/")
@app.route("/index")
def index():
    pass


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Welcome, {form.username.data}!", "success")
        return redirect(url_for("index"))
    return render_template("login.html", form=form)
