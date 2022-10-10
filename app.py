import re
from flask import Flask, request
import os
import pymongo 
import logging
import json

# Debugging :
# Make sure that both instances have pods running
# Check you arent connected via https

app = Flask(__name__)

def connect():
    CONNECTION_STRING = "mongodb.fraser-brown-dev.svc.cluster.local"
    client = pymongo.MongoClient(CONNECTION_STRING,
                                username= os.environ.get('DB_USER'),
                                password=  os.environ.get('DB_PASS'),
                                authSource=  os.environ.get('DB_NAME'),
                                authMechanism='SCRAM-SHA-1')
 
    return client.sampledb

@app.route('/')
def hello():
    return "Hello World! use the user page to look up details"


@app.route('/add/<username>')
def profile(username):
    db = connect();
    people = db.people
    personDocument = {
        "name": { "first": "Alan", "last": username},
        "contribs": [ "Turing machine", "Turing test", "Turingery" ],
        "views": 1250000
    } 
    people.insert_one(personDocument)
    return f'{username}\'s profile has been created'

@app.route('/user/<username>')
def lookup(username):
    db = connect();
    people = db.people
    turing = people.find_one({ "name.last": username })
    return str(turing)

@app.post('/add')
def postApi():
    db = connect();
    people = db.people
    personDocument = request.form
    
    people.insert_one(personDocument)
    
    return str(request.form['hello'])

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')


