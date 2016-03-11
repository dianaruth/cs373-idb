# idk if any of this is right, please change
# I just had to put something to get travis to pass

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime
from config import *

db = SQLAlchemy(app)

class Person(db.Model) :
    print("I'm a person!")
    
class Planet(db.Model) :
    print("I'm a planet!")
    
class Species(db.Model) :
    print("I'm a species!")