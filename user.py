from app import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session

def login(username, password):
	print("username, password", username, password)
	sql = 'SELECT id, username, password FROM users WHERE username=:username'
	result = db.session.execute(sql, {'username':username})
	user = result.fetchone()
	if user != None:
		print('käyttäjä ei ollut none')
		print('salasana', user[2])
		if check_password_hash(user[2], password):
			session['username'] = user[1]
			session['user_id'] = user[0]
			print('salasanat matsasivat')
			print('session', session)
			return True
	return False

def register(username, password):
	try:
		hash_value = generate_password_hash(password)
		sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
		db.session.execute(sql, {"username":username, "password":hash_value})
		db.session.commit()
		return login(username, password)
	except:
		return False

def logout():
	session.clear()
	return True