from app import db

def add_new_blog(title, author, url, owner, tag=[]):
    sql = "INSERT INTO blog (title, author, url, tag, created_at, owner) \
        VALUES (:title, :author, :url, :tag, NOW(), :owner)"
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

def get_by_user(owner):
    sql = "SELECT * FROM blog WHERE visible=1 AND owner=:owner"
    result = db.session.execute(sql, {"owner":owner})
    articles = result.fetchall()
    return articles

def hide(item_id):
    sql = "UPDATE blog SET visible = 0 WHERE id=:item_id "
    db.session.execute(sql, {"item_id":item_id})
    db.session.commit()
    return True

def search(key, owner):
    sql = "SELECT * FROM blog WHERE (visible=1 AND owner=:owner) \
        AND (title ILIKE :key OR author ILIKE :key OR :key_tag = ANY(tag))"
    result = db.session.execute(sql, {"owner":owner, "key":"%" + key + "%", "key_tag":key})
    blogs = result.fetchall()
    return blogs

def update(id, attributes):
    if not attributes:
        return False
    try:
        tag = attributes["tag"]
        tag = [t.strip() for t in tag.split(";")]
        sql = "UPDATE blog SET title=:title, author=:author, url=:url, tag=:tag WHERE id=:id"
        db.session.execute(sql, {"title": attributes["title"],
                                "author": attributes["author"],
                                "url": attributes["url"],
                                "tag": tag,
                                "id": id})
        db.session.commit()
    except:
        return False
    return True
