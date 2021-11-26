#from db import db
from collections import namedtuple

def get_all():
    if True:
        Article = namedtuple("Article", "id title author url")
        google = Article(1, "google", "sä ja mä", "https://www.google.com")
        yle = Article(2, "yle", "yleiset", "https://www.yle.fi")
        
        return [google, yle]
    else:
        query = "SELECT * FROM  article"
        result = db.session.execute(query)
        articles = result.fetchall()
    return articles