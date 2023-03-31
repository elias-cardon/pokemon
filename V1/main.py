from combat import Combat
from donnees_pokemon import pokemons_premiere_generation

def menu():
    while True:
        print("\nMenu principal :")
        print("1. Lancer une partie")
        print("2. Quitter")

        choix = int(input("Entrez votre choix : "))

        if choix == 1:
            pokemon1, pokemon2 = choisir_pokemon()
            combat = Combat(pokemon1, pokemon2)
            while combat.vainqueur() is None:
                combat.infliger_degats(pokemon1, pokemon2)
                combat.infliger_degats(pokemon2, pokemon1)
            print(f"Le vainqueur est {combat.vainqueur()}!")
        elif choix == 2:
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def choisir_pokemon():
    print("Choisissez deux Pokémon pour combattre :")
    for index, pokemon in enumerate(pokemons_premiere_generation):
        print(f"{index + 1}. {pokemon.nom}")

    choix1 = int(input("Entrez le numéro du premier Pokémon : ")) - 1
    choix2 = int(input("Entrez le numéro du deuxième Pokémon : ")) - 1

    return pokemons_premiere_generation[choix1], pokemons_premiere_generation[choix2]

if __name__ == "__main__":
    menu()
