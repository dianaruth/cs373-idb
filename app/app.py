# -*- coding: utf-8 -*-
from flask import Flask, render_template, send_file, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://guestbook-admin:my-guestbook-admin-password@pythonwebapp_db/guestbook'

db = SQLAlchemy(app)

if db == None:
    print("nope")

@app.route('/get_people')
def get_people_data():
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the following three (currently hardcoded) people:
        - Luke Skywalker
        - C-3P0
        - R2-D2
    Gets information about each person from the API and returns a JSON object
    """
    
    # construct a list of json objects
    people = []
    # only get first three people for this phase
    for index in range(1, 4) :
        person = requests.get('http://www.swapi.co/api/people/' + str(index)).json()
        j = {}
        j["id"] = index
        if index == 1 :
            j["description"] = "Luke Skywalker was a Force-sensitive Human male who helped defeat the Galactic Empire in the Galactic Civil War and helped found the New Republic, as well as the New Jedi Order. Born in 19 BBY as the son of the fallen Jedi Knight Anakin Skywalker and the Queen and Senator of Naboo, Padmé Amidala, Luke was raised on Tatooine and hidden from Emperor Palpatine and his father, who had recently become Darth Vader, Dark Lord of the Sith. In 0 BBY, Skywalker's life changed forever. A chance purchase of two droids, R2-D2 and C-3PO, led to him to receive training in the ways of the Force from Jedi Master Obi-Wan Kenobi and to meet Han Solo, and Princess Leia Organa, who was, unbeknownst to him, his twin sister. Skywalker then destroyed the first Death Star and joined the Rebel Alliance."
        elif index == 2 :
            j["description"] = "C-3PO, sometimes spelled See-Threepio and often referred to as Threepio, was a bipedal, humanoid protocol droid designed to interact with organics, programmed primarily for etiquette and protocol. He was fluent in over six million forms of communication, and developed a fussy and worry-prone personality throughout his many decades of operation. After being destroyed and discarded on the planet Tatooine before 32 BBY, C-3PO was rebuilt; his salvaged nature gave him special qualities that distinguished him from similar droid models. Along with his counterpart, the astromech droid R2-D2, C-3PO constantly found himself directly involved in pivotal moments of galactic history, and aided in saving the galaxy on many occasions. C-3PO considered various droids and organics to be friends of his, and was very dedicated to them, as well as to any master that he served."
        elif index == 3 :
            j["description"] = "R2-D2, pronounced Artoo-Detoo and often referred to as Artoo, was an R2-series astromech droid manufactured by Industrial Automaton prior to 32 BBY. Resourceful and spunky, the droid developed an adventurous personality during his many decades of operation. Inside of his cylindrical frame were many arms, sensors, and other tools that could be extended to fulfill various needs, such as slicing computers, extinguishing fires, projecting holograms, repairing starships, and flying. Along with his counterpart, the protocol droid C-3PO, R2-D2 constantly found himself directly involved in pivotal moments of galactic history. His bravery, coupled with his many gadgets, played large roles in saving the galaxy time and time again. Like other astromech droids, R2-D2 could walk on two legs or use a third leg to roll across the ground."
        a = []
        for s in person["species"] :
            i = s.rfind("/", 0, len(s) - 1)
            a.append(int(s[i+1:-1]))
        j["species"] = a
        if (person["homeworld"]) :
            i = person["homeworld"].rfind("/", 0, len(person["homeworld"]) - 1)
            j["homeworld"] = int(person["homeworld"][i+1:-1])
        j["name"] = person["name"]
        j["gender"] = person["gender"]
        j["birth_year"] = person["birth_year"]
        j["height"] = person["height"]
        j["mass"] = person["mass"]
        j["hair_color"] = person["hair_color"]
        j["eye_color"] = person["eye_color"]
        people.append(j)
    return jsonify({"people": people})

@app.route('/get_planets')
def get_planets_data():
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the following three (currently hardcoded) planets:
        - Tatooine
        - Alderaan
        - Yavin IV
    Gets information about each planet from the API and returns a JSON object
    """
    
    # construct a list of json objects
    planets = []
    # only get first three planets for this phase
    for index in range(1, 4) :
        planet = requests.get('http://www.swapi.co/api/planets/' + str(index)).json()
        j = {}
        j["id"] = index
        if index == 1 :
            j["description"] = "Tatooine (pronounced /tætu'in/; Jawaese: Tah doo Een e[8]) was a desert world and the first planet in the binary Tatoo star system. It was part of the Arkanis sector in the Outer Rim Territories. It was inhabited by poor locals who mostly farmed moisture for a living. Other activities included used equipment retailing and scrap dealing. The planet was on the 5709-DC Shipping Lane, a spur of the Triellus Trade Route, which itself connected to the Sisar Run. The planet was not far from the Corellian Run. It had its own navigation system. However, it would still play a role in galactic events, serving as the home of Anakin Skywalker. It was here that Jedi Master Qui-Gon Jinn recognized Anakin's potential to become a Jedi and where he introduced him to Obi-Wan Kenobi, his future master and mentor. Tatooine was also the home of Anakin's son, Luke, where he lived until his early adulthood. The planet acquired a bad reputation, often being viewed as the cesspool of the galaxy due to the large number of criminals who could be found there."
        elif index == 2 :
            j["description"] = "Alderaan, located in the Core Worlds, was the second planet in the Alderaan system, and the home of many famous heroes, including Leia Organa Solo, Bail Organa, and Ulic Qel-Droma. Renowned galaxy-wide for their planet's unspoiled beauty, refined culture, and commitment to peace, Alderaanians worked with and around the land to preserve as much of the natural surroundings as they could. Originally the home of the Killiks, Alderaan was later conquered by Humans. Despite a battle during the Great Galactic War and a civil war during the subsequent Cold War, Alderaan remained peaceful during much of galactic history. However, in 0 BBY, Grand Moff Tarkin and the Galactic Empire wanted to intimidate the galaxy into submission, and destroyed the unarmed and peaceful planet using the first Death Star's superlaser."
        elif index == 3 :
            j["description"] = "Yavin 4 was one of three habitable moons orbiting the gas giant Yavin. It was mainly covered in jungle and rainforest, and despite being remote and unheard of, it would play an important role in galactic events, including the seduction of Jedi Knight Exar Kun to the dark side and the destruction of Sith Lord Freedon Nadd during the Great Sith War, the site of the eventual final death of the maddened Jedi Revan in the waning days of the Galactic War, a ferocious duel between Jedi and Sith during the Clone Wars, and serving as the base of the Alliance to Restore the Republic during the Battle of Yavin and as a battlefield in other battles of the Galactic Civil War. An attack was launched on the Death Star from this moon. It also became the base for a Jedi Academy after the war ended."
        a = []
        for r in planet["residents"] :
            i = r.rfind("/", 0, len(r) - 1)
            a.append(int(r[i+1:-1]))
        j["residents"] = a
        j["name"] = planet["name"]
        j["climate"] = planet["climate"]
        j["gravity"] = planet["gravity"]
        j["terrain"] = planet["terrain"]
        j["population"] = planet["population"]
        planets.append(j)
    return jsonify({"planets": planets})

