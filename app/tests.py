import unittest
from flask.ext.testing import TestCase
from flask import Flask
from models import *
from create_db import create_people, create_planets, create_species

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
        create_species()

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
        # species = Species.query.all()
        # for s in species:
        #     print (str(s)) # uncomment to see all classifications
        mammals = Species.query.filter(Species.classification == "mammal").all()
        # for m in mammals :
        #     print (str(m)) # uncomment to see all mammals
        assert len(mammals) > 0

    """
    Select a specie by name then test to see if it's in the database.
    """
    def test_query_species_2(self):
        specie = Species.query.filter(Species.name == "Pau'an").first()
        assert specie in db.session()
        assert specie.average_height == '190'

    """
    Select one specie and delete it.
    This query should return 1 for the number of rows deleted.
    """
    def test_query_species_3(self):
        specie = Species.query.filter(Species.name == "Pau'an").delete()
        assert specie == 1

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

    """
    Test our populate 'people' table script for initially filling the database.
    The number of rows in the 'people' table should be 88 because 3 initial + 85 total.
    """
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
        db.session.add(planet1)
        db.session.add(planet2)
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
        assert len(planets) == 62 # 2 from db init and 60 from adding entire populate script

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

    def test_planet_exists_2(self):
        create_planets()
        # query all Planets that possess a 'desert' terrain
        desert_planets = Planets.query.filter(Planets.terrain.contains("desert")).all()
        assert len(desert_planets) > 1 # there are other planets other than Tatooine which has a desert terrain

    def test_planet_exists_3(self):
        planet = Planets.query.filter(Planets.name == "Alderaan").first()
        assert planet in db.session()

if __name__ == '__main__':
	unittest.main(verbosity=2)