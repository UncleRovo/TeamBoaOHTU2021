from app import db
from collections import namedtuple

class Articles:

    def __init__(self):
        self.articles = None
        
    def add_new_article(article_title, article_author, article_url):
        sql = 'INSERT INTO articles (title, author, url) VALUES (:title, :author, :url)'
        db.session.execute(sql, {"title":article_title, "author":article_author, "url":article_url})
        db.session.commit()
        return True

    def get_all():
        sql = 'SELECT * FROM articles'
        result = db.session.execute(sql)
        articles = result.fetchall()
        return articles
