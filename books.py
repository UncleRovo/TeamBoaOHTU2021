from app import db

def add_new_book(title, author, isbn):
    sql = 'INSERT INTO book (title, author, isbn) VALUES (:title, :author, :isbn)'
    db.session.execute(sql, {"title":title, "author":author, "isbn":isbn})
    db.session.commit()
    return True

def get_all():
    sql = 'SELECT * FROM book WHERE visible=1'
    result = db.session.execute(sql)
    books = result.fetchall()
    return books