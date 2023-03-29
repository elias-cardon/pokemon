class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def est_mort(self, pokemon):
        return pokemon.get_points_de_vie() <= 0

    def vainqueur(self):
        if self.est_mort(self.pokemon1):
            return self.pokemon2.get_nom()
        elif self.est_mort(self.pokemon2):
            return self.pokemon1.get_nom()
        else:
            return None

    def get_multiplicateur(self, attaquant, defenseur):
        type_attaquant = attaquant.type_pokemon.lower()
        type_defenseur = defenseur.type_pokemon.lower()

        multiplicateurs = {
            "eau": {"eau": 1, "feu": 2, "terre": 0.5, "normal": 1},
            "feu": {"eau": 0.5, "feu": 1, "terre": 2, "normal": 1},
            "terre": {"eau": 2, "feu": 0.5, "terre": 1, "normal": 1},
            "normal": {"eau": 0.75, "feu": 0.75, "terre": 0.75, "normal": 1},
        }

        return multiplicateurs[type_attaquant][type_defenseur]

    def infliger_degats(self, attaquant, defenseur):
        multiplicateur = self.get_multiplicateur(attaquant, defenseur)
        degats = attaquant.attaque * multiplicateur - defenseur.defense
        defenseur.set_points_de_vie(defenseur.get_points_de_vie() - max(degats, 0))

    def perdant(self):
        if self.est_mort(self.pokemon1):
            return self.pokemon1.get_nom()
        elif self.est_mort(self.pokemon2):
            return self.pokemon2.get_nom()
        else:
            return None
