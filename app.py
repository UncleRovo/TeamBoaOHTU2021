import getpass
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import re


app = Flask(__name__)


# For testing purposes. getting the username is automated. 
# Eliminates having to write your own username into app.config[...] 
# When .env is supported remove import getpass as well. 

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri == None:
    # Defines address for db and creates db-object that can execute sql-commands
    uri = f"postgresql:///{getpass.getuser()}"
elif uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`

# Defines address for db and creates db-object that can execute sql-commands
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #unittestejä varten (ei tule warning-messagea). Kommentin voi poistaa myöh.
db = SQLAlchemy(app)

import routes
