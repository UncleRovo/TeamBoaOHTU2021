from flask import render_template, request, redirect
from app import app
from app import db
import articles, blogs, user, videos, books

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/browse")
def browse():
    if (user.isLoggedIn()):
        u_id = user.get_id()
        return render_template("browse.html", blogs=blogs.get_by_user(u_id),
                                          articles=articles.get_by_user(u_id),
                                          videos=videos.get_by_user(u_id),
                                          books=books.get_by_user(u_id))
    return redirect("/")

@app.route("/new_choose_type", methods=["GET", "POST"])
def new_choose_type():
    if (user.isLoggedIn() == False):
        return redirect("/")
        
    if request.method == "GET":
        return render_template("new_choose_type.html")
    if request.method == "POST":
        type_of = request.form.get("type")
        if type_of == "article":
            return redirect("/new_article")
        elif type_of == "blog":
            return redirect("/new_blog")
        elif type_of == "video":
            return redirect("/new_video")
        elif type_of == "book":
            return redirect("/new_book")
        else:
            return render_template("new_choose_type.html")

@app.route("/new_article", methods=["GET", "POST"])
def new_article():
    if (user.isLoggedIn() == False):
        return redirect("/")
        
    if request.method == "GET":
        return render_template("new_article.html")
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        resource_id_type = request.form["resource_id_type"]
        resource_id = request.form["resource_id"]
        tag = request.form["tag"]
        tag = [t.strip() for t in tag.split(";")]
        print(tag)
        if resource_id_type == "doi":
            doi = resource_id
            url = ""
        else:
            doi = ""
            url = resource_id

        if articles.add_new_article(title, author, doi, url, user.get_id(), tag):
            return redirect("/")
        else: # error-sivu (?) lisättävä myöhemmin
            return redirect("/new_article")

@app.route("/new_blog", methods=["GET", "POST"])
def new_blog():
    if (user.isLoggedIn() == False):
        return redirect("/")
        
    if request.method == "GET":
        return render_template("new_blog.html")
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        url = request.form["url"]
        tag = request.form["tag"]
        tag = [t.strip() for t in tag.split(";")]
        if blogs.add_new_blog(title, author, url, user.get_id(), tag):
            return redirect("/")
        else:
            return redirect("/new_blog")

@app.route("/new_video", methods=["GET", "POST"])
def new_video():
    if (user.isLoggedIn() == False):
        return redirect("/")
        
    if request.method == "GET":
        return render_template("new_video.html")
    if request.method == "POST":
        title = request.form["title"]
        channel = request.form["channel"]
        url = request.form["url"]
        tag = request.form["tag"]
        tag = [t.strip() for t in tag.split(";")]
        if videos.add_new_video(title, channel, url, user.get_id(), tag):
            return redirect("/")
        else:
            return redirect("/new_video")

@app.route("/new_book", methods=["GET", "POST"])
def new_book():
    if (user.isLoggedIn() == False):
        return redirect("/")
        
    if request.method == "GET":
        return render_template("new_book.html")
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        isbn = request.form["isbn"]
        tag = request.form["tag"]
        tag = [t.strip() for t in tag.split(";")]
        if books.add_new_book(title, author, isbn, user.get_id(), tag):
            return redirect("/")
        else:
            return redirect("/new_book")

@app.route("/register", methods=["GET", "POST"])
def register():
    if (user.isLoggedIn()):
        return redirect("/")
        
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.register(username, password):
            if user.login(username, password):
                return redirect("/")
        else:
            return render_template("/register.html", message="Rekisteröinti ei onnistunut")

@app.route("/login", methods=["GET", "POST"])
def login():
    if (user.isLoggedIn()):
        return redirect("/")
        
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.login(username, password):
            return redirect("/")
        else:
            return render_template("/login.html", message="Kirjautuminen ei onnistunut")

@app.route("/logout")
def logout():
    user.logout()
    return redirect("/")

@app.route("/hide_item", methods=["GET", "POST"])
def hide_item():
    if (user.isLoggedIn() == False):
        return redirect("/")
        
    if request.method == "GET":
        return redirect("/browse")
    if request.method == "POST":
        item_type = request.form["item_type"]
        item_id = request.form["item_id"]
        if item_type == "blog":
            blogs.hide(item_id)
        elif item_type == "article":
            articles.hide(item_id)
        elif item_type == "video":
            videos.hide(item_id)
        elif item_type == "book":
            books.hide(item_id)
    return redirect("/browse")
