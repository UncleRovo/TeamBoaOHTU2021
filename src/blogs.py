from app import db

def add_new_blog(title, author, url, tag=[]):
    sql = "INSERT INTO blog (title, author, url, tag, created_at) VALUES (:title, :author, :url, :tag, NOW())"
    db.session.execute(sql, {"title":title, "author":author, "url":url, "tag":tag})
    db.session.commit()
    return True

def get_all():
    sql = "SELECT * FROM blog WHERE visible=1"
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles

def hide(item_id):
    sql = "UPDATE blog SET visible = 0 WHERE id=:item_id "
    db.session.execute(sql, {"item_id":item_id})
    db.session.commit()
    return True
