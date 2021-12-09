from app import db

def add_new_video(title, channel, url, owner, tag=[]):
    sql = "INSERT INTO video (title, channel, url, tag, created_at, owner) VALUES (:title, :channel, :url, :tag, NOW(), :owner)"
    db.session.execute(sql, {"title":title, "channel":channel, "url":url, "tag":tag, "owner":owner})
    db.session.commit()
    return True

def get_all():
    sql = "SELECT * FROM video WHERE visible=1"
    result = db.session.execute(sql)
    videos = result.fetchall()
    return videos
    
def get_by_user(owner):
    sql = "SELECT * FROM video WHERE visible=1 AND owner = :owner"
    result = db.session.execute(sql, {"owner":owner})
    articles = result.fetchall()
    return articles

def hide(item_id):
    sql = "UPDATE video SET visible = 0 WHERE id=:item_id "
    db.session.execute(sql, {"item_id":item_id})
    db.session.commit()
    return True
