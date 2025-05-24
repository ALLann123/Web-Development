from config import db

class Contact(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(80), unique=False, nullable=False)
    last_name=db.Column(db.String(80), unique=False, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    
    #converts our db fields into json(python dictionary) which is used in an api
    def to_json(self):
        #use camel case fields when using json, the snake case is for python
        return {
            "id":self.id,
            "firstName":self.first_name,
            "lastName":self.last_name,
            "email":self.email,
        }

