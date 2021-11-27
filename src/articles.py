from app import db
from collections import namedtuple

def get_all():
    sql = 'SELECT * FROM articles'
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles

    