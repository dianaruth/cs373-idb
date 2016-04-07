# -*- coding: utf-8 -*-
from flask import Flask, render_template, send_file, jsonify
import os, time, subprocess
import requests
from flask.ext.script import Manager
from models import *
from create_db import populate_tables
import json

time.sleep(5)

SQLALCHEMY_DATABASE_URI = \
    '{engine}://{username}:{password}@{hostname}/{database}'.format(
        engine='mysql+pymysql',
        username=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        hostname=os.getenv('MYSQL_HOST'),
        database=os.getenv('MYSQL_DATABASE'))

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)

@app.route('/get_people')
def get_people_data():
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the following three (currently hardcoded) people:
        - Luke Skywalker
        - C-3P0
        - R2-D2
    Gets information about each person from the API and returns a JSON object
    """
    
    people = People.query.all()
    json_people = [person.serialize for person in people]

    return jsonify({"people": json_people})

@app.route('/get_planets')
def get_planets_data():
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the following three (currently hardcoded) planets:
        - Tatooine
        - Alderaan
        - Yavin IV
    Gets information about each planet from the API and returns a JSON object
    """
    
    planets = Planets.query.all()
    json_planet = [planet.serialize for planet in planets]

    return jsonify({"planets": json_planet})

@app.route('/get_species')
def get_species_data():
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the following three (currently hardcoded) species:
        - Human
        - Droid
        - Wookiee
    Gets information about each species from the API and returns a JSON object
    """
    
    speciess = Species.query.all()
    json_species = [species.serialize for species in speciess]

    return jsonify({"species": json_species})
    
@app.route("/get_person/<path>")
def get_person_data(path):
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the person with id "path"
    Returns data about the person in the form of a JSON object
    """
    
    person = People.query.get(path)
    json_person = person.serialize

    return jsonify({"person": json_person})

@app.route('/get_planet/<path>')
def get_planet_data(path):
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the planet with id "path"
    Returns data about the planet in the form of a JSON object
    """
    
    planet = Planets.query.get(path)
    json_planet = planet.serialize

    return jsonify({"planet": json_planet})

@app.route('/get_s/<path>')
def get_s_data(path):
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the species with id "path"
    Returns data about the species in the form of a JSON object
    """
    
    species = Species.query.get(path)
    json_species = species.serialize

    return jsonify({"species": json_species})


@app.route('/person/<path>/planet')
def get_planet_for_person(path):
    """
    Given a person id (denoted by "path"), return a JSON object for that person's home planet
    """

    person = People.query.get(path)
    json_person = person.serialize

    try:
        homeworld = Planets.query.filter_by(name=json_person['homeworld']).first()
        json_homeworld = homeworld.serialize

    except:
        json_homeworld = None

    return jsonify({"homeworld": json_homeworld})


@app.route('/species/<path>/people')
def get_species_for_person(path):
    """
    Given species ID (path) return all people where speciesID == path
    """
    person = People.query.get(path)
    json_person = person.serialize

    try:
        species = Species.query.filter_by(name=json_person['species']).first()
        json_species = species.serialize

    except:
        json_species = None

    return jsonify({"species": json_species})


@app.route('/species/<path>/planet')
def get_planet_for_species(path):
    """
    Given species ID (path) return homeworld
    """

    species = Species.query.get(path)
    # json_species = species.serialize

    try:
        planet = Planets.query.filter_by(name=json_species['homeworld']).first()
        json_planet = planet.serialize

    except:
        json_planet = None

    return jsonify({"planet": json_planet})

@app.route('/planet/<path>/people')
def get_people_from_planet(path):

    planet = Planets.query.get(path)
    people = People.query.filter_by(homeworld = planet.name)

    try:
        json_people = [person.serialize for person in people]
    except:
        json_people = None

    return jsonify({"planet": json_people})

@app.route('/planet/<path>/species')
def get_species_from_planet(path):

    planet = Planets.query.get(path)
    species = Species.query.filter_by(homeworld = planet.name).first()

    try:
        json_species = species.serialize
    except:
        json_species = None

    return jsonify({"species": json_species})

@app.route('/species/<path>/people')
def get_people_from_species(path):

    species = Species.query.get(path)
    people = People.query.filter_by(species = species.name)

    try:
        json_people = [person.serialize for person in people]
    except:
        json_people = None

    return jsonify({"people":json_people})

@app.route('person/<path>/species')
def get_speciecs_from_person(path):
    
    person = People.query.get(path)
    species = Species.query.filter_by(name = person.species)

    try:
        json_species.serialize
    except:
        json_species = None

    return jsonify({"species":json_species})


@app.route('/run_tests')
def run_tests():
    output = subprocess.getoutput("python tests.py")
    return json.dumps({'output': str(output)})

@app.route("/people")
def render_people():
    return render_template('index.html')

@app.route("/planets")
def render_planets():
    return render_template('index.html')

@app.route("/species")
def render_species():
    return render_template('index.html')

@app.route("/about")
def render_about():
    return render_template('index.html')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

@app.route('/')
def home():
    return send_file('templates/index.html')

db.init_app(app)

# with app.app_context():
#     app.config['SQLALCHEMY_ECHO'] = True
#     db.create_all()
#     populate_tables()

@manager.command
def create_db():
    app.config['SQLALCHEMY_ECHO'] = True
    db.create_all()

@manager.command
def create_data():
    app.config['SQLALCHEMY_ECHO'] = True
    populate_tables()

@manager.command
def drop_db():
    app.config['SQLALCHEMY_ECHO'] = True
    db.session.remove()
    db.drop_all()

if __name__ == "__main__":
    manager.run()