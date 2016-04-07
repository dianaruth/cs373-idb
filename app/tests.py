import unittest
from flask.ext.testing import TestCase
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from models import *
from create_db import create_people, create_planets, create_species

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/swewars_test.db'  # set the database URI to a local database
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
                         height="172", mass="77", hair_color="blond", eye_color="blue", description="YAY", image="YAY")

        person2 = People(name="C-3PO", gender="n/a", birth_year="112BBY",
                     height="167", mass="77", hair_color="n/a", eye_color="yellow", description="YAY", image="YAY")
        person3 = People(name="WHO", gender="n/a", birth_year="112BBY",
                         height="167", mass="77", hair_color="n/a", eye_color="yellow", description="YAY", image="YAY")
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
                         height="167", mass="77", hair_color="n/a", eye_color="yellow", description="YAY", image="YAY")
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
                         height="167", mass="77", hair_color="n/a", eye_color="yellow", description="YAY", image="YAY")
        db.session.add(person)
        db.session.commit()
        assert person in db.session
        People.query.filter(People.name == "Jon").delete()
        assert person not in db.session

    """
    Test completely emptying the People table.
    """
    def test_empty_table_1(self):
        num = People.query.delete()
        db.session.commit()
        people = People.query.all()
        assert num == 3 # People.query.delete() returned the number of rows to be deleted
        assert len(people) == 0 # the number of rows in 'people' table should be zero

    """
    Test our populate 'people' table script for initially filling the database.
    The number of rows in the 'people' table should be 88.
    """
    def test_populate_script(self):
        create_people()
        people = People.query.all()
        # for person in people : # uncomment if you want to see the list of rows (all people from our database)
        #     print(str(person))
        assert len(people) == 88 # there are a total of 88 rows in the People table

if __name__ == '__main__':
	unittest.main()