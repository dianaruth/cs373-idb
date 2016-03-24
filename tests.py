from unittest import main, TestCase
from models import *
from flask import *
from sqlalchemy import *

class tests(TestCase):

    def test_init_people_1(self):
        person_name = "Luke Skywalker"
        test_people = People(name = person_name, gender = "male", birth_year = "19BBY", height = 167, mass = 77,
            hair_color = "blond", eye_color = "blue")
        self.assertEqual(person_name, test_people.name)
        self.assertEqual(77, test_people.mass)

if __name__ == '__main__':
    main()