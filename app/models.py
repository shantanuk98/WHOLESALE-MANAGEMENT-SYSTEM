from datetime import datetime
from app import db


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140),nullable = False , unique=True)
    qty = db.Column(db.Integer,default=1, nullable = False)
    minqty = db.Column(db.Integer,default=0, nullable = False)
    sp = db.Column(db.Integer , default=0, nullable = False)
    cp = db.Column(db.Integer,default=0, nullable = False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<stock {}>'.format(self.name)

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable = False)
    stock = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String(120), unique=True , nullable = False)
    phonenumber = db.Column(db.String(120), unique=True , nullable = False)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    country = db.Column(db.String(120))

    def __repr__(self):
        return '<Supplier {}>'.format(self.username)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable = False)
    email = db.Column(db.String(120), unique=True , nullable = False)
    phonenumber = db.Column(db.String(120), unique=True , nullable = False)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    country = db.Column(db.String(120))
    outstandingAmount = db.Column(db.Integer,default=0)


    def __repr__(self):
        return '<customer {}>'.format(self.name)

class Payments(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    stock = db.Column(db.String(120),nullable=False)
    customerPhone = db.Column(db.String(120) , nullable = False)
    customerEmail = db.Column(db.String(120) , nullable = False)
    customer = db.Column(db.String(120) , nullable = False)
    value = db.Column(db.Integer,default = 0, nullable = False)
    qty = db.Column(db.Integer , default = 1, nullable = False)
    amt = db.Column(db.Integer,default=0, nullable = False)
    amtpaid = db.Column(db.Integer,default=0, nullable = False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

