from flask import render_template, request, redirect
from app import app
import articles

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/browse")
def browse():
    article_list = articles.get_all()
    return render_template("browse.html", articles=article_list)

@app.route("/new") ##tarvitseeko tätä? tiedostonimi on new.html,reitti on /add > tulee selkeyttää.
def new():
    return render_template("new.html")

@app.route("/add", methods=['GET', 'POST']) #pitäisikö täm äsiis olla /new?
def add():
    type = request.form.get("type")
    if type == "article":
        return render_template("newarticle.html")
    else:
        return render_template("new.html")

@app.route("/newarticle", methods=['GET', 'POST'])
def new_article():
    if request.method == "GET":
        return render_template("newarticle.html")
    if request.method == "POST":
        article_title = request.form["title"] #Add conditions later? Cannot be empty etc.
        article_author = request.form["author"]
        article_url = request.form["url"]
        if articles.add_new_article(article_title, article_author, article_url):
            return redirect("/")
        else: # error-sivu (?) lisättävä myöhemmin
            return redirect("new_article")
