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
    if index.exists_in(whoosh_index_path, indexname = "people_index"):
        people_ix = index.open_dir(whoosh_index_path, indexname = "people_index")
    else:
        people_ix = index.create_in(whoosh_index_path, schema=PeopleSchema(),
                                    indexname="people_index")
        fill_people_index(people_ix)
    return people_ix


def fill_people_index(ix):
    writer = ix.writer()
    peopleList = People.query.all()
    for person in peopleList:
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


def search_results(ix, search_query, fields):
    qp = MultifieldParser(fields, schema=ix.schema, group=qparser.OrGroup)
    q = qp.parse(search_query)
    data = []
    data_index = 0
    with ix.searcher() as s:
        results = s.search(q)
        logger.debug(results)
        for hit in results:
            logger.debug(hit)
            data.append(dict(**hit))
            context = str()
            for field in fields:
                if(len(hit.highlights(field)) > 0):
                    context += hit.highlights(field)
            data[data_index]["context"] = context
            data_index += 1
    return data