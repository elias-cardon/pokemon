from pokemon import Pokemon

class Normal(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "normal")

class Feu(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "feu")

class Eau(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "eau")

    def get_defense(self):
        return self.defense

class Terre(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "terre")

class Plante(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "plante")

class Electrik(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "electrik")

    def get_attaque(self):
        return self.attaque

class Glace(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "glace")

class Combat(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "combat")

class Poison(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "poison")

class Sol(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "sol")

class Vol(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "vol")

class Psy(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "psy")

class Insecte(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "insecte")

class Roche(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "roche")

class Spectre(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "spectre")

class Dragon(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "dragon")