from flask import Flask, session
from datetime import timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)


# 设置session
@app.route('/')
def index():
    session['username'] = 'name'
    session.permanent = True
    session.get('username')
    session['username'] = False