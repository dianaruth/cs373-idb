from flask import Flask
from app import db
from sqlalchemy import orm, ForeignKey

class People():
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String)
    skin_color = db.Column(db.String)
    eye_color = db.Column(db.String)
    birth_year = db.Column(db.String)
    gender = db.Column(db.String)
    homeworld = db.Column(db.String)
    films = db.Column(db.String)
    species = db.Column(db.String)
    vehicles = db.Column(db.String)
    starships = db.Column(db.String)
    url = db.Column(db.String)

    def __init__(self, name, gender, birth_year, height, mass, hair_color, eye_color):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.eye_color = eye_color


class Planets():
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    rotation_period = db.Column(db.String)
    diameter = db.Column(db.String)
    climate = db.Column(db.String)
    gravity = db.Column(db.String)
    terrain = db.Column(db.String)
    surface_water = db.Column(db.String)
    population = db.Column(db.Integer)
    residents = db.Column(db.String)
    films = db.Column(db.String)
    url = db.Column(db.String)

    def __init__(self, climate, gravity, terrain, population): 
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.population = population

class Species():
    __tablename__ = 'species'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    classification = db.Column(db.String)
    designation = db.Column(db.String)
    average_height = db.Column(db.String)
    skin_colors = db.Column(db.String)
    hair_colors = db.Column(db.String)
    eye_colors = db.Column(db.String)
    average_lifespan = db.Column(db.String)
    homeworld = db.Column(db.String)
    language = db.Column(db.String)
    people = db.Column(db.String)
    films = db.Column(db.String)
    url = db.Column(db.String)

    def __init__(self, classification, average_height, average_lifespan, language):
        self.classification = classification
        self.average_height = average_height
        self.average_lifespan = average_lifespan
        self.language = language