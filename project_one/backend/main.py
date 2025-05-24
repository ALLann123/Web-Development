from flask import request, jsonify
from config import app, db
from models import Contact

#lets write the get method
@app.route("/contacts", methods=["GET"])
def get_contacts():
    #handles the get request sent
    contacts=Contact.query.all()    #uses sqlalchemy to list all contacts
    #the returned objects should be in json
    json_contacts=list(map(lambda x:x.to_json(), contacts))

    return jsonify({"contacts":json_contacts})


#this handles our request that we got
#handles creating the contacts
@app.route("/create_contact", methods=["POST"])
def create_contact():
    #lets look for the values from the json response
    first_name=request.json.get("firstName")
    last_name=request.json.get("lastName")
    email=request.json.get("email")

    #check if values exist
    if not first_name or not last_name or not email:
        #return this error message
        return (
            jsonify({"message":" You must include a first name, last name and email"}), 
            400, 
        )
    
    #lets add information to database. Adding entry to the database
    new_contact=Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        #write tothe database
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    #display it worked
    return jsonify({"message":"User created!"}), 201

#we want to update information by id
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    #look db and find user with the ID
    contact=Contact.query.get(user_id)

    #if we did not find the json dat
    if not contact:
        return jsonify({"message":"User not found"}), 404
    
    #if contact is found pass in the json data
    data=request.json
    contact.first_name=data.get("firstName", contact.first_name)
    contact.last_name=data.get("lastName", contact.last_name)
    contact.email=data.get("email", contact.email)

    db.session.commit()
    return jsonify({"message":"User Updated."}), 200

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    #look db and find user with the ID
    contact=Contact.query.get(user_id)

    #if we did not find the json dat
    if not contact:
        return jsonify({"message":"User not found"}), 404

    #delete the contact
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message":"User deleted"}), 200


if __name__ =="__main__":
    #this creates our database as soon as we run our program. Creates if not created
    with app.app_context():
        db.create_all()

    app.run(debug=True)

