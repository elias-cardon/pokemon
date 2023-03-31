import pygame
from pygame.locals import *
import time
import math
import random
import requests
import io
from urllib.request import urlopen

pygame.init()

#Création de la fenêtre de jeu
game_width = 500
game_height = 500
size = (game_height, game_width)
game = pygame.display.set_mode(size)
pygame.display.set_caption('Combat Pokémon')

#Définition des couleurs
black = (0, 0, 0)
gold = (218, 165, 32)
grey = (200, 200, 200)
green = (0, 200, 0)
red = (200, 0 ,0)
white = (255, 255, 255)

#game loop
game_status = 'Choisir un Pokémon'
while game_status != 'quit':
    for event in pygame.event.get():
        if event.type == QUIT:
            game_status = 'quit'

pygame.quit()