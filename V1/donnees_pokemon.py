from types_pokemon import Normal, Feu, Eau, Terre, Plante, Electrik, Glace, Combat, Poison, Sol, Vol, Psy, Insecte, Roche, Spectre, Dragon

# Les Pokémon de la première génération sont représentés sous la forme d'une liste
# d'instances de Pokémon avec les attributs suivants :
# 1. Nom du Pokémon (chaîne de caractères)
# 2. Niveau du Pokémon (entier)
# 3. Puissance d'attaque du Pokémon (entier)
# 4. Défense du Pokémon (entier)
pokemons_premiere_generation = [
    Plante("Bulbizarre", 5, 49, 49),
    Plante("Herbizarre", 16, 62, 63),
    Plante("Florizarre", 32, 82, 83),
    Feu("Salamèche", 5, 52, 43),
    Feu("Reptincel", 16, 64, 58),
    Feu("Dracaufeu", 36, 84, 78),
    Eau("Carapuce", 5, 48, 65),
    Eau("Carabaffe", 16, 63, 80),
    Eau("Tortank", 36, 83, 100),
    Insecte("Chenipan", 1, 30, 35),
    Insecte("Chrysacier", 7, 20, 55),
    Insecte("Papilusion", 10, 45, 50),
    Insecte("Aspicot", 1, 35, 30),
    Insecte("Coconfort", 7, 25, 50),
    Insecte("Dardargnan", 10, 90, 40),
    Normal("Roucool", 1, 45, 40),
    Normal("Roucoups", 18, 60, 55),
    Normal("Roucarnage", 36, 80, 75),
    Normal("Rattata", 1, 56, 35),
    Normal("Rattatac", 20, 81, 60),
    Normal("Piafabec", 1, 60, 30),
    Normal("Rapasdepic", 20, 90, 65),
    Normal("Abo", 1, 60, 44),
    Poison("Arbok", 22, 95, 69),
    Electrik("Pikachu", 5, 55, 40),
    Electrik("Raichu", 20, 90, 55),
    Sol("Sabelette", 1, 75, 85),
    Sol("Sablaireau", 22, 100, 110),
    Normal("Nidoran♀", 1, 47, 52),
    Poison("Nidorina", 16, 62, 67),
    Poison("Nidoqueen", 16, 92, 87),
    Normal("Nidoran♂", 1, 57, 40),
    Poison("Nidorino", 16, 72, 57),
    Poison("Nidoking", 16, 102, 77),
    Psy("Melo", 1, 45, 48),
    Psy("Melodelfe", 28, 70, 73),
    Vol("Goupix", 1, 41, 40),
    Feu("Feunard", 32, 76, 75),
    Normal("Ronflex", 1, 110, 65),
    Normal("Evoli", 1, 55, 50),
    Electrik("Voltali", 1, 65, 60),
    Eau("Aquali", 1, 65, 60),
    Feu("Pyroli", 1, 130, 60),
    Normal("Porygon", 1, 60, 70),
    Normal("Amonita", 1, 40, 100),
    Roche("Amonistar", 40, 60, 125),
    Normal("Kabuto", 1, 80, 90),
    Roche("Kabutops", 40, 115, 105),
    Terre("Ptéra", 1, 105, 65),
    Psy("Mewtwo", 70, 110, 90),
    Psy("Mew", 1, 100, 100),
    Terre("Onix", 1, 45, 160),
    Insecte("Dardagnan", 10, 90, 40),
    Poison("Nidoking", 16, 102, 77),
    Psy("Melo", 1, 45, 48),
    Psy("Melodelfe", 28, 70, 73),
    Glace("Givrali", 1, 60, 110),
    Insecte("Papilusion", 10, 45, 50),
    Vol("Roucarnage", 36, 80, 75),
    Normal("Rattatac", 20, 81, 60),
    Electrik("Elektek", 1, 83, 57),
    Insecte("Aéromite", 1, 60, 65),
    Roche("Rhinoféros", 1, 85, 95),
    Roche("Rhinastoc", 42, 135, 120),
    Insecte("Scarabrute", 25, 125, 100),
    Glace("Lokhlass", 1, 85, 80),
    Spectre("Ectoplasma", 25, 65, 60),
    Spectre("Spectrum", 1, 50, 45),
    Spectre("Fantominus", 1, 35, 30),
    Roche("Aéroptéryx", 1, 105, 65),
    Dragon("Dracolosse", 55, 134, 95),
    Dragon("Draco", 30, 64, 45),
    Dragon("Minidraco", 10, 41, 40),
    Eau("Léviator", 20, 125, 79),
    Eau("Magicarpe", 1, 10, 55),
    Eau("Akwakwak", 33, 82, 78),
    Eau("Psykokwak", 1, 52, 48),
    Combat("Mackogneur", 28, 130, 80),
    Combat("Machopeur", 28, 100, 70),
    Combat("Machoc", 1, 80, 50),
    Eau("Tentacruel", 30, 70, 65),
    Eau("Tentacool", 1, 50, 100),
    Eau("Staross", 28, 100, 85),
    Eau("Stari", 1, 45, 55),
    Electrik("Magnéton", 30, 60, 95),
    Electrik("Magnéti", 1, 35, 70),
    Vol("Dodrio", 31, 110, 70),
    Vol("Doduo", 1, 85, 45),
    Psy("Lippoutou", 38, 70, 75),
    Psy("Lippouti", 1, 45, 48),
    Insecte("Mimitoss", 1, 25, 50),
    Insecte("Morphéo", 10, 90, 89),
    Poison("Smogogo", 35, 90, 120),
    Poison("Smogo", 1, 65, 95),
    Sol("Tadmorv", 1, 80, 50),
    Poison("Grotadmorv", 38, 105, 75),
    Roche("Grolem", 25, 120, 130),
    Roche("Gravalanch", 1, 95, 115),
    Roche("Racaillou", 1, 80, 100),
    Plante("Saquedeneu", 1, 100, 60),
    Plante("Boustiflor", 1, 65, 70),
    Plante("Ortide", 21, 80, 85),
    Psy("Alakazam", 16, 50, 45),
    Psy("Kadabra", 16, 35, 30),
    Psy("Abra", 1, 20, 15),
    Eau("Flagadoss", 2, 75, 110),
    Eau("Ramoloss", 1, 65, 65),
    Eau("Poissoroy", 33, 92, 67),
    Eau("Poissirène", 1, 52, 67),
    Electrik("Raikou", 1, 85, 75),
    Eau("Tygnon", 20, 105, 79),
    Combat("Kicklee", 1, 120, 53),
    Glace("Artikodin", 1, 85, 100),
    Electrik("Electhor", 1, 90, 85),
    Feu("Sulfura", 1, 100, 90),
    Eau("Krabboss", 28, 130, 115),
    Eau("Krabby", 1, 105, 90),
]