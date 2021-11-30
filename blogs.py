from app import db

def add_new_blog(title, author, url):
    sql = 'INSERT INTO blog (title, author, url) VALUES (:title, :author, :url)'
    db.session.execute(sql, {"title":title, "author":author, "url":url})
    db.session.commit()
    return True

def get_all():
    sql = 'SELECT * FROM blog WHERE visible=1'
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles
