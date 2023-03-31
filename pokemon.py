import math
class Pokemon:
    def __init__(self, nom, niveau, attaque, defense, type_pokemon=None):
        self._nom = nom
        self._points_de_vie = 100
        self.niveau = niveau
        self.attaque = attaque
        self.defense = defense
        self.type_pokemon = type_pokemon

    @property
    def nom(self):
        return self._nom

    def get_points_de_vie(self):
        return self._points_de_vie

    def get_nom(self):
        return self.__nom

    def set_points_de_vie(self, points_de_vie):
        self.__points_de_vie = points_de_vie

    def afficher(self):
        return f"Nom: {self.__nom}, Points de vie: {self.__points_de_vie}, Attaque: {self.attaque}, Défense: {self.defense}, Type: {self.type_pokemon}"

    def calculer_degats(self, adversaire, puissance, multiplicateur):
        niveau = self.niveau
        attaque = self.attaque
        defense = adversaire.defense

        degats = ((((2 * niveau / 5 + 2) * puissance * attaque / defense) / 50) + 2) * multiplicateur
        return degats

    def calculer_statistique(self, niveau, base_stat, iv, ev, nature):
        return math.floor((((base_stat * 2 + iv + math.floor(ev / 4)) * niveau) / 100 + 5) * nature)