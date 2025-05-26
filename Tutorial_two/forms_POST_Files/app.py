#!/usr/bin/python3
from flask import Flask,render_template, request, Response, send_from_directory, jsonify
import pandas as pd # type: ignore
import os
import uuid

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')

        if username=='manchester' and password == 'password':
            return 'success'
        else:
            return "Failure"

#this blovk handles our file uploads
@app.route('/file_upload', methods=["POST"])
def file_upload():
    #lets get the uploaded file
    file=request.files['file']
    if file.content_type=='text/plain':
        #we read a txt file and decode it
        return file.read().decode()
    elif file.content_type=='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type=='application/vnd.ms-excel':
        df=pd.read_excel(file)
        #now we display the file we have read using pandas as its an excel file
        return df.to_html()

#convert the file to a CSV file and return to the user
@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    #get the file
    file=request.files['file']

    #load our file using pandas
    df=pd.read_excel(file)

    response=Response(
        df.to_csv(),  #convert the file to csv
        mimetype='text/csv',
        headers={
            'content-Disposition':'attachment; filename=result.csv'
        }
    )
    return response

@app.route('/convert_csv_two', methods=['POST'])
def convert_csv_two():
    #get the uploaded file
    file=request.files['file']

    #load the file
    df = pd.read_excel(file)

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    filename=f'{uuid.uuid4()}.csv'

    df.to_csv(os.path.join('downloads',filename))  # Fixed: to_csv instead of to.csv

    #now pass the file to allow the user to download it
    return render_template('download.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(
        directory='downloads',
        path=filename,
        as_attachment=True,
        download_name='result.csv'
    )

#using javascript button
@app.route('/handle_post', methods=['POST'])
def handle_post():
    #get the json data
    greeting=request.json['greeting']
    name=request.json['name']

    with open('file.txt', 'w') as f:
        f.write(f'{greeting}, {name}')
    
    return jsonify({'message':'Successfully Written'})


if __name__=="__main__":
    app.run(debug=True)