import os

from whoosh import index, qparser
from whoosh.fields import SchemaClass, TEXT, KEYWORD, ID, STORED
from whoosh.qparser import MultifieldParser, QueryParser
from whoosh.query import *
from models import People, Species, Planets

whoosh_index_path = "whoosh_index"


def create_whoosh_dir():
    if not os.path.exists(whoosh_index_path):
        os.mkdir(whoosh_index_path)


class PeopleSchema(SchemaClass):
    id = ID(stored=True)
    name = KEYWORD(stored=True, lowercase=True)
    gender = KEYWORD(stored=True, lowercase=True)
    birth_year = KEYWORD(stored=True, lowercase=True)
    height = KEYWORD(stored=True, lowercase=True)
    mass = KEYWORD(stored=True, lowercase=True)
    hair_color = KEYWORD(stored=True, lowercase=True)
    eye_color = KEYWORD(stored=True, lowercase=True)
    description = KEYWORD(stored=True, lowercase=True)
    image = KEYWORD(stored=True, lowercase=True)
    homeworld = KEYWORD(stored=True, lowercase=True)
    skin_color = KEYWORD(stored=True, lowercase=True)
    species = KEYWORD(stored=True, lowercase=True)

def get_people_index():
    people_ix = index.create_in(whoosh_index_path, schema=PeopleSchema(),
                                indexname="people_index")
    fill_people_index(people_ix)
    return people_ix


def fill_people_index(ix):
    writer = ix.writer()
    people_list = People.query.all()
    for person in people_list:
        writer.add_document(name=person.name,
                            id=str(person.id),
                            gender=person.gender,
                            birth_year=person.birth_year,
                            height=person.height,
                            mass=person.mass,
                            hair_color=person.hair_color,
                            eye_color=person.eye_color,
                            description=person.description,
                            image=person.image,
                            homeworld=person.homeworld,
                            skin_color=person.skin_color,
                            species=person.species)
    writer.commit()


class PlanetsSchema(SchemaClass):
    id = ID(stored=True)
    name = KEYWORD(stored=True, lowercase=True)
    climate = KEYWORD(stored=True, lowercase=True)
    gravity = KEYWORD(stored=True, lowercase=True)
    terrain = KEYWORD(stored=True, lowercase=True)
    population = KEYWORD(stored=True, lowercase=True)
    description = KEYWORD(stored=True, lowercase=True)
    image = KEYWORD(stored=True, lowercase=True)


def get_planets_index():
    planets_ix = index.create_in(whoosh_index_path, schema=PlanetsSchema(),
                                 indexname="planets_index")
    fill_planets_index(planets_ix)
    return planets_ix


def fill_planets_index(ix):
    writer = ix.writer()
    planets_list = Planets.query.all()
    for planet in planets_list:
        writer.add_document(name=planet.name,
                            id=str(planet.id).lower(),
                            climate=planet.climate,
                            gravity=planet.gravity,
                            terrain=planet.terrain,
                            population=planet.population,
                            description=planet.description,
                            image=planet.image)
    writer.commit()


class SpeciesSchema(SchemaClass):
    id = ID(stored=True)
    name = KEYWORD(stored=True, lowercase=True)
    classification = KEYWORD(stored=True, lowercase=True)
    average_height = KEYWORD(stored=True, lowercase=True)
    average_lifespan = KEYWORD(stored=True, lowercase=True)
    language = KEYWORD(stored=True, lowercase=True)
    description = KEYWORD(stored=True, lowercase=True)
    image = KEYWORD(stored=True, lowercase=True)
    homeworld = KEYWORD(stored=True, lowercase=True)


def get_species_index():
    species_ix = index.create_in(whoosh_index_path, schema=SpeciesSchema(),
                                 indexname="species_index")
    fill_species_index(species_ix)
    return species_ix


def fill_species_index(ix):
    writer = ix.writer()
    species_list = Species.query.all()
    for species in species_list:
        writer.add_document(name=species.name,
                            id=str(species.id).lower(),
                            classification=species.classification,
                            average_height=species.average_height,
                            average_lifespan=species.average_lifespan,
                            language=species.language,
                            description=species.description,
                            image=species.image,
                            homeworld=species.homeworld)
    writer.commit()

class MyFuzzyTerm(FuzzyTerm):
     def __init__(self, fieldname, text, boost=1.0, maxdist=5, prefixlength=1, constantscore=True):
        super(MyFuzzyTerm, self).__init__(fieldname, text, boost, maxdist, len(text), constantscore)

def search_results(ix, search_query, fields, statement):
    qp = MultifieldParser(fields, schema=ix.schema, group=getattr(qparser, statement), termclass=MyFuzzyTerm)
    # qp = QueryParser(fields, schema=ix.schema, termclass=MyFuzzyTerm)
    qp.add_plugin(qparser.FuzzyTermPlugin())
    q = qp.parse(search_query)
    data = []
    with ix.searcher() as s:
        results = s.search(q, limit=None)
        for hit in results:
            data.append(dict(**hit))
    return data
