import unittest, json
from flask.ext.testing import TestCase
from flask import Flask
from models import *
from create_db import create_people, create_planets, create_species, populate_tables

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/swewars_test.db'  # set the database URI to a local database
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


"""
Test the Species model.
"""
class TestSpecies(TestCase):

    """
    Initialize the app and database.
    """
    def create_app(self):
        db.init_app(app)
        with app.app_context():
            db.create_all()
        return app

    """
    Insert data into the database.
    Run our populate species script.
    """
    def setUp(self):
        # create_species()
        s1 = Species(name = "Wookiee", classification = "mammal",
            average_height = "210", average_lifespan = "400", language = "Shyriiwook", description = "", image = "", homeworld = "")
        db.session.add(s1)
        s2 = Species(name = "Human", classification = "mammal",
            average_height = "180", average_lifespan = "120", language = "Galactic Basic", description = "", image = "", homeworld = "")
        db.session.add(s2)
        db.session.commit()


    """
    Destroy the database and its tables after testing is complete.
    """
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    """
    Run a where clause to get a query of all mammals.
    """
    def test_query_species_1(self):
        species = Species.query.filter(Species.classification == "mammal").all()
        assert len(species) > 0

    """
    Select a specie by name then test to see if it's in the database.
    """
    def test_query_species_2(self):
        species = Species.query.filter(Species.name == "Human").first()
        assert species in db.session()
        assert species.average_height == '180'

    """
    Select one specie and delete it.
    This query should return 1 for the number of rows deleted.
    """
    def test_query_species_3(self):
        species = Species.query.filter(Species.name == "Wookiee").delete()
        assert species == 1

    """
    Test clearing the Species table.
    """
    def test_clear_table(self):
        num = Species.query.delete()
        species = Species.query.all()
        assert len(species) == 0

"""
Test the People model.
"""
class TestPeople(TestCase):

    """
    Initialize the app and database.
    """
    def create_app(self):
        db.init_app(app)
        with app.app_context():
            db.create_all()
        return app

    """
    Insert data into the database.
    """
    def setUp(self) :
        person1 = People(name="Luke Skywalker", gender="male", birth_year="19BBY",
                         height="172", mass="77", hair_color="blond", eye_color="blue", description="YAY", image="YAY",
                         homeworld=" ", skin_color=" ", species=" ")
        person2 = People(name="C-3PO", gender="n/a", birth_year="112BBY",
                     height="167", mass="77", hair_color="n/a", eye_color="yellow", description="YAY", image="YAY",
                         homeworld=" ", skin_color=" ", species=" ")
        person3 = People(name="WHO", gender="n/a", birth_year="112BBY",
                         height="167", mass="77", hair_color="n/a", eye_color="yellow", description="YAY", image="YAY",
                         homeworld=" ", skin_color=" ", species=" ")
        db.session.add(person1)
        db.session.add(person2)
        db.session.add(person3)
        db.session.commit()

    """
    Destroy the database and its tables after testing is complete.
    """
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    """
    Test the number of rows in the People table after initialization.
    """
    def test_num_people_1(self):  # test the number of people on the table
        people = People.query.all()
        assert len(people) == 3

    """
    Test adding and deleting from the People table.
    """
    def test_delete_1(self):
        person4 = People(name="whoooooo", gender="n/a", birth_year="112BBY",
                         height="167", mass="77", hair_color="n/a", eye_color="yellow", description="YAY", image="YAY",
                         homeworld=" ", skin_color=" ", species=" ")
        db.session.add(person4)
        db.session.commit()
        people = People.query.all()
        assert len(people) == 4
        People.query.filter(People.name == "whoooooo").delete() # that's an invalid person... delete
        db.session.commit()
        assert len(People.query.all()) == 3

    """
    Test selecting a person by their name.
    """
    def test_select_person_1(self):
        person = People.query.filter(People.name == "WHO").first()
        assert person.gender == "n/a" and person.height == "167"

    """
    Test selecting a person by their birth year.
    """
    def test_select_person_2(self):
        person = People.query.filter(People.birth_year == "19BBY").first()
        assert person.gender == "male" and person.eye_color == "blue"

    """
    Test selecting a person by their birth year.
    """
    def test_select_person_2(self):
        person = People.query.filter(People.height == "172").first()
        assert person.name == "Luke Skywalker"

    """
    Test whether person exists in table.
    """
    def test_person_exists_1(self):
        person = People(name="Jon", gender="male", birth_year="112BBY",
                         height="167", mass="77", hair_color="n/a", eye_color="yellow", description="YAY", image="YAY",
                        homeworld = " ", skin_color = " ", species = " ")
        db.session.add(person)
        db.session.commit()
        assert person in db.session
        People.query.filter(People.name == "Jon").delete()
        assert person not in db.session

    """
    Test completely emptying the People table.
    """
    def test_empty_table(self):
        num = People.query.delete()
        db.session.commit()
        people = People.query.all()
        assert num == 3 # People.query.delete() returned the number of rows to be deleted
        assert len(people) == 0 # the number of rows in 'people' table should be zero

    # """
    # Test our populate 'people' table script for initially filling the database.
    # The number of rows in the 'people' table should be 88 because 3 initial + 85 total.
    # """
    def test_populate_script(self):
        create_people()
        people = People.query.all()
        # for person in people : # uncomment if you want to see the list of rows (all people from our database)
        #     print(str(person))
        assert len(people) == 88 # there are a total of 88 rows in the People table


