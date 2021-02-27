from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user_name:password@IP:5432/db_name"
app.config['SQLALCHEMY_RECORD_QUERIES'] = True


db = SQLAlchemy(app)

relations = db.Table(
    'relations',
    db.Column('tagid_rt', db.Integer, db.ForeignKey('tag_mul_to_mul.tagid')),
    db.Column('pid_rt', db.Integer, db.ForeignKey('product_mul_to_mul.pid')))


class Product(db.Model):
    __tablename__ = 'product_mul_to_mul'
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

    db_product_tag_rel = db.relationship(
        "Tag", secondary=relations, backref="product")

    def __init__(self, name, price, img, description, state):
        self.name = name
        self.price = price
        self.img = img
        self.description = description
        self.state = state


class Tag(db.Model):
    __tablename__ = 'tag_mul_to_mul'
    tagid = db.Column(db.Integer, primary_key=True)
    tag_type = db.Column(db.String(30))
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now)

    def __init__(self, tag_type):
        self.tag_type = tag_type


@app.route('/')
def index():
    # Create data
    db.create_all()

    return 'ok'


if __name__ == "__main__":
    app.run()