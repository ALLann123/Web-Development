#!/usr/bin/python3
from flask import render_template, request
from models import Person


def register_routes(app, db):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method=='GET':
            people=Person.query.all()
            return render_template(template_name_or_list='index.html', people=people)
        elif request.method=="POST":
            name=request.form.get('name')
            age=request.form.get('age')
            job=request.form.get('job')

            #create an object
            person=Person(name=name, age=age, job=job)

            #add the new object to the database
            db.session.add(person)
            db.session.commit()

            people=Person.query.all()
            return render_template(template_name_or_list='index.html', people=people)

    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        Person.query.filter(Person.pid==pid).delete()

        db.session.commit()

        people=Person.query.all()
        return render_template(template_name_or_list='index.html', people=people)

    @app.route('/detail/<pid>')
    def detail(pid):
        person=Person.query.filter(Person.pid==pid).first()
        return render_template(template_name_or_list='detail.html', person=person)