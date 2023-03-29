class Pokemon:
    def __init__(self, nom, niveau, attaque, defense, type_pokemon):
        self.__nom = nom
        self.__points_de_vie = 100
        self.niveau = niveau
        self.attaque = attaque
        self.defense = defense
        self.type_pokemon = type_pokemon

    def get_nom(self):
        return self.__nom

    def get_points_de_vie(self):
        return self.__points_de_vie

    def set_points_de_vie(self, points_de_vie):
        self.__points_de_vie = points_de_vie

    def afficher(self):
        return f"Nom: {self.__nom}, Points de vie: {self.__points_de_vie}, Attaque: {self.attaque}, Défense: {self.defense}, Type: {self.type_pokemon}"
