import os, datetime
import re
from flask import Flask, request, render_template, redirect, abort, flash, json, jsonify

from unidecode import unidecode

# mongoengine database module
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)   # create our flask app
app.config['CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
#app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# --------- Database Connection ---------
# MongoDB connection to MongoLab's database
app.config['MONGODB_SETTINGS'] = {'HOST':os.environ.get('MONGOLAB_URI'),'DB': 'dwdfall2013'}
app.logger.debug("Connecting to MongoLabs")
db = MongoEngine(app) # connect MongoEngine with Flask App

# import data models
import models