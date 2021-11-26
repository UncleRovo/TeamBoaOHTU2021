from app import db
from collections import namedtuple

def get_all():
    # Laitoin funktion palauttamaan normaalin kyselyn tuloksen väliaikaisratkaisun sijaan :) -t. Juhana
    sql = 'SELECT * FROM articles'
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles
    
    # if True:
        

    #     Article = namedtuple("Article", "id title author url")
    #     google = Article(1, "google", "sä ja mä", "https://www.google.com")
    #     yle = Article(2, "yle", "yleiset", "https://www.yle.fi")
        
    #     return [google, yle]
    # else:

    