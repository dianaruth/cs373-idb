import os, json
import app
from models import People, Species, Planets, db

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def create_people():
    people = load_json('../db/people.json')

    for person in people:
        name = person['name']
        gender = person['gender']
        birth_year = person['birth_year']
        height = person['height']
        mass = person['mass']
        hair_color = person['hair_color']
        eye_color = person['eye_color']

        person = People(name, gender, birth_year, height, mass, hair_color, eye_color)

        db.session.add(person)
        db.session.commit()

def create_planets():
    planets = load_json('../db/planets.json')

    for planet in planets:
        name = planet['name']
        climate =  planet['climate']
        gravity = planet['gravity']
        terrain = planet['terrain']
        population = planet['population']

        planet = Planets(name, climate, gravity, terrain, population)

        db.session.add(planet)
        db.session.commit()

def create_species():
    speciess = load_json('../db/species.json')

    for species in speciess:
        name = species['name']
        classification = species['classification']
        average_height = species['average_height']
        average_lifespan = species['average_lifespan']
        language = species['language']

        species = Species(name, classification, average_height, average_lifespan, language)

        db.session.add(species)
        db.session.commit()

def create_all():
    create_people()
    create_planets()
    create_species()

if __name__ == '__main__':
    create_all()