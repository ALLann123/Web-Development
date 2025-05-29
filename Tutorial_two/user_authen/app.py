#!/usr/bin/python3
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from models import User
from db import db

def create_app():
    app=Flask(__name__, template_folder='templates')

    #lets create a db
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///./testdb.db'

    #in authentication we need to get our session
    app.secret_key='SOME KEY'
    #initialize app
    db.init_app(app)

    #lets create the login manager
    login_manager=LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    #lets get the  user id
    def load_user(uid):
        return User.query.get(uid)
    
    @login_manager.unauthorized_handler
    def unauthorize_callback():
        return redirect(url_for('login'))
    bcrypt=Bcrypt(app)

    #imports later on
    from routes import register_routes
    register_routes(app, db, bcrypt)


    migrat=Migrate(app, db)
    return app



