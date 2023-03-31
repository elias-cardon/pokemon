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
            "Normal": {"Normal": 1, "Feu": 1, "Eau": 1, "Terre": 1, "Plante": 1, "Electrik": 1, "Glace": 1, "Combat": 1,
                       "Poison": 1, "Sol": 1, "Vol": 1, "Psy": 1, "Insecte": 1, "Roche": 0.5, "Spectre": 0,
                       "Dragon": 1},
            "Feu": {"Normal": 1, "Feu": 0.5, "Eau": 0.5, "Terre": 1, "Plante": 2, "Electrik": 1, "Glace": 2,
                    "Combat": 1, "Poison": 1, "Sol": 1, "Vol": 1, "Psy": 1, "Insecte": 2, "Roche": 0.5, "Spectre": 1,
                    "Dragon": 0.5},
            "Eau": {"Normal": 1, "Feu": 2, "Eau": 0.5, "Terre": 2, "Plante": 0.5, "Electrik": 1, "Glace": 1,
                    "Combat": 1, "Poison": 1, "Sol": 2, "Vol": 1, "Psy": 1, "Insecte": 1, "Roche": 2, "Spectre": 1,
                    "Dragon": 0.5},
            "Terre": {"Normal": 1, "Feu": 2, "Eau": 1, "Terre": 1, "Plante": 0.5, "Electrik": 2, "Glace": 1,
                      "Combat": 1, "Poison": 0.5, "Sol": 1, "Vol": 0, "Psy": 1, "Insecte": 0.5, "Roche": 2,
                      "Spectre": 1, "Dragon": 1},
            "Plante": {"Normal": 1, "Feu": 0.5, "Eau": 2, "Terre": 2, "Plante": 0.5, "Electrik": 1, "Glace": 1,
                       "Combat": 1, "Poison": 0.5, "Sol": 2, "Vol": 0.5, "Psy": 1, "Insecte": 0.5, "Roche": 2,
                       "Spectre": 1, "Dragon": 0.5},
            "électrik": {
                "normal": 1, "feu": 1, "eau": 2, "plante": 0.5, "électrik": 0.5, "glace": 1, "combat": 1, "poison": 1,
                "sol": 0, "vol": 2, "psy": 1, "insecte": 1, "roche": 1, "spectre": 1, "dragon": 0.5
            },
            "Glace": {"Normal": 1, "Feu": 0.5, "Eau": 0.5, "Terre": 2, "Plante": 2, "Electrik": 1, "Glace": 0.5,
                      "Combat": 1, "Poison": 1, "Sol": 2, "Vol": 2, "Psy": 1, "Insecte": 1, "Roche": 1, "Spectre": 1,
                      "Dragon": 2},
            "Combat": {"Normal": 2, "Feu": 1, "Eau": 1, "Terre": 1, "Plante": 1, "Electrik": 1, "Glace": 2, "Combat": 1,
                       "Poison": 0.5, "Sol": 1, "Vol": 0.5, "Psy": 0.5, "Insecte": 0.5, "Roche": 2, "Spectre": 0,
                       "Dragon": 1},
            "Poison": {"Normal": 1, "Feu": 1, "Eau": 1, "Terre": 0.5, "Plante": 2, "Electrik": 1, "Glace": 1,
                       "Combat": 1, "Poison": 0.5, "Sol": 0.5, "Vol": 1, "Psy": 1, "Insecte": 1, "Roche": 0.5,
                       "Spectre": 0.5, "Dragon": 1},
            "Sol": {"Normal": 1, "Feu": 2, "Eau": 1, "Terre": 1, "Plante": 0.5, "Electrik": 2, "Glace": 1, "Combat": 1,
                    "Poison": 2, "Sol": 1, "Vol": 0, "Psy": 1, "Insecte": 0.5, "Roche": 2, "Spectre": 1, "Dragon": 1},
            "Vol": {"Normal": 1, "Feu": 1, "Eau": 1, "Terre": 1, "Plante": 2, "Electrik": 0.5, "Glace": 1, "Combat": 2,
                    "Poison": 1, "Sol": 1, "Vol": 1, "Psy": 1, "Insecte": 2, "Roche": 0.5, "Spectre": 1, "Dragon": 1},
            "Psy": {"Normal": 1, "Feu": 1, "Eau": 1, "Terre": 1, "Plante": 1, "Electrik": 1, "Glace": 1, "Combat": 2,
                    "Poison": 2, "Sol": 1, "Vol": 1, "Psy": 0.5, "Insecte": 1, "Roche": 1, "Spectre": 1, "Dragon": 1},
        }

        return multiplicateurs[type_attaquant][type_defenseur]

    def infliger_degats(self, attaquant, defenseur):
        multiplicateur = self.get_multiplicateur(attaquant, defenseur)
        degats = attaquant.get_attaque() * multiplicateur - defenseur.get_defense()
        degats = max(degats, 0)
        defenseur.set_points_de_vie(defenseur.get_points_de_vie() - degats)
        print(
            f"{self.pokemon1.nom} inflige {degats} points de dégâts à {self.pokemon2.nom} ({multiplicateur}x multiplicateur)")

    def perdant(self):
        if self.est_mort(self.pokemon1):
            return self.pokemon1.get_nom()
        elif self.est_mort(self.pokemon2):
            return self.pokemon2.get_nom()
        else:
            return None
