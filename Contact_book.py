from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.Integer, nullable = False)
    email = db.Column(db.String(80), nullable = False)
    address = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return f"<Contact_Details {self.id}---{self.name}---{self.phone}----{self.email}-----{self.address}>"
    

@app.route('/')
def index():
    return 'Contact deatils'

@app.route('/contacts')
def get_contacts():
    contacts = Contact.query.all()
    output = []
    for contact in contacts:
        contact_data = {"id":contact.id,"name":contact.name,"phone":contact.phone,"email":contact.email,"address":contact.address}
        #contact_data = {"id":request.json['id'],"name":request.json['name'],"phone":request.json['phone'],"email":request.json['email'],"address":request.json["address"]}
        output.append(contact_data)
    return {"Contact_Details":output}

@app.route('/contacts/<id>')
def get_contact(id):
    contact = Contact.query.get(id)
    return {"id":contact.id,"name":contact.name,"phone":contact.phone,"email":contact.email,"address":contact.address}

@app.route('/contacts', methods = ['POST'])
def add_contact():
    contact = Contact(name=request.json['name'],phone=request.json['phone'],email=request.json['email'],address=request.json['address'])
    db.session.add(contact)
    db.session.commit()
    return {"id":contact.id}

@app.route('/contacts/<id>', methods = ['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)
    if contact is None:
        return {"error":"Not Found"}
    db.session.delete(contact)
    db.session.commit()
    return {"message":"yeet!@"}

@app.route('/contacts/<id>', methods = ['PUT'])
def update_contact(id):
    contact = Contact.query.get(id)
    if contact is None:
        return {"error":"Not Found"}
    contact.name = request.json['name']
    contact.phone = request.json['phone']
    contact.email = request.json['email']
    contact.address = request.json['address']
    db.session.commit()
    return {"message":"updated successfully"}

@app.route('/contacts/<id>', methods = ['PATCH'])
def patched_contact(id):
    contact = Contact.query.get(id)
    if contact is None:
        return {"error":"Not Found"}
    if "name" in  request.json:
        contact.name = request.json['name']
    if "phone" in request.json:
        contact.phone = request.json['phone']
    if "email" in request.json:
        contact.email = request.json['email']
    if "address" in request.json:
        contact.address = request.json['address']
    db.session.commit()
    return {"message":"patched successfully"}

@app.route('/contacts/<name>')
def get_by_name_of_contact(name):
    contact = Contact.query.filter_by(name=name).first()
    return {"id":contact.id,"name":contact.name,"phone":contact.phone,"email":contact.email,"address":contact.address}







'''
@app.route('/contacts')
def get_contacts():
    contacts = Contact.query.all()
    out = []
    for contact in contacts:
        contact_data = {"name":contact.name,"phone":contact.phone,"email":contact.email,"address":contact.address}
        out.append(contact_data)
    return {"contact": out}

@app.route('/contacts', methods=['POST'])
def add_contact():
    contact = Contact(name=request.json['name'],)


'''


