import json, logging
from models import *

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def create_people():
    people = load_json('people.json')

    for person in people:
        name = person['name']
        gender = person['gender']
        birth_year = person['birth_year']
        height = person['height']
        mass = person['mass']
        hair_color = person['hair_color']
        eye_color = person['eye_color']
        description = person['description']
        image = person['image']

        person = People(name, gender, birth_year, height, mass, hair_color, eye_color, description, image)

        db.session.add(person)
        db.session.commit()

def create_planets():
    planets = load_json('planets.json')

    for planet in planets:
        name = planet['name']
        climate = planet['climate']
        gravity = planet['gravity']
        terrain = planet['terrain']
        population = planet['population']
        description = planet['description']
        image = planet['image']

        planet = Planets(name, climate, gravity, terrain, population, description, image)

        db.session.add(planet)
        db.session.commit()

def create_species():
    speciess = load_json('species.json')

    for species in speciess:
        name = species['name']
        classification = species['classification']
        average_height = species['average_height']
        average_lifespan = species['average_lifespan']
        language = species['language']
        description = species['description']
        image = species['image']

        species = Species(name, classification, average_height, average_lifespan, language, description, image)

        db.session.add(species)
        db.session.commit()

def populate_tables():
    create_people()
    create_planets()
    create_species()
