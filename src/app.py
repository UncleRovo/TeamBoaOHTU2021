from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Defines address for db and creates db-object that can execute sql-commands
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///juhanaka"
db = SQLAlchemy(app)


import routes