"""
Test the Planets model.
"""
class TestPlanets(TestCase):

    """
    Initialize the app and database.
    """
    def create_app(self):
        db.init_app(app)
        with app.app_context():
            db.create_all()
        return app


    """
    Insert data into the database.
    """
    def setUp(self):
        planet1 = Planets(name = "Alderaan", climate = "temperate, tropical",
            gravity = "1 standard", terrain = "jungle, rainforests", population = 1000, description="YAY", image="YAY")
        planet2 = Planets(name = 'Tatooine', climate = "arid",
            gravity = "1 standard", terrain = "desert", population = 200000, description="YAY", image="YAY")
        planet3 = Planets(name = 'Invalid Planet', climate="unknown", gravity = "unknown", terrain = "unknown", population = "unknown", description = "unknown", image = "unknown")
        db.session.add(planet1)
        db.session.add(planet2)
        db.session.add(planet3)
        db.session.commit()


    """
    Destroy the database and its tables after testing is complete.
    """
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    """
    Test our populate 'planets' table script.
    """
    def test_populate_script(self):
        create_planets()
        planets = Planets.query.all()
        # for planet in planets: # uncomment if you want to see all planets that will be in our database
        #     print(str(planet))
        assert len(planets) == 63 # 3 from db init and 60 from adding entire populate script

    """
    Test emptying our 'planets' table.
    The number of entries in our table should always be 0 after this execution.
    """
    def test_empty_table(self):
        Planets.query.delete()
        db.session.commit()
        planets = Planets.query.all()
        assert len(planets) == 0

    """
    Test selecting a planet by its name.
    """
    def test_planet_exists_1(self):
        planet = Planets.query.filter(Planets.name == "Tatooine").first()
        assert planet in db.session()


    """
    Make sure deleted planet is no longer in database.
    """
    def test_planet_exists_2(self):
        planet = Planets.query.filter(Planets.name == "Invalid Planet").first()
        assert not planet in db.session()


    # """
    # Takes too long...
    # Website is getting timed out so comment out
    # """
    def test_planet_exists_2(self):
        create_planets()
        # query all Planets that possess a 'desert' terrain
        desert_planets = Planets.query.filter(Planets.terrain.contains("desert")).all()
        assert len(desert_planets) > 1 # there are other planets other than Tatooine which has a desert terrain

    def test_planet_exists_3(self):
        planet = Planets.query.filter(Planets.name == "Alderaan").first()
        assert planet in db.session()

"""
Test our RESTful API
"""
from app import get_people_data, get_planets_data, get_species_data, get_person_data, \
    get_planet_data, get_s_data, get_planet_for_person, get_species_for_person, \
    get_planet_for_species


class TestRESTfulAPI(TestCase):
    """
    Initialize the app and database.
    """
    def create_app(self):
        db.init_app(app)
        with app.app_context():
            db.create_all()
        return app

    """
    Insert data into the database.
    Run our populate species script.
    Populate all three tables.
    """
    def setUp(self):
        populate_tables()

    """
    Destroy the database and its tables after testing is complete.
    """
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_all_tables(self):
        people = People.query.all()
        species = Species.query.all()
        planets = Planets.query.all()
        # for person in people : # SEE THE 'people' TABLE
        #     print(str(person))
        # for s in species : # SEE THE 'species' TABLE
        #     print(str(s))
        # for planet in planets: # SEE THE 'planets' TABLE
        #     print (str(planet))
        assert len(people) > 0 and len(species) > 0 and len(planets) > 0

    """
    Test our get_people_data API call.
    """
    def test_get_people_data(self):
        output = get_people_data()
        assert str(output).__contains__("[200 OK]") # JSON response successful

    """
    Test our get_planets_data API call.
    """
    def test_get_planets_data(self):
        output = get_planets_data()
        assert str(output).__contains__("[200 OK]")  # JSON response successful

    """
    Test our get_planets_data API call.
    """
    def test_get_species_data(self):
        output = get_species_data()
        assert str(output).__contains__("[200 OK]")  # JSON response successful

    """
    Test the get_person_data API call.
    """
    def test_get_person_data_1(self):
        output = get_person_data(1).get_data()
        assert output is not None and str(output).__contains__("19BBY") # birth year should be 19BBY

    def test_get_person_data_2(self):
        output = get_person_data(2)
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_get_person_data_3(self):
        output = get_person_data(15)
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    """
    Test the get_planet_data API call.
    """
    def test_get_planet_data_1(self):
        output = get_planet_data(1).get_data()
        assert output is not None and str(output).__contains__("arid")  # climate should be arid

    def test_get_planet_data_2(self):
        output = get_planet_data(2)
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_get_planet_data_3(self):
        output = get_planet_data(14)
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    """
    Test the get_s_data API call. (Single specie)
    """
    def test_get_s_data_1(self):
        output = get_s_data(1).get_data()
        assert output is not None and str(output).__contains__("180")  # height should be 180

    def test_get_s_data_2(self):
        output = get_s_data(2)
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_get_s_data_3(self):
        output = get_s_data(13)
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

# get_planet_for_person, get_species_for_person, \
#     get_planet_for_species
    """
    Test the get_planet_for_person API call.
    """
    def test_get_planet_for_person_1(self):
        output = get_planet_for_person(1).get_data()
        assert output is not None and str(output).__contains__("arid")  # should have an 'arid' climate

    def test_get_planet_for_person_2(self):
        output = get_planet_for_person(2)
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_get_planet_for_person_3(self):
        output = get_planet_for_person(15)
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    """
    Test the get_species_for_person API call.
    """
    def test_get_species_for_person_1(self):
        output = get_species_for_person(1)
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_get_species_for_person_2(self):
        output = get_species_for_person(2)
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_get_species_for_person_3(self):
        output = get_species_for_person(14)
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    """
    Test the get_planet_for_species API call.
    """
    def test_get_planet_for_species_1(self):
        output = get_planet_for_species(1)
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_get_planet_for_species_2(self):
        output = get_planet_for_species(2)
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_get_planet_for_species_3(self):
        output = get_planet_for_species(13)
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_get_planet_for_species_4(self):
        output = get_planet_for_species(13).get_data()
        assert output is not None and str(output).__contains__("temperate")


from app import search

"""
Test the search functionality
"""
class TestSearch(TestCase):
    """
    Initialize the app and database.
    """
    def create_app(self):
        db.init_app(app)
        with app.app_context():
            db.create_all()
        return app

    """
    Insert data into the database.
    Run our populate species script.
    """
    def setUp(self):
        populate_tables()

    """
    Destroy the database and its tables after testing is complete.
    """
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_search_query_1(self):
        output = search("luke")
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_search_query_2(self):
        output = search("Wookiee")
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_search_query_3(self):
        output = search("Luke Skywalker")
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_search_query_4(self):
        output = search("blue")
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_search_query_5(self):
        output = search("R5-D4")
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_search_query_6(self):
        output = search("Quermia")
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    def test_search_query_7(self):
        output = search("cwencjkweuiapdkospwqmklqiwdqw")
        assert output is not None and str(output).__contains__("[200 OK]")  # JSON response successful

    """
    Test an empty search
    """ 
    def test_search_1(self):
        output = search('')
        assert str(output.get_data()).__contains__('[]')
    
    """
    Test a legit search
    """
    def test_search_2(self):
        output = search('Luke')
        assert str(output.get_data()).__contains__('Luke Skywalker')
    
    """
    Test an AND search
    """
    def test_search_3(self):
        output = search('Luke Skywalker')
        assert str(output.get_data()).__contains__('Luke Skywalker')

    """
    Test an OR search
    """
    def test_search_4(self):
        output = search('Luke Skywalker')
        assert str(output.get_data()).__contains__('Luke Skywalker')

    """
    Searching for 'Wookiee' should get back row for Wookiee.
    """
    def test_search_5(self):
        output = search('Wookiee')
        assert str(output.get_data()).__contains__('Wookiee')

    """
    Searching for 'Anakin' should get back row for Anakin.
    """
    def test_search_6(self):
        output = search('Anakin')
        assert str(output.get_data()).__contains__('Anakin')

if __name__ == '__main__':
	unittest.main(verbosity=2)
    
"""
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
app.py              140     48    66%   165-166, 183-184, 211-219, 224-232, 238-246, 252-260, 265-266, 271, 276, 281, 286, 291, 297, 302, 314-316, 321-323, 326
create_db.py         56      0   100%
models.py            83      3    96%   83, 149, 217
tests.py            269      5    98%   152-153, 266-267, 549
whoosh_setup.py      85      1    99%   14
-----------------------------------------------
TOTAL               633     57    91%   
"""
