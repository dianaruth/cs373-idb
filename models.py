from flask import *
from sqlalchemy import *

# ----
# People
# ----
class People():
    """"People Model"""

    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    birth_year = Column(String)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String)
    eye_color = Column(String)

    
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

# ----
# Planets
# ----
class Planets():
    """Planets Model"""

    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    climate = Column(String)
    gravity = Column(String)
    terrain = Column(String)
    population = Column(Integer)
    
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

# ----
# Species
# ----
class Species():
    """Species Model"""

    __tablename__ = 'species'

    #
    id = Column(Integer, primary_key=True)
    name = Column(String)
    classification = Column(String)
    average_height = Column(String)
    average_lifespan = Column(String)
    language = Column(String)

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