@app.route('/get_species')
def get_species_data():
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the following three (currently hardcoded) species:
        - Human
        - Droid
        - Wookiee
    Gets information about each species from the API and returns a JSON object
    """
    
    # construct a list of json objects
    species = []
    # only get first three species for this phase
    for index in range(1, 4) :
        s = requests.get('http://www.swapi.co/api/species/' + str(index)).json()
        j = {}
        j["id"] = index
        if index == 1 :
            j["description"] = "Humans, taxonomically referred to as Homo sapiens, were the galaxy's most numerous and politically dominant sentient species with millions of major and minor colonies galaxywide. Believed to have originated on the galactic capital of Coruscant, they could be found anywhere, engaged in many different pursuits: spacers, mercenaries, smugglers, merchants, soldiers, assassins, farmers, crime lords, laborers, slaves, slavers, and many others, including Jedi and Sith. Since Humans were the most common sentient species, they were often considered to be a standard or average to which the biology, psychology, and culture of other species were compared."
        elif index == 2 :
            j["description"] = "Droids, short for androids, or also called robots, were mechanical beings, often possessing artificial intelligence. They were used in a variety of roles and environments, often those considered too menial or too dangerous for humans and other species. Droids were also used in fields that required extensive specialization and knowledge, such as medical droids and astromech droids. Droids designed for combat were battle droids. Depending on the model and its corresponding purpose, droids were totally obedient, rugged, expendable, capable of vast memory recall, and mathematically precise. These characteristics made them well suited for many jobs, though the lack of independent thought in the cheaper, less advanced models limited their capability. This lack of autonomy was simultaneously a vast asset and a glaring weakness—an asset in terms of obedience and control but a massive drawback in terms of effectiveness. Designers faced a fundamental paradox—make the droids overly intelligent, and they might rebel; yet make the droids not intelligent enough and they would be ineffectual. Customarily, droid names were an arrangement of numbers and letters."
        elif index == 3 :
            j["description"] = "The Wookiees, whose name for themselves translated to the People of the Trees, were a species of tall, hairy humanoids that were inhabitants of the planet Kashyyyk. One of the most noteworthy members of the species was Chewbacca, Han Solo's best friend and co-pilot, who played a vital role in the Galactic Civil War and afterwards. A race of arboreal mammals, the Wookiees lived in treehouses nestled in the canopy of the towering wroshyr trees. Despite their fearsome appearance, they were usually gentle, although they were prone to devastating fits of rage when provoked."
        a = []
        for p in s["people"] :
            i = p.rfind("/", 0, len(p) - 1)
            a.append(int(p[i+1:-1]))
        j["people"] = a
        if (s["homeworld"]) :
            i = s["homeworld"].rfind("/", 0, len(s["homeworld"]) - 1)
            j["homeworld"] = int(s["homeworld"][i+1:-1])
        j["name"] = s["name"]
        j["classification"] = s["classification"]
        j["average_height"] = s["average_height"]
        j["average_lifespan"] = s["average_lifespan"]
        j["language"] = s["language"]
        species.append(j)
    return jsonify({"species": species})
    
@app.route("/get_person/<path>")
def get_person_data(path):
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the person with id "path"
    Returns data about the person in the form of a JSON object
    """
    
    person = requests.get('http://www.swapi.co/api/people/' + path).json()
    j = {}
    index = int(path)
    j["id"] = index
    if index == 1 :
        j["description"] = "Luke Skywalker was a Force-sensitive Human male who helped defeat the Galactic Empire in the Galactic Civil War and helped found the New Republic, as well as the New Jedi Order. Born in 19 BBY as the son of the fallen Jedi Knight Anakin Skywalker and the Queen and Senator of Naboo, Padmé Amidala, Luke was raised on Tatooine and hidden from Emperor Palpatine and his father, who had recently become Darth Vader, Dark Lord of the Sith. In 0 BBY, Skywalker's life changed forever. A chance purchase of two droids, R2-D2 and C-3PO, led to him to receive training in the ways of the Force from Jedi Master Obi-Wan Kenobi and to meet Han Solo, and Princess Leia Organa, who was, unbeknownst to him, his twin sister. Skywalker then destroyed the first Death Star and joined the Rebel Alliance."
    elif index == 2 :
        j["description"] = "C-3PO, sometimes spelled See-Threepio and often referred to as Threepio, was a bipedal, humanoid protocol droid designed to interact with organics, programmed primarily for etiquette and protocol. He was fluent in over six million forms of communication, and developed a fussy and worry-prone personality throughout his many decades of operation. After being destroyed and discarded on the planet Tatooine before 32 BBY, C-3PO was rebuilt; his salvaged nature gave him special qualities that distinguished him from similar droid models. Along with his counterpart, the astromech droid R2-D2, C-3PO constantly found himself directly involved in pivotal moments of galactic history, and aided in saving the galaxy on many occasions. C-3PO considered various droids and organics to be friends of his, and was very dedicated to them, as well as to any master that he served."
    elif index == 3 :
        j["description"] = "R2-D2, pronounced Artoo-Detoo and often referred to as Artoo, was an R2-series astromech droid manufactured by Industrial Automaton prior to 32 BBY. Resourceful and spunky, the droid developed an adventurous personality during his many decades of operation. Inside of his cylindrical frame were many arms, sensors, and other tools that could be extended to fulfill various needs, such as slicing computers, extinguishing fires, projecting holograms, repairing starships, and flying. Along with his counterpart, the protocol droid C-3PO, R2-D2 constantly found himself directly involved in pivotal moments of galactic history. His bravery, coupled with his many gadgets, played large roles in saving the galaxy time and time again. Like other astromech droids, R2-D2 could walk on two legs or use a third leg to roll across the ground."
    a = []
    for s in person["species"] :
        i = s.rfind("/", 0, len(s) - 1)
        a.append(int(s[i+1:-1]))
    j["species"] = a
    if (person["homeworld"]) :
        i = person["homeworld"].rfind("/", 0, len(person["homeworld"]) - 1)
        j["homeworld"] = int(person["homeworld"][i+1:-1])
    j["name"] = person["name"]
    j["gender"] = person["gender"]
    j["birth_year"] = person["birth_year"]
    j["height"] = person["height"]
    j["mass"] = person["mass"]
    j["hair_color"] = person["hair_color"]
    j["eye_color"] = person["eye_color"]
    return jsonify({"person": j})

