#!/usr/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

db=SQLAlchemy()

def create_app():
    app=Flask(__name__, template_folder='templates')

    #lets create a db
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///./testdb.db'

    #initialize app
    db.init_app(app)

    #imports later on
    from routes import register_routes
    register_routes(app, db)


    migrat=Migrate(app, db)
    return app



