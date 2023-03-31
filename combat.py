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

        print("Type attaquant:", type_attaquant)
        print("Type defenseur:", type_defenseur)

        multiplicateurs = {
            "normal": {"normal": 1, "feu": 1, "eau": 1, "terre": 1, "plante": 1, "electrik": 1, "glace": 1, "combat": 1,
                       "poison": 1, "sol": 1, "vol": 1, "psy": 1, "insecte": 1, "roche": 0.5, "spectre": 0,
                       "dragon": 1},
            "feu": {"normal": 1, "feu": 0.5, "eau": 0.5, "terre": 1, "plante": 2, "electrik": 1, "glace": 2,
                    "combat": 1, "poison": 1, "sol": 1, "vol": 1, "psy": 1, "insecte": 2, "roche": 0.5, "spectre": 1,
                    "dragon": 0.5},
            "eau": {"normal": 1, "feu": 2, "eau": 0.5, "terre": 2, "plante": 0.5, "electrik": 1, "glace": 1,
                    "combat": 1, "poison": 1, "sol": 2, "vol": 1, "psy": 1, "insecte": 1, "roche": 2, "spectre": 1,
                    "dragon": 0.5},
            "terre": {"normal": 1, "feu": 2, "eau": 1, "terre": 1, "plante": 0.5, "electrik": 2, "glace": 1,
                      "combat": 1, "poison": 0.5, "sol": 1, "vol": 0, "psy": 1, "insecte": 0.5, "roche": 2,
                      "spectre": 1, "dragon": 1},
            "plante": {"normal": 1, "feu": 0.5, "eau": 2, "terre": 2, "plante": 0.5, "electrik": 1, "glace": 1,
                       "combat": 1, "poison": 0.5, "sol": 2, "vol": 0.5, "psy": 1, "insecte": 0.5, "roche": 2,
                       "spectre": 1, "dragon": 0.5},
            "electrik": {
                "normal": 1, "feu": 1, "eau": 2, "plante": 0.5, "electrik": 0.5, "glace": 1, "combat": 1, "poison": 1,
                "sol": 0, "vol": 2, "psy": 1, "insecte": 1, "roche": 1, "spectre": 1, "dragon": 0.5
            },
            "glace": {"normal": 1, "feu": 0.5, "eau": 0.5, "terre": 2, "plante": 2, "electrik": 1, "glace": 0.5,
                      "combat": 1, "poison": 1, "sol": 2, "vol": 2, "psy": 1, "insecte": 1, "roche": 1, "spectre": 1,
                      "dragon": 2},
            "combat": {"normal": 2, "feu": 1, "eau": 1, "terre": 1, "plante": 1, "electrik": 1, "glace": 2, "combat": 1,
                       "poison": 0.5, "sol": 1, "vol": 0.5, "psy": 0.5, "insecte": 0.5, "roche": 2, "spectre": 0,
                       "dragon": 1},
            "poison": {"normal": 1, "feu": 1, "eau": 1, "terre": 0.5, "plante": 2, "electrik": 1, "glace": 1,
                       "combat": 1, "poison": 0.5, "sol": 0.5, "vol": 1, "psy": 1, "insecte": 1, "roche": 0.5,
                       "spectre": 0.5, "dragon": 1},
            "sol": {"normal": 1, "feu": 2, "eau": 1, "terre": 1, "plante": 0.5, "electrik": 2, "glace": 1, "combat": 1,
                    "poison": 2, "sol": 1, "vol": 0, "psy": 1, "insecte": 0.5, "roche": 2, "spectre": 1, "dragon": 1},
            "vol": {"normal": 1, "feu": 1, "eau": 1, "terre": 1, "plante": 2, "electrik": 0.5, "glace": 1, "combat": 2,
                    "poison": 1, "sol": 1, "vol": 1, "psy": 1, "insecte": 2, "roche": 0.5, "spectre": 1, "dragon": 1},
            "psy": {"normal": 1, "feu": 1, "eau": 1, "terre": 1, "plante": 1, "electrik": 1, "glace": 1, "combat": 2,
                    "poison": 2, "sol": 1, "vol": 1, "psy": 0.5, "insecte": 1, "roche": 1, "spectre": 1, "dragon": 1},
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