@app.route('/get_planet/<path>')
def get_planet_data(path):
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the planet with id "path"
    Returns data about the planet in the form of a JSON object
    """
    
    planet = requests.get('http://www.swapi.co/api/planets/' + path).json()
    j = {}
    index = int(path)
    j["id"] = index
    if index == 1 :
        j["description"] = "Tatooine (pronounced /tætu'in/; Jawaese: Tah doo Een e[8]) was a desert world and the first planet in the binary Tatoo star system. It was part of the Arkanis sector in the Outer Rim Territories. It was inhabited by poor locals who mostly farmed moisture for a living. Other activities included used equipment retailing and scrap dealing. The planet was on the 5709-DC Shipping Lane, a spur of the Triellus Trade Route, which itself connected to the Sisar Run. The planet was not far from the Corellian Run. It had its own navigation system. However, it would still play a role in galactic events, serving as the home of Anakin Skywalker. It was here that Jedi Master Qui-Gon Jinn recognized Anakin's potential to become a Jedi and where he introduced him to Obi-Wan Kenobi, his future master and mentor. Tatooine was also the home of Anakin's son, Luke, where he lived until his early adulthood. The planet acquired a bad reputation, often being viewed as the cesspool of the galaxy due to the large number of criminals who could be found there."
    elif index == 2 :
        j["description"] = "Alderaan, located in the Core Worlds, was the second planet in the Alderaan system, and the home of many famous heroes, including Leia Organa Solo, Bail Organa, and Ulic Qel-Droma. Renowned galaxy-wide for their planet's unspoiled beauty, refined culture, and commitment to peace, Alderaanians worked with and around the land to preserve as much of the natural surroundings as they could. Originally the home of the Killiks, Alderaan was later conquered by Humans. Despite a battle during the Great Galactic War and a civil war during the subsequent Cold War, Alderaan remained peaceful during much of galactic history. However, in 0 BBY, Grand Moff Tarkin and the Galactic Empire wanted to intimidate the galaxy into submission, and destroyed the unarmed and peaceful planet using the first Death Star's superlaser."
    elif index == 3 :
        j["description"] = "Yavin 4 was one of three habitable moons orbiting the gas giant Yavin. It was mainly covered in jungle and rainforest, and despite being remote and unheard of, it would play an important role in galactic events, including the seduction of Jedi Knight Exar Kun to the dark side and the destruction of Sith Lord Freedon Nadd during the Great Sith War, the site of the eventual final death of the maddened Jedi Revan in the waning days of the Galactic War, a ferocious duel between Jedi and Sith during the Clone Wars, and serving as the base of the Alliance to Restore the Republic during the Battle of Yavin and as a battlefield in other battles of the Galactic Civil War. An attack was launched on the Death Star from this moon. It also became the base for a Jedi Academy after the war ended."
    a = []
    for r in planet["residents"] :
        i = r.rfind("/", 0, len(r) - 1)
        a.append(int(r[i+1:-1]))
    j["residents"] = a
    j["name"] = planet["name"]
    j["climate"] = planet["climate"]
    j["gravity"] = planet["gravity"]
    j["terrain"] = planet["terrain"]
    j["population"] = planet["population"]
    return jsonify({"planet": j})

@app.route('/get_s/<path>')
def get_s_data(path):
    """
    Calls the Star Wars API (www.swapi.com) to obtain information on the species with id "path"
    Returns data about the species in the form of a JSON object
    """
    
    s = requests.get('http://www.swapi.co/api/species/' + path).json()
    j = {}
    index = int(path)
    j["id"] = index
    if index == 1 :
        j["description"] = "Humans, taxonomically referred to as Homo sapiens, were the galaxy's most numerous and politically dominant sentient species with millions of major and minor colonies galaxywide. Believed to have originated on the galactic capital of Coruscant, they could be found anywhere, engaged in many different pursuits: spacers, mercenaries, smugglers, merchants, soldiers, assassins, farmers, crime lords, laborers, slaves, slavers, and many others, including Jedi and Sith. Since Humans were the most common sentient species, they were often considered to be a standard or average to which the biology, psychology, and culture of other species were compared."
    elif index == 2 :
        j["description"] = "Droids, short for androids, or also called robots, were mechanical beings, often possessing artificial intelligence. They were used in a variety of roles and environments, often those considered too menial or too dangerous for humans and other species. Droids were also used in fields that required extensive specialization and knowledge, such as medical droids and astromech droids. Droids designed for combat were battle droids. Depending on the model and its corresponding purpose, droids were totally obedient, rugged, expendable, capable of vast memory recall, and mathematically precise. These characteristics made them well suited for many jobs, though the lack of independent thought in the cheaper, less advanced models limited their capability. This lack of autonomy was simultaneously a vast asset and a glaring weakness—an asset in terms of obedience and control but a massive drawback in terms of effectiveness. Designers faced a fundamental paradox—make the droids overly intelligent, and they might rebel; yet make the droids not intelligent enough and they would be ineffectual. Customarily, droid names were an arrangement of numbers and letters."
    elif index == 3 :
        j["description"] = "The Wookiees, whose name for themselves translated to the People of the Trees, were a species of tall, hairy humanoids that were inhabitants of the planet Kashyyyk. One of the most noteworthy members of the species was Chewbacca, Han Solo's best friend and co-pilot, who played a vital role in the Galactic Civil War and afterwards. A race of arboreal mammals, the Wookiees lived in treehouses nestled in the canopy of the towering wroshyr trees. Despite their fearsome appearance, they were usually gentle, although they were prone to devastating fits of rage when provoked."
    a = []
    for p in s["people"] :
        i = p.rfind("/", 0, len(p) - 1)
        a.append(int(p[i+1:-1]))
    j["people"] = a
    if (s["homeworld"]) :
        i = s["homeworld"].rfind("/", 0, len(s["homeworld"]) - 1)
        j["homeworld"] = int(s["homeworld"][i+1:-1])
    j["name"] = s["name"]
    j["classification"] = s["classification"]
    j["average_height"] = s["average_height"]
    j["average_lifespan"] = s["average_lifespan"]
    j["language"] = s["language"]
    return jsonify({"species": j})

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

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

@app.route('/')
def home():
    return send_file('templates/index.html')

if __name__ == "__main__":
    app.run(debug=True)