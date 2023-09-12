from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)

app.secret_key = 'secretkey'

# SETTING UP THE MONGODB DATABASE
app.config['MONGO_URI'] = "mongodb://localhost:27017/flaskCRUD"

# FOR MONGO ATLAS THE BELOW URI
# app.config['MONGO_URI'] = "mongodb+srv://<USERNAME>:<password>@cluster0.dqidshh.mongodb.net/<YOUR DATABASE>?retryWrites=true&w=majority"


mongo = PyMongo(app)

from application import routes