import getpass
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# For testing purposes. getting the username is automated. 
# Eliminates having to write your own username into app.config[...] 
# When .env is supported remove import getpass as well. 

# Defines address for db and creates db-object that can execute sql-commands
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{getpass.getuser()}"
db = SQLAlchemy(app)


import routes