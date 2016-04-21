# -*- coding: utf-8 -*-
from flask import Flask, render_template, send_file, jsonify, session
# from sqlalchemy_fulltext import FullTextSearch, FullText
import os, time, subprocess
import requests
from flask.ext.script import Manager
from models import *
from create_db import populate_tables
import json
from sqlalchemy import or_

time.sleep(5)

SQLALCHEMY_DATABASE_URI =\
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

@app.route('/search/<path>')
def get_search_results(search_string):
    search_string_list = search_string.split() # split the string to run the or clause... list of user texts
    if len(search_string_list) == 1:
        single_search_string = "%" + search_string + "%"
        single_results = get_single_results(single_search_string)  # get results for all single word search
    and_results = get_or_results(search_string_list)

def get_or_results(search_string_list):
    search_string_list = map(lambda word : "%" + word + "%", search_string_list)
    # search the People table
    or_results = [People.query.filter(or_(People.name.like(word),
                                          People.gender.like(word),
                                          People.birth_year.like(word),
                                          People.height.like(word),
                                          People.mass.like(word),
                                          People.hair_color.like(word),
                                          People.eye_color.like(word))).all() for word in search_string_list]
    # search the Species table
    or_results += [Species.query.filter(or_(Species.name.like(word),
                                            Species.classification.like(word),
                                            Species.average_height.like(word),
                                            Species.average_lifespan.like(word),
                                            Species.language.like(word))).all() for word in search_string_list]
    # search the Planets table
    or_results += [Planets.query.filter(or_(Planets.name.like(word),
                                            Planets.climate.like(word),
                                            Planets.gravity.like(word),
                                            Planets.terrain.like(word),
                                            Planets.population.like(word))).all() for word in search_string_list]
    print("OR RESULTS LIST: ")
    print(or_results)
    return or_results

"""
With the string not yet split, run a like clause on all three tables.
The result will return only rows that match all of the unsplit string.
"""
def get_single_results(search_string):
    # search the People table
    single_result = People.query.filter(or_(People.name.like(search_string),
                                                 People.gender.like(search_string),
                                                 People.birth_year.like(search_string),
                                                 People.height.like(search_string),
                                                 People.mass.like(search_string),
                                                 People.hair_color.like(search_string),
                                                 People.eye_color.like(search_string))).all()
    # search the Species table
    single_result += Species.query.filter(or_(Species.name.like(search_string),
                                                   Species.classification.like(search_string),
                                                   Species.average_height.like(search_string),
                                                   Species.average_lifespan.like(search_string),
                                                   Species.language.like(search_string))).all()
    # search the Planets table
    single_result += Planets.query.filter(or_(Planets.name.like(search_string),
                                                   Planets.climate.like(search_string),
                                                   Planets.gravity.like(search_string),
                                                   Planets.terrain.like(search_string),
                                                   Planets.population.like(search_string))).all()
    print('SINGLE LIST: ')
    print(single_result)
    return(single_result)

@app.route('/get_people')
def get_people_data():
    """
    Returns a list of JSON objects containing every person in the database. Each person has the following attributes:
    -id
    -name
    -description
    -image
    -birth year
    -eye color
    -gender
    -hair color
    -height
    -homeworld
    -mass
    -skin color
    -species
    """

    people = People.query.all()
    json_people = [person.serialize for person in people]

    return jsonify({"people": json_people})

@app.route('/get_planets')
def get_planets_data():
    """
    Returns a list of JSON objects containing every planet in the database. Each planet has the following attributes:
    -id
    -name
    -description
    -image
    -climate
    -gravity
    -population
    -terrain
    """

    planets = Planets.query.all()
    json_planet = [planet.serialize for planet in planets]

    return jsonify({"planets": json_planet})

@app.route('/get_species')
def get_species_data():
    """
    Returns a list of JSON objects containing every species in the database. Each species has the following attributes:
    -id
    -name
    -description
    -image
    -average height
    -average lifespan
    -classification
    -homeworld
    -language
    """

    speciess = Species.query.all()
    json_species = [species.serialize for species in speciess]

    return jsonify({"species": json_species})

@app.route("/get_person/<path>")
def get_person_data(path):
    """
    Returns a JSON object for the person specified by personID.
    """

    person = People.query.get(path)
    json_person = person.serialize

    return jsonify({"person": json_person})

@app.route('/get_planet/<path>')
def get_planet_data(path):
    """
    Returns a JSON object for the planet specified by planetID.
    """

    planet = Planets.query.get(path)
    json_planet = planet.serialize

    return jsonify({"planet": json_planet})

@app.route('/get_s/<path>')
def get_s_data(path):
    """
    Returns a JSON object for the species specified by speciesID.
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


@app.route('/person/<path>/species')
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
    json_species = species.serialize

    try:
        planet = Planets.query.filter_by(name=json_species['homeworld']).first()
        json_planet = planet.serialize

    except:
        json_planet = None

    return jsonify({"native_planet": json_planet})

@app.route('/planet/<path>/people')
def get_people_from_planet(path):

    planet = Planets.query.get(path)
    people = People.query.filter_by(homeworld = planet.name)

    try:
        json_people = [person.serialize for person in people]
    except:
        json_people = None

    return jsonify({"residents": json_people})

@app.route('/planet/<path>/species')
def get_species_from_planet(path):

    planet = Planets.query.get(path)
    species = Species.query.filter_by(homeworld = planet.name).first()

    try:
        json_species = species.serialize
    except:
        json_species = None

    return jsonify({"native_species": json_species})

@app.route('/species/<path>/people')
def get_people_from_species(path):

    species = Species.query.get(path)
    people = People.query.filter_by(species = species.name)

    try:
        json_people = [person.serialize for person in people]
    except:
        json_people = None

    return jsonify({"people":json_people})

@app.route('/person/<path>/species')
def get_species_from_person(path):

    person = People.query.get(path)
    json_species = Species.query.filter_by(name = person.species)

    try:
        json_species.serialize
    except:
        json_species = None

    return jsonify({"species":json_species})


@app.route('/run_tests')
def run_tests():
    output = subprocess.getoutput("python tests_web.py")
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

@app.route("/results")
def render_results():
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
    # app.config['SQLALCHEMY_ECHO'] = True
    # db.create_all()
    # populate_tables()


@manager.command
def create_db():
    app.config['SQLALCHEMY_ECHO'] = True
    db.create_all()
    populate_tables()

@manager.command
def drop_db():
    app.config['SQLALCHEMY_ECHO'] = True
    db.session.remove()
    db.drop_all()

if __name__ == "__main__":
    manager.run()