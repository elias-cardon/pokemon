from pokemon import Pokemon

class Normal(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Normal")

class Feu(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Feu")

class Eau(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Eau")

    def get_defense(self):
        return self.defense

class Terre(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Terre")

class Plante(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Plante")

class Electrik(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "électrik")

    def get_attaque(self):
        return self.attaque

class Glace(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Glace")

class Combat(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Combat")

class Poison(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Poison")

class Sol(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Sol")

class Vol(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Vol")

class Psy(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Psy")

class Insecte(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Insecte")

class Roche(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Roche")

class Spectre(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Spectre")

class Dragon(Pokemon):
    def __init__(self, nom, niveau, base_attaque, base_defense, iv_attaque=0, iv_defense=0, ev_attaque=0, ev_defense=0, nature_attaque=1, nature_defense=1):
        attaque = self.calculer_statistique(niveau, base_attaque, iv_attaque, ev_attaque, nature_attaque)
        defense = self.calculer_statistique(niveau, base_defense, iv_defense, ev_defense, nature_defense)
        super().__init__(nom, niveau, attaque, defense, "Dragon")