from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Defines address for db and creates db-object that can execute sql-commands
# Change the {user} to your username
# For more info: https://hy-tsoha.github.io/materiaali/osa-2/#postgresql-tulkki
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///user"
db = SQLAlchemy(app)


import routes