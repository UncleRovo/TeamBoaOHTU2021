from flask import render_template, request, redirect
from app import app
from articles import Articles

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/browse")
def browse():
    article_list = articles.get_all()
    return render_template("browse.html", articles=article_list)

@app.route("/new_choose_type", methods=['GET', 'POST'])
def new_choose_type():
    if request.method == "GET":
        return render_template("new_choose_type.html")
    if request.method == "POST":
        type = request.form.get("type")
        if type == "article":
            return redirect("/new_article")
        else:
            return render_template("new_choose_type.html")

#"/add" poistettu, liitetty "new_choose_typeen", joka ennen oli nimellä "new"

@app.route("/new_article", methods=['GET', 'POST'])
def new_article():
    if request.method == "GET":
        return render_template("new_article.html")
    if request.method == "POST":
        article_title = request.form["title"] #Add conditions later? Cannot be empty etc.
        article_author = request.form["author"]
        article_url = request.form["url"]
        if articles.add_new_article(article_title, article_author, article_url):
            return redirect("/")
        else: # error-sivu (?) lisättävä myöhemmin
            return redirect("/new_article")
