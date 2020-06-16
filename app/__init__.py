from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
import json
import datetime
from bson.objectid import ObjectId
import os


class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

# create the flask object




app = Flask(__name__)
CORS(app)


# add mongo url to flask config, so that flask_pymongo can use it to make connection
# app.config['MONGO_URI'] = os.environ.get('mongodb://localhost:27017/')
app.config["MONGO_URI"] = "mongodb://localhost:27017/flaskrest"
mongo = PyMongo(app)

app.json_encoder = JSONEncoder


# Configurations
app.config.from_object('config')