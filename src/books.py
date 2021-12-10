from app import db

def add_new_book(title, author, isbn, owner, tag=[]):
    sql = "INSERT INTO book (title, author, isbn, tag, created_at, owner) VALUES (:title, :author, :isbn, :tag, NOW(), :owner)"
    db.session.execute(sql, {"title":title, "author":author, "isbn":isbn, "tag":tag, "owner":owner})
    db.session.commit()
    return True

def get_all():
    sql = "SELECT * FROM book WHERE visible=1"
    result = db.session.execute(sql)
    books = result.fetchall()
    return books
    
def get_by_user(owner):
    sql = "SELECT * FROM book WHERE visible=1 AND owner=:owner"
    result = db.session.execute(sql, {"owner":owner})
    articles = result.fetchall()
    return articles

def get_one(id):
    sql = "SELECT * FROM book WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    book = result.fetchone()
    return book

def hide(item_id):
    sql = "UPDATE book SET visible = 0 WHERE id=:item_id "
    db.session.execute(sql, {"item_id":item_id})
    db.session.commit()
    return True

def update(id, attributes):
    if not attributes:
        return False
    try:
        tag = attributes["tag"]
        tag = [t.strip() for t in tag.split(";")]
        sql = "UPDATE book SET title=:title, author=:author, isbn=:isbn, tag=:tag WHERE id=:id"
        db.session.execute(sql, {"title": attributes["title"],
                                "author": attributes["author"],
                                "isbn": attributes["isbn"],
                                "tag": tag,
                                "id": id})
        db.session.commit()
    except:
        return False
    return True
