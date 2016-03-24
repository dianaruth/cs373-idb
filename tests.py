from unittest import main, TestCase
from models import *
from flask import *
from sqlalchemy import *

class tests(TestCase):

    """
    For Phase I of the project, we will only be testing the inialization of the models
    since we are not required to set up a database through Carina, yet.
    """
    def test_init_people_1(self):
        person_name = "Luke Skywalker"
        test_person = People(name = person_name, gender = "male", birth_year = "19BBY", 
            height = 172, mass = 77, hair_color = "blond", eye_color = "blue")
        self.assertEqual(person_name, test_person.name)
        self.assertEqual(77, test_person.mass)

    def test_init_people_2(self):
        person_name = "C-3PO"
        test_person = People(name = person_name, gender = "n/a", birth_year = "112BBY",
                height = 167, mass = 77, hair_color = "n/a", eye_color = "yellow")
        self.assertEqual(person_name, test_person.name)
        self.assertEqual(167, test_person.height)

    def test_init_people_3(self):
        person_name = "R2-D2"
        test_person = People(name = person_name, gender = "n/a", birth_year = "33BBY",
                height = 96, mass = 32, hair_color = "n/a", eye_color = "red")
        self.assertEqual("n/a", test_person.gender)
        self.assertEqual("n/a", test_person.hair_color)

    def test_init_planets_1(self):
        planet_name = "Alderaan"
        test_planet = Planets(name = planet_name, climate = "temperature", 
            gravity = "1 standard", terrain = "grasslands, mountains", population = 2000000000)
        self.assertEqual(planet_name, test_planet.name)

    def test_init_planets_2(self):
        planet_name = "Tatooine"
        test_planet = Planets(name = planet_name, climate = "arid", 
            gravity = "1 standard", terrain = "desert", population = 200000)
        self.assertEqual(200000, test_planet.population)

    def test_init_planets_3(self):
        planet_name = "Yavin IV"
        test_planet = Planets(name = planet_name, climate = "temperate, tropical", 
            gravity = "1 standard", terrain = "jungle, rainforests", population = 1000)
        self.assertEqual(1000, test_planet.population)
        self.assertEqual("temperate, tropical", test_planet.climate)

    def test_init_species_1(self):
        species_name = "Droid"
        test_specie = Species(name = species_name, classification = "artificial",
            average_height = "n/a", average_lifespan = "indefinite", language = "n/a")
        self.assertEqual("indefinite", test_specie.average_lifespan)

    def test_init_species_2(self):
        species_name = "Human"
        test_specie = Species(name = species_name, classification = "mammal",
            average_height = "180", average_lifespan = "120", language = "Galactic Basic")
        self.assertEqual("180", test_specie.average_height)

    def test_init_species_3(self):
        species_name = "Wookiee"
        test_specie = Species(name = species_name, classification = "mammal",
            average_height = "210", average_lifespan = "400", language = "Shyriiwook")
        self.assertEqual("210", test_specie.average_height)
        self.assertEqual("Shyriiwook", test_specie.language)


if __name__ == '__main__':
    main()