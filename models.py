from flask import Flask
from sqlalchemy import *

class People():
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)
    homeworld = Column(String)
    films = Column(String)
    species = Column(String)
    vehicles = Column(String)
    starships = Column(String)
    url = Column(String)

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

    id = Column(Integer, primary_key=True)
    name = Column(String)
    rotation_period = Column(String)
    diameter = Column(String)
    climate = Column(String)
    gravity = Column(String)
    terrain = Column(String)
    surface_water = Column(String)
    population = Column(Integer)
    residents = Column(String)
    films = Column(String)
    url = Column(String)

    def __init__(self, climate, gravity, terrain, population): 
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.population = population

class Species():
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    classification = Column(String)
    designation = Column(String)
    average_height = Column(String)
    skin_colors = Column(String)
    hair_colors = Column(String)
    eye_colors = Column(String)
    average_lifespan = Column(String)
    homeworld = Column(String)
    language = Column(String)
    people = Column(String)
    films = Column(String)
    url = Column(String)

    def __init__(self, classification, average_height, average_lifespan, language):
        self.classification = classification
        self.average_height = average_height
        self.average_lifespan = average_lifespan
        self.language = language