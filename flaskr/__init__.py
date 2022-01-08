from flask import Flask
from pymongo import MongoClient 
from flaskr.inventory_manager import Manager
import os

client = MongoClient('mongodb://localhost:27017/',connect=False)
db = client['AURA']

app = Flask(__name__, static_url_path='/static') #instance of a Flask class, uses __name__ since we're using a single module

app.config['TEMPLATES_AUTO_RELOAD'] = True #Helps with debug of frontend
app.config['SECRET_KEY'] = os.urandom(20).hex() #secret for the app, used for authentication of sessions

manager = Manager(db) #inventory management object

from flaskr import routes
