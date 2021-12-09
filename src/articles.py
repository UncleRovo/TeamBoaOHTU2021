from app import db

def add_new_article(title, author, doi, url, tag=[]):
    sql = "INSERT INTO article (title, author, doi, url, tag, created_at) VALUES (:title, :author, :doi, :url, :tag, NOW())"
    db.session.execute(sql, {"title":title, "author":author, "doi":doi, "url":url, "tag":tag})
    db.session.commit()
    return True

def get_all():
    sql = "SELECT * FROM article WHERE visible=1"
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles

def hide(item_id):
    sql = "UPDATE article SET visible = 0 WHERE id=:item_id"
    db.session.execute(sql, {"item_id":item_id})
    db.session.commit()
    return True
