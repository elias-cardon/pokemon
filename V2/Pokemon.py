import pygame
from pygame.locals import *
import time
import math
import random
import requests
import io
from urllib.request import urlopen

#Base URL de l'API pokémon
base_url = 'https://pokeapi.co/api/v2'
class Pokemon(pygame.sprite.Sprite):

    def __init__(self, name, level, x, y):
        pygame.sprite.Sprite.__init__(self)

        #Appel de l'API endpoint
        req = requests.get(f'{base_url}/pokemon/{name.lower()}')
        self.json = req.json()

        #on set le nom du pokémon et le niveau
        self.name = name
        self.level = level

        #on set la position du pokémon sur l'écran
        self.x = x
        self.y = y

        #nombre de potions restant
        self.num_potions = 3

        #On récupère les stats du pokémon via l'API
        stats = self.json['stats']
        for stat in stats:
            if stat['stat']['name'] == 'hp':
                self.current_hp = stat['base_stat'] + self.level
                self.max_hp = stat['base_stat'] + self.level
            elif stat['stat']['name'] == 'attack':
                self.attack = stat['base_stat']
            elif stat['stat']['name'] == 'defense':
                self.defense = stat['base_stat']
            elif stat['stat']['name'] == 'speed':
                self.speed = stat['base_stat']

        #On set le type du pokémon
        self.types = []
        for i in range(len(self.json['types'])):
            type = self.json['types'][i]
            self.types.append(type['types']['name'])

        #On set la largeur du sprite
        self.size = 150

        # On set le devant du sprite
        self.set_sprite('front_default')

    def set_sprite(self, side):
        # On set le sprite du pokémon
        image = self.json['sprites'][side]
        image_stream = urlopen(image)