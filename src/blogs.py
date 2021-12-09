from app import db

def add_new_blog(title, author, url, owner, tag=[]):
    sql = "INSERT INTO blog (title, author, url, tag, created_at, owner) VALUES (:title, :author, :url, :tag, NOW(), :owner)"
    db.session.execute(sql, {"title":title, "author":author, "url":url, "tag":tag, "owner":owner})
    db.session.commit()
    return True

def get_all():
    sql = "SELECT * FROM blog WHERE visible=1"
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles

def get_one(id):
    sql = "SELECT * FROM blog WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    blog = result.fetchone()
    return blog

def hide(item_id):
    sql = "UPDATE blog SET visible = 0 WHERE id=:item_id "
    db.session.execute(sql, {"item_id":item_id})
    db.session.commit()
    return True
