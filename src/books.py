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

def hide(item_id):
    sql = "UPDATE book SET visible = 0 WHERE id=:item_id "
    db.session.execute(sql, {"item_id":item_id})
    db.session.commit()
    return True
