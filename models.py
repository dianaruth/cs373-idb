import sys
from sqlalchemy import *
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from app import db

# ----\
# People
# ----
class People(db.Model):
    """"People Model"""

    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    name = db.Column(db.String(256))
    gender = db.Column(db.String(256))
    birth_year = db.Column(db.String(256))
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(256))
    eye_color = db.Column(db.String(256))

    def __init__(self, name, gender, birth_year, height, mass, hair_color, eye_color):
        """
        Assigns variables to the class upon initialization.

        Parameters
        ----------
        self : Planets
        name : Column(String)
        gender : Column(String)
        birth_year : Column(String)
        height: Column(Integer)
        mass : Column(Integer)
        hair_color : Column(String)
        eye_color : Column(String)

        Returns
        -------
        People
        """
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.eye_color = eye_color

    @property
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "gender" : self.gender,
            "birth year" : self.birth_year,
            "height" : self.height,
            "mass" : self.mass,
            "hair color" : self.hair_color,
            "eye color" : self.eye_color
        }

# ----
# Planets
# ----
class Planets(db.Model):
    """Planets Model"""

    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    name = db.Column(db.String(256))
    climate = db.Column(db.String(256))
    gravity = db.Column(db.String(256))
    terrain = db.Column(db.String(256))
    population = db.Column(db.Integer)
    
    def __init__(self, name, climate, gravity, terrain, population): 
        """
        Assigns variables to the class upon initialization.

        Parameters
        ----------
        self : Planets
        name : Column(String)
        climate : Column(String)
        gravity : Column(String)
        terrain : Column(String)
        population : Column(Integer)

        Returns
        -------
        Planets
        """
        self.name = name
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.population = population

    @property
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "climate" : self.climate,
            "gravity" : self.gravity,
            "terrain" : self.terrain,
            "population" : self.population
        }


# ----
# Species
# ----
class Species(db.Model):
    """Species Model"""

    __tablename__ = 'species'

    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    name = db.Column(db.String)
    classification = db.Column(db.String(256))
    average_height = db.Column(db.String(256))
    average_lifespan = db.Column(db.String(256))
    language = db.Column(db.String(256))

    def __init__(self, name, classification, average_height, average_lifespan, language):
        """
        Assigns variables to the class upon initialization.
        
        Parameters
        ----------
        self : Planets
        name : Column(String)
        classification : Column(String)
        average_height : Column(String)
        average_lifespan : Column(String)
        language : Column(String)
        
        Returns
        -------
        People
        """
        self.name = name
        self.classification = classification
        self.average_height = average_height
        self.average_lifespan = average_lifespan
        self.language = language


    @property
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "classification" : self.classification,
            "average height" : self.average_height,
            "average lifespan" : self.average_lifespan,
            "language" : self.language
        }