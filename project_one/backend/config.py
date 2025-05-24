from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS     #allows us to send requests to our backend. Removes the error

app=Flask(__name__)
#disables the error we may get
CORS(app)

#initialize the db
#stores the db on my local machine
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

#disable tracking of every update on the db
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

#create a database instance with our configurations
db=SQLAlchemy(app)

