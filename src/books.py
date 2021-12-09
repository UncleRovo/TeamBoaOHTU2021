from app import db

def add_new_book(title, author, isbn, tag=[]):
    sql = "INSERT INTO book (title, author, isbn, tag, created_at) VALUES (:title, :author, :isbn, :tag, NOW())"
    db.session.execute(sql, {"title":title, "author":author, "isbn":isbn, "tag":tag})
    db.session.commit()
    return True

def get_all():
    sql = "SELECT * FROM book WHERE visible=1"
    result = db.session.execute(sql)
    books = result.fetchall()
    return books

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
