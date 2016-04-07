from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ----\
# People
# ----
class People(db.Model):
    """"People Model"""

    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    name = db.Column(db.String(256))
    gender = db.Column(db.String(256))
    birth_year = db.Column(db.String(256))
    height = db.Column(db.String(256))
    mass = db.Column(db.String(256))
    hair_color = db.Column(db.String(256))
    eye_color = db.Column(db.String(256))
    description = db.Column(db.Text())
    image = db.Column(db.String(256))
    homeworld = db.Column(db.String(256))
    skin_color = db.Column(db.String(256))

    def __init__(self, name, gender, birth_year, height, mass, hair_color, eye_color, description, image, homeworld, skin_color):
        """
        Assigns variables to the class upon initialization.

        Parameters
        ----------
        self : Planets
        name : Column(String)
        gender : Column(String)
        birth_year : Column(String)
        height: Column(Integer)
        mass : Column(Integer)
        hair_color : Column(String)
        eye_color : Column(String)

        Returns
        -------
        People
        """
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.description = description
        self.image = image
        self.homeworld = homeworld
        self.skin_color = skin_color


    @property
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "gender" : self.gender,
            "birth_year" : self.birth_year,
            "height" : self.height,
            "mass" : self.mass,
            "hair_color" : self.hair_color,
            "eye_color" : self.eye_color,
            "description" : str(self.description),
            "image" : self.image,
            "homeworld" : self.homeworld,
            "skin_color" : self.skin_color
        }

    """
    Determine how the People model object looks when converted to String. (str())
    """
    def __repr__(self):
        return 'Name: %r' % self.name + ' Gender: %r' % self.gender + ' Birth year: %r' % self.birth_year + \
               ' Height: %r' % self.height + ' Mass: %r' % self.mass + ' Hair Color: %r' % self.hair_color + \
               'Eye Color: %r' % self.eye_color


# ----
# Planets
# ----
class Planets(db.Model):
    """Planets Model"""

    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    name = db.Column(db.String(256))
    climate = db.Column(db.String(256))
    gravity = db.Column(db.String(256))
    terrain = db.Column(db.String(256))
    population = db.Column(db.String(256))
    description = db.Column(db.Text())
    image = db.Column(db.String(256))
    
    def __init__(self, name, climate, gravity, terrain, population, description, image):
        """
        Assigns variables to the class upon initialization.

        Parameters
        ----------
        self : Planets
        name : Column(String)
        climate : Column(String)
        gravity : Column(String)
        terrain : Column(String)
        population : Column(Integer)

        Returns
        -------
        Planets
        """
        self.name = name
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.population = population
        self.description = description
        self.image = image

    @property
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "climate" : self.climate,
            "gravity" : self.gravity,
            "terrain" : self.terrain,
            "population" : self.population,
            "description" : str(self.description),
            "image" : self.image
        }

    """
    Determine how the Planets model object looks when converted to String. (str())
    """

    def __repr__(self):
        return 'Name: %r' % self.name + ' Climate: %r' % self.climate + ' Gravity: %r' % self.gravity + \
               ' Terrain: %r' % self.terrain + ' Population: %r' % self.population

# ----
# Species
# ----
class Species(db.Model):
    """Species Model"""

    __tablename__ = 'species'

    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    name = db.Column(db.String(256))
    classification = db.Column(db.String(256))
    average_height = db.Column(db.String(256))
    average_lifespan = db.Column(db.String(256))
    language = db.Column(db.String(256))
    description = db.Column(db.Text())
    image = db.Column(db.String(256))
    homeworld = db.Column(db.String(256))

    def __init__(self, name, classification, average_height, average_lifespan, language, description, image, homeworld):
        """
        Assigns variables to the class upon initialization.

        Parameters
        ----------
        self : Planets
        name : Column(String)
        classification : Column(String)
        average_height : Column(String)
        average_lifespan : Column(String)
        language : Column(String)

        Returns
        -------
        People
        """
        self.name = name
        self.classification = classification
        self.average_height = average_height
        self.average_lifespan = average_lifespan
        self.language = language
        self.description = description
        self.image = image
        self.homeworld = homeworld


    @property
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "classification" : self.classification,
            "average_height" : self.average_height,
            "average_lifespan" : self.average_lifespan,
            "language" : self.language,
            "description" : str(self.description),
            "image" : self.image,
            "homeworld" : self.homeworld
        }

    """
    Determine how the Species model object looks when converted to String. (str())
    """

    def __repr__(self):
        return 'Name: %r' % self.name + ' Classification: %r' % self.classification + ' Average Height: %r' % self.average_height + \
               ' Average Lifespan: %r' % self.average_lifespan + ' Language: %r' % self.language