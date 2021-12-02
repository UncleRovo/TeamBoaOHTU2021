from app import db

def add_new_video(title, channel, url):
    sql = 'INSERT INTO video (title, channel, url) VALUES (:title, :channel, :url)'
    db.session.execute(sql, {"title":title, "channel":channel, "url":url})
    db.session.commit()
    return True

def get_all():
    sql = 'SELECT * FROM video WHERE visible=1'
    result = db.session.execute(sql)
    videos = result.fetchall()
    return videos
