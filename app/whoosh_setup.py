import os
import logging
import time

from whoosh import index, qparser
from whoosh.fields import SchemaClass, TEXT, KEYWORD, ID, STORED
from whoosh.qparser import MultifieldParser
from models import People, Species, Planets

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

whoosh_index_path = "whoosh_index"


def create_whoosh_dir():
    if not os.path.exists(whoosh_index_path):
        os.mkdir(whoosh_index_path)


class PeopleSchema(SchemaClass):
    id = ID(stored=True)
    name = KEYWORD(stored=True)
    gender = KEYWORD(stored=True)
    birth_year = KEYWORD(stored=True)
    height = KEYWORD(stored=True)
    mass = KEYWORD(stored=True)
    hair_color = KEYWORD(stored=True)
    eye_color = KEYWORD(stored=True)
    description = KEYWORD(stored=True)
    image = KEYWORD(stored=True)
    homeworld = KEYWORD(stored=True)
    skin_color = KEYWORD(stored=True)
    species = KEYWORD(stored=True)


def get_people_index():
    people_ix = index.create_in(whoosh_index_path, schema=PeopleSchema(),
                                indexname="people_index")
    fill_people_index(people_ix)
    return people_ix


def fill_people_index(ix):
    writer = ix.writer()
    people_list = People.query.all()
    for person in people_list:
        writer.add_document(name=person.name.lower(),
                            id=str(person.id).lower(),
                            gender=person.gender.lower(),
                            birth_year=person.birth_year.lower(),
                            height=person.height.lower(),
                            mass=person.mass.lower(),
                            hair_color=person.hair_color.lower(),
                            eye_color=person.eye_color.lower(),
                            description=person.description.lower(),
                            image=person.image.lower(),
                            homeworld=person.homeworld.lower(),
                            skin_color=person.skin_color.lower(),
                            species=person.species.lower())
    writer.commit()


class PlanetsSchema(SchemaClass):
    id = ID(stored=True)
    name = KEYWORD(stored=True)
    climate = KEYWORD(stored=True)
    gravity = KEYWORD(stored=True)
    terrain = KEYWORD(stored=True)
    population = KEYWORD(stored=True)
    description = KEYWORD(stored=True)
    image = KEYWORD(stored=True)


def get_planets_index():
    planets_ix = index.create_in(whoosh_index_path, schema=PlanetsSchema(),
                                 indexname="planets_index")
    fill_planets_index(planets_ix)
    return planets_ix


def fill_planets_index(ix):
    writer = ix.writer()
    planets_list = Planets.query.all()
    for planet in planets_list:
        writer.add_document(name=planet.name.lower(),
                            id=str(planet.id).lower(),
                            climate=planet.climate.lower(),
                            gravity=planet.gravity.lower(),
                            terrain=planet.terrain.lower(),
                            population=planet.population.lower(),
                            description=planet.description.lower(),
                            image=planet.image.lower())
    writer.commit()


class SpeciesSchema(SchemaClass):
    id = ID(stored=True)
    name = KEYWORD(stored=True)
    classification = KEYWORD(stored=True)
    average_height = KEYWORD(stored=True)
    average_lifespan = KEYWORD(stored=True)
    language = KEYWORD(stored=True)
    description = KEYWORD(stored=True)
    image = KEYWORD(stored=True)
    homeworld = KEYWORD(stored=True)


def get_species_index():
    species_ix = index.create_in(whoosh_index_path, schema=SpeciesSchema(),
                                 indexname="species_index")
    fill_species_index(species_ix)
    return species_ix


def fill_species_index(ix):
    writer = ix.writer()
    species_list = Species.query.all()
    for species in species_list:
        writer.add_document(name=species.name.lower(),
                            id=str(species.id).lower(),
                            classification=species.classification.lower(),
                            average_height=species.average_height.lower(),
                            average_lifespan=species.average_lifespan.lower(),
                            language=species.language.lower(),
                            description=species.description.lower(),
                            image=species.image.lower(),
                            homeworld=species.homeworld.lower())
    writer.commit()


def search_results(ix, search_query, fields):
    qp = MultifieldParser(fields, schema=ix.schema, group=qparser.OrGroup)
    q = qp.parse(search_query.lower())
    data = []
    with ix.searcher() as s:
        results = s.search(q)
        logger.debug(results)
        for hit in results:
            logger.debug(hit)
            data.append(dict(**hit))
    return data