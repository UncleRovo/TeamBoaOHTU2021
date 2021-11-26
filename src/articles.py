from app import db
from collections import namedtuple

def get_all():
    sql = 'SELECT * FROM article'
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles

    