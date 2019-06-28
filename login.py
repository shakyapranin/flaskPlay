from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mongologinexample'
mongouri = 'mongodb+srv://' + os.getenv('MONGO_USERNAME') + ':' + os.getenv('MONGO_PASSWORD') + '@' + os.getenv('MONGO_CLUSTER_URL')
app.config['MONGO_URI'] = mongouri

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as' + session['username']
    
    return render_template('index.html')

@app.route('/login')
def login():
    return 'logged in'

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)