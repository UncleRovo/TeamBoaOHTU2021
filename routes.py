from flask import render_template, request, redirect
from app import app
import articles, blogs, user, videos

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/browse")
def browse():
    return render_template("browse.html", blogs=blogs.get_all(),
                                          articles=articles.get_all(),
                                          videos=videos.get_all(),)

@app.route("/new_choose_type", methods=['GET', 'POST'])
def new_choose_type():
    if request.method == "GET":
        return render_template("new_choose_type.html")
    if request.method == "POST":
        type = request.form.get("type")
        if type == "article":
            return redirect("/new_article")
        elif type == "blog":
            return redirect("/new_blog")
        else:
            return render_template("new_choose_type.html")

@app.route("/new_article", methods=['GET', 'POST'])
def new_article():
    if request.method == "GET":
        return render_template("new_article.html")
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        resource_id_type = request.form["resource_id_type"]
        resource_id = request.form["resource_id"]
        if resource_id_type == "doi":
            doi = resource_id
            url = ""
        else:
            doi = ""
            url = resource_id

        if articles.add_new_article(title, author, doi, url):
            return redirect("/")
        else: # error-sivu (?) lisättävä myöhemmin
            return redirect("/new_article")

@app.route("/new_blog", methods=['GET', 'POST'])
def new_blog():
    if request.method == "GET":
        return render_template("new_blog.html")
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        url = request.form["url"]
        if blogs.add_new_blog(title, author, url):
            return redirect("/")
        else:
            return redirect("/new_blog")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.register(username, password):
            return redirect("/")
        else: 
            # At the moment, there is no notification if the username is already taken. 
            # User is just redirected back to the registration page
            return render_template("/register.html")
        
@app.route('/logout')
def logout():
    user.logout()
    return redirect('/')

@app.route('/login', methods=['get','post'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.login(username, password):
            return redirect("/")
        else:
            # Same placeholder as in /register when logging in / registering fails.
            # Needs a notification still
            return render_template("login.html")