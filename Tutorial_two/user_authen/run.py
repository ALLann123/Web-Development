#!/usr/bin/python3
from app import create_app

#make an instance of the create_app class we have imported
flask_app=create_app()

if __name__=='__main__':
    flask_app.run(debug=True)