#!/usr/bin/python3
from flask import Flask, request, make_response

#create a flask object
app=Flask(__name__)

#set the route to home page and print the string
@app.route("/")
def index():
    return "<h1>Hello World</>"

#lets add another route
@app.route("/hello")
def hello():
    response=make_response("Hello World")
    response.status_code=202
    response.headers['content-type']='text/plain'
    return response

#this below is a url processor, inthe example we add name as a variable that will be passed to our function
@app.route('/greet/<name>')
def greet(name):
    return f"<h2>Hello {name}</h2>"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'{number1}+{number2}= {number1+number2}'

@app.route('/handle_url_params')
def handlee_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting=request.args['greeting']
        name=request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return "Some parameters are missing"


if __name__ =="__main__":
    app.run(debug=True)

