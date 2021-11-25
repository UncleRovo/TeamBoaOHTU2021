from app import app
from flask import render_template, request

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/browse")
def browse():
    return render_template("browse.html")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/add", methods=['GET', 'POST'])
def add():
    type = request.form.get("type")
    if type == "article":
        return render_template("newarticle.html")
    else:
        return render_template("new.html")