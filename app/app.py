from flask import Flask, render_template, send_file, jsonify
import requests

app = Flask(__name__, static_url_path='')

@app.route('/get_people')
def get_people_data():
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the following three (currently hardcoded) people:
        - Luke Skywalker
        - C-3P0
        - R2-D2
    Gets information about each person from the API and returns a JSON object
    """
    
    # construct a dictionary of json objects
    people = []
    # only get first three people for this phase
    for index in range(1, 4) :
        person = requests.get('http://www.swapi.co/api/people/' + str(index)).json()
        people.append(person)
    return jsonify({"people": people})

@app.route('/get_planets')
def get_planets_data():
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the following three (currently hardcoded) planets:
        - Tatooine
        - Alderaan
        - Yavin IV
    Gets information about each planet from the API and returns a JSON object
    """
    
    # construct a dictionary of json objects
    planets = []
    # only get first three planets for this phase
    for index in range(1, 4) :
        planet = requests.get('http://www.swapi.co/api/planets/' + str(index)).json()
        planets.append(planet)
    return jsonify({"planets": planets})

@app.route('/get_species')
def get_species_data():
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the following three (currently hardcoded) species:
        - Human
        - Droid
        - Wookiee
    Gets information about each species from the API and returns a JSON object
    """
    
    # construct a dictionary of json objects
    species = []
    # only get first three species for this phase
    for index in range(1, 4) :
        s = requests.get('http://www.swapi.co/api/species/' + str(index)).json()
        species.append(s)
    return jsonify({"species": species})

@app.route('/')
def home():
    return send_file('templates/index.html')

if __name__ == "__main__":
    app.run(debug=True)
    