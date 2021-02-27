from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user_name:password@IP:5432/db_name"
app.config['SQLALCHEMY_RECORD_QUERIES'] = True


db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'product'
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(30), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    img = db.Column(
        db.String(100), unique=True, nullable=False)
    description = db.Column(
        db.String(255), nullable=False)
    state = db.Column(
        db.String(10), nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now)


    def __init__(self, name, price, img, description, state):
        self.name = name
        self.price = price
        self.img = img
        self.description = description
        self.state = state

class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    update_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now, nullable=False)

    db_user_atc = db.relationship("AddToCar", backref="user")

    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role

class AddToCar(db.Model):
    __tablename__ = 'addtocar'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(5), nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    update_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now, nullable=False)

    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)
    pid = db.Column(db.Integer, db.ForeignKey('product.pid'), nullable=False)

    def __init__(self, uid, pid, quantity, state):
        self.uid = uid
        self.pid = pid
        self.quantity = quantity
        self.state = state


@app.route('/')
def index():
    # Create data
    db.create_all()

    return 'ok'


if __name__ == "__main__":
    app.run()