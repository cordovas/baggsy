# mongoengine database module
from mongoengine import *
from flask.ext.mongoengine.wtf import model_form, 

from datetime import datetime
import logging

class Idea(Document):

	
	creator = mongoengine.StringField(max_length=120, required=True, verbose_name="First name")
	title = mongoengine.StringField(max_length=120, required=True)
	slug = mongoengine.StringField()
	idea = mongoengine.StringField(required=True, verbose_name="What is your idea?")
	latitude = mongoengine.StringField(max_length=120, required=True)
	longitude = mongoengine.StringField(max_length=120, required=True)