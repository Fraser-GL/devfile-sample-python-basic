from flask import Flask
import os
import pymongo 
import logging

app = Flask(__name__)

@app.route('/')
def hello():
    CONNECTION_STRING = "mongodb.fraser-brown-dev.svc.cluster.local"
    client = pymongo.MongoClient(CONNECTION_STRING)
 
    db = client.testTable
    # client.authenticate()
    # people = db.people
    # personDocument = {
    #     "name": { "first": "Alan", "last": "Turing" },
    #     "contribs": [ "Turing machine", "Turing test", "Turingery" ],
    #     "views": 1250000
    # } 
    # people.insert_one(personDocument)
    
    return "Hello World! I have updated this code to use a database" + os.environ.get('DB_USER')

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')


