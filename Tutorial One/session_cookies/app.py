#!/usr/bin/python3
from flask import Flask, render_template,session, make_response, request, flash

app=Flask(__name__, template_folder='templates')
#create a secret key we can use on the serve side
app.secret_key='SOME KEY'

@app.route('/')
def index():
    return render_template('index.html', message='Session Data Set.')

#we are setting the session data
@app.route('/set_data')
def set_data():
    session['name']='Allan'
    session['other']='Hello World'

    return render_template('index.html')


#used to display the session data
@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name=session['name']
        other=session['other']
        return render_template(template_name_or_list='index.html', message=f'Name: {name}, Other: {other}')
    else:
        return render_template(template_name_or_list='index.html', message=f'No session found.')

#this clears the session data
@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template(template_name_or_list='index.html', message=f'Session Cleared')


#----Cookies
@app.route('/set_cookie')
def set_cookie():
    #this instructs the browser to set the cookie
    response=make_response(render_template(template_name_or_list='index.html', messages='Cookie Set'))
    response.set_cookie(key='cookie_name', value='cookie_value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value=request.cookies['cookie_name']
    return render_template('index.html', message=f'Cookie Value={cookie_value}')

@app.route('/remove_cookie')
def remove_cookie():
    #this instructs the browser to set the cookie
    response=make_response(render_template(template_name_or_list='index.html', messages='Cookie removed'))
    response.set_cookie(key='cookie_name', expires=0)
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')

        if username=='allan' and password == '12345':
            flash('Successful Login')
            return render_template(template_name_or_list='index.html', messae='')
        else:
            flash('Login Failed!')
            return render_template(template_name_or_list='index.html', messages='')


if __name__=='__main__':
    app.run(debug=True)