from app import db

def add_new_article(title, author, doi, url):
    sql = 'INSERT INTO article (title, author, doi, url) VALUES (:title, :author, :doi, :url)'
    db.session.execute(sql, {"title":title, "author":author, "doi":doi, "url":url})
    db.session.commit()
    return True

def get_all():
    sql = 'SELECT * FROM article WHERE visible=1'
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles
