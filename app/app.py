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
        person["id"] = index
        people.append(person)
    return jsonify({"people": people})

    """
    response:
    
    {
        'people': [
            {
                'edited': '2014-12-20T21:17:56.891000Z',
                'hair_color': 'blond',
                'id': 1,
                'species': ['http://www.swapi.co/api/species/1/'],
                'gender': 'male',
                'created': '2014-12-09T13:50:51.644000Z',
                'height': '172',
                'skin_color': 'fair',
                'url': 'http://www.swapi.co/api/people/1/',
                'birth_year': '19BBY',
                'name': 'Luke Skywalker',
                'eye_color': 'blue',
                'starships': 
                    ['http://www.swapi.co/api/starships/12/', 'http://www.swapi.co/api/starships/22/'],
                'vehicles': 
                    ['http://www.swapi.co/api/vehicles/14/', 'http://www.swapi.co/api/vehicles/30/'],
                'homeworld': 'http://www.swapi.co/api/planets/1/',
                'mass': '77',
                'films': 
                    ['http://www.swapi.co/api/films/6/', 'http://www.swapi.co/api/films/3/', 'http://www.swapi.co/api/films/2/', 'http://www.swapi.co/api/films/1/', 'http://www.swapi.co/api/films/7/']
            },
            {
                'edited': '2014-12-20T21:17:50.309000Z',
                'hair_color': 'n/a',
                'id': 2,
                'species': ['http://www.swapi.co/api/species/2/'],
                'gender': 'n/a',
                'created': '2014-12-10T15:10:51.357000Z',
                'height': '167',
                'skin_color': 'gold',
                'url': 'http://www.swapi.co/api/people/2/',
                'birth_year': '112BBY',
                'name': 'C-3PO',
                'eye_color': 'yellow',
                'starships': [],
                'vehicles': [],
                'homeworld': 'http://www.swapi.co/api/planets/1/',
                'mass': '75',
                'films': 
                    ['http://www.swapi.co/api/films/5/', 'http://www.swapi.co/api/films/4/', 'http://www.swapi.co/api/films/6/', 'http://www.swapi.co/api/films/3/', 'http://www.swapi.co/api/films/2/', 'http://www.swapi.co/api/films/1/']
            },
            {
                'edited': '2014-12-20T21:17:50.311000Z',
                'hair_color': 'n/a',
                'id': 3,
                'species': ['http://www.swapi.co/api/species/2/'],
                'gender': 'n/a',
                'created': '2014-12-10T15:11:50.376000Z',
                'height': '96',
                'skin_color': 'white, blue',
                'url': 'http://www.swapi.co/api/people/3/',
                'birth_year': '33BBY',
                'name': 'R2-D2',
                'eye_color': 'red',
                'starships': [],
                'vehicles': [],
                'homeworld': 'http://www.swapi.co/api/planets/8/',
                'mass': '32',
                'films': 
                    ['http://www.swapi.co/api/films/5/', 'http://www.swapi.co/api/films/4/', 'http://www.swapi.co/api/films/6/', 'http://www.swapi.co/api/films/3/', 'http://www.swapi.co/api/films/2/', 'http://www.swapi.co/api/films/1/', 'http://www.swapi.co/api/films/7/']
            }
        ]
    }
    """

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
        planet["id"] = index
        planets.append(planet)
    return jsonify({"planets": planets})

    """
    response: 
    
    {
        'planets': [
            {
                'population': '200000',
                'residents':
                    ['http://www.swapi.co/api/people/1/', 'http://www.swapi.co/api/people/2/', 'http://www.swapi.co/api/people/4/', 'http://www.swapi.co/api/people/6/', 'http://www.swapi.co/api/people/7/', 'http://www.swapi.co/api/people/8/', 'http://www.swapi.co/api/people/9/', 'http://www.swapi.co/api/people/11/', 'http://www.swapi.co/api/people/43/', 'http://www.swapi.co/api/people/62/'],
                'id': 1,
                'created': '2014-12-09T13:50:49.641000Z',
                'edited': '2014-12-21T20:48:04.175778Z',
                'url': 'http://www.swapi.co/api/planets/1/',
                'name': 'Tatooine',
                'surface_water': '1',
                'rotation_period': '23',
                'orbital_period': '304',
                'climate': 'arid',
                'terrain': 'desert',
                'gravity': '1 standard',
                'diameter': '10465',
                'films': 
                    ['http://www.swapi.co/api/films/5/', 'http://www.swapi.co/api/films/4/', 'http://www.swapi.co/api/films/6/', 'http://www.swapi.co/api/films/3/', 'http://www.swapi.co/api/films/1/']
            },
            {
                'population': '2000000000',
                'residents':
                    ['http://www.swapi.co/api/people/5/', 'http://www.swapi.co/api/people/68/', 'http://www.swapi.co/api/people/81/'],
                'id': 2,
                'created': '2014-12-10T11:35:48.479000Z',
                'edited': '2014-12-20T20:58:18.420000Z',
                'url': 'http://www.swapi.co/api/planets/2/',
                'name': 'Alderaan',
                'surface_water': '40',
                'rotation_period': '24',
                'orbital_period': '364',
                'climate': 'temperate',
                'terrain': 'grasslands, mountains',
                'gravity': '1 standard',
                'diameter': '12500',
                'films': 
                    ['http://www.swapi.co/api/films/6/', 'http://www.swapi.co/api/films/1/']
            },
            {
                'population': '1000',
                'residents': [],
                'id': 3,
                'created': '2014-12-10T11:37:19.144000Z',
                'edited': '2014-12-20T20:58:18.421000Z',
                'url': 'http://www.swapi.co/api/planets/3/',
                'name': 'Yavin IV',
                'surface_water': '8',
                'rotation_period': '24',
                'orbital_period': '4818',
                'climate': 'temperate, tropical',
                'terrain': 'jungle, rainforests',
                'gravity': '1 standard',
                'diameter': '10200',
                'films': 
                    ['http://www.swapi.co/api/films/1/']
            }
        ]
    }
    """

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
        s["id"] = index
        species.append(s)
    return jsonify({"species": species})

    """
    response:
    
    {
        'species': [
            {
                'classification': 'mammal',
                'hair_colors': 'blonde, brown, black, red',
                'eye_colors': 'brown, blue, green, hazel, grey, amber',
                'id': 1,
                'created': '2014-12-10T13:52:11.567000Z',
                'language': 'Galactic Basic',
                'url': 'http://www.swapi.co/api/species/1/',
                'edited': '2015-04-17T06:59:55.850671Z',
                'films': 
                    ['http://www.swapi.co/api/films/7/', 'http://www.swapi.co/api/films/5/', 'http://www.swapi.co/api/films/4/', 'http://www.swapi.co/api/films/6/', 'http://www.swapi.co/api/films/3/', 'http://www.swapi.co/api/films/2/', 'http://www.swapi.co/api/films/1/'],
                'name': 'Human',
                'designation': 'sentient',
                'average_height': '180',
                'homeworld': 'http://www.swapi.co/api/planets/9/',
                'skin_colors': 'caucasian, black, asian, hispanic',
                'people': 
                    ['http://www.swapi.co/api/people/1/', 'http://www.swapi.co/api/people/4/', 'http://www.swapi.co/api/people/5/', 'http://www.swapi.co/api/people/6/', 'http://www.swapi.co/api/people/7/', 'http://www.swapi.co/api/people/9/', 'http://www.swapi.co/api/people/10/', 'http://www.swapi.co/api/people/11/', 'http://www.swapi.co/api/people/12/', 'http://www.swapi.co/api/people/14/', 'http://www.swapi.co/api/people/18/', 'http://www.swapi.co/api/people/19/', 'http://www.swapi.co/api/people/21/', 'http://www.swapi.co/api/people/22/', 'http://www.swapi.co/api/people/25/', 'http://www.swapi.co/api/people/26/', 'http://www.swapi.co/api/people/28/', 'http://www.swapi.co/api/people/29/', 'http://www.swapi.co/api/people/32/', 'http://www.swapi.co/api/people/34/', 'http://www.swapi.co/api/people/35/', 'http://www.swapi.co/api/people/43/', 'http://www.swapi.co/api/people/51/', 'http://www.swapi.co/api/people/60/', 'http://www.swapi.co/api/people/61/', 'http://www.swapi.co/api/people/62/', 'http://www.swapi.co/api/people/66/', 'http://www.swapi.co/api/people/67/', 'http://www.swapi.co/api/people/68/', 'http://www.swapi.co/api/people/69/', 'http://www.swapi.co/api/people/74/', 'http://www.swapi.co/api/people/81/', 'http://www.swapi.co/api/people/84/', 'http://www.swapi.co/api/people/85/', 'http://www.swapi.co/api/people/86/'],
                'average_lifespan': '120'
            },
            {
                'classification': 'artificial',
                'hair_colors': 'n/a',
                'eye_colors': 'n/a',
                'id': 2,
                'created': '2014-12-10T15:16:16.259000Z',
                'language': 'n/a',
                'url': 'http://www.swapi.co/api/species/2/',
                'edited': '2015-04-17T06:59:43.869528Z',
                'films': 
                    ['http://www.swapi.co/api/films/7/', 'http://www.swapi.co/api/films/5/', 'http://www.swapi.co/api/films/4/', 'http://www.swapi.co/api/films/6/', 'http://www.swapi.co/api/films/3/', 'http://www.swapi.co/api/films/2/', 'http://www.swapi.co/api/films/1/'],
                'name': 'Droid',
                'designation': 'sentient',
                'average_height': 'n/a',
                'homeworld': None,
                'skin_colors': 'n/a',
                'people': 
                    ['http://www.swapi.co/api/people/2/', 'http://www.swapi.co/api/people/3/', 'http://www.swapi.co/api/people/8/', 'http://www.swapi.co/api/people/23/', 'http://www.swapi.co/api/people/87/'],
                'average_lifespan': 'indefinite'
            },
            {
                'classification': 'mammal',
                'hair_colors': 'black, brown',
                'eye_colors': 'blue, green, yellow, brown, golden, red',
                'id': 3,
                'created': '2014-12-10T16:44:31.486000Z',
                'language': 'Shyriiwook',
                'url': 'http://www.swapi.co/api/species/3/',
                'edited': '2015-01-30T21:23:03.074598Z',
                'films': 
                    ['http://www.swapi.co/api/films/7/', 'http://www.swapi.co/api/films/6/', 'http://www.swapi.co/api/films/3/', 'http://www.swapi.co/api/films/2/', 'http://www.swapi.co/api/films/1/'],
                'name': 'Wookiee',
                'designation': 'sentient',
                'average_height': '210',
                'homeworld': 'http://www.swapi.co/api/planets/14/',
                'skin_colors': 'gray',
                'people': 
                    ['http://www.swapi.co/api/people/13/', 'http://www.swapi.co/api/people/80/'],
                'average_lifespan': '400'
            }
        ]
    }
    """

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

@app.route('/<path:path>')
def catch_all(path):
  return render_template('index.html')

@app.route('/')
def home():
    return send_file('templates/index.html')

if __name__ == "__main__":
    app.run(debug=True)
    
    