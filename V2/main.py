import pygame
from pygame.locals import *
import time
import math
import random
import requests
import io
from urllib.request import urlopen
from Move import Move
from Pokemon import Pokemon

pygame.init()

# create the game window
game_width = 500
game_height = 500
size = (game_width, game_height)
game = pygame.display.set_mode(size)
pygame.display.set_caption('Pokemon Battle')

# define colors
black = (0, 0, 0)
gold = (218, 165, 32)
grey = (200, 200, 200)
green = (0, 200, 0)
red = (200, 0, 0)
white = (255, 255, 255)

# game states
SELECT_POKEMON = 'select pokemon'
PREBATTLE = 'prebattle'
START_BATTLE = 'start battle'
PLAYER_TURN = 'player turn'
PLAYER_MOVE = 'player move'
RIVAL_TURN = 'rival turn'
FAINTED = 'fainted'
GAMEOVER = 'gameover'
QUIT = 'quit'

# button dimensions and positions
BUTTON_WIDTH = 240
BUTTON_HEIGHT = 70
FIGHT_BUTTON_POS = (10, 350)
POTION_BUTTON_POS = (250, 350)
MOVE_BUTTON_POS = [(10 + i % 2 * BUTTON_WIDTH, 350 + i // 2 * BUTTON_HEIGHT) for i in range(4)]


def display_message(message):
    # draw a white box with black border
    pygame.draw.rect(game, white, (10, 350, 480, 140))
    pygame.draw.rect(game, black, (10, 350, 480, 140), 3)

    # display the message
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    text = font.render(message, True, black)
    text_rect = text.get_rect()
    text_rect.x = 30
    text_rect.y = 410
    game.blit(text, text_rect)

    pygame.display.update()


def create_button(width, height, left, top, text_cx, text_cy, label):
    # position of the mouse cursor
    mouse_cursor = pygame.mouse.get_pos()

    button = Rect(left, top, width, height)

    # highlight the button if mouse is pointing to it
    if button.collidepoint(mouse_cursor):
        pygame.draw.rect(game, gold, button)
    else:
        pygame.draw.rect(game, white, button)

    # add the label to the button
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render(f'{label}', True, black)
    text_rect = text.get_rect(center=(text_cx, text_cy))
    game.blit(text, text_rect)

    return button


def handle_select_pokemon(mouse_click):
    global game_status, player_pokemon, rival_pokemon
    # check which pokemon was clicked on
    for i in range(len(pokemons)):
        if pokemons[i].get_rect().collidepoint(mouse_click):
            # assign the player's and rival's pokemon
            player_pokemon = pokemons[i]
            rival_pokemon = pokemons[(i + 1) % len(pokemons)]

            # lower the rival pokemon's level to make the battle easier
            rival_pokemon.level = int(rival_pokemon.level * .75)

            # set the coordinates of the hp bars
            player_pokemon.hp_x = 275
            player_pokemon.hp_y = 250
            rival_pokemon.hp_x = 50
            rival_pokemon.hp_y = 50

            game_status = PREBATTLE

def handle_player_turn(mouse_click):
    global game_status
    # check if fight button was clicked
    if fight_button.collidepoint(mouse_click):
        game_status = PLAYER_MOVE

    # check if potion button was clicked
    if potion_button.collidepoint(mouse_click):
        # force to attack if there are no more potions
        if player_pokemon.num_potions == 0:
            display_message('No more potions left')
            time.sleep(2)
            game_status = PLAYER_MOVE
        else:
            player_pokemon.use_potion()
            display_message(f'{player_pokemon.name} used potion')
            time.sleep(2)
            game_status = RIVAL_TURN

def handle_player_move(mouse_click):
    global game_status
    # check which move button was clicked
    for i in range(len(move_buttons)):
        button = move_buttons[i]

        if button.collidepoint(mouse_click):
            move = player_pokemon.moves[i]
            player_pokemon.perform_attack(rival_pokemon, move)

            # check if the rival's pokemon fainted
            if rival_pokemon.current_hp == 0:
                game_status = FAINTED
            else:
                game_status = RIVAL_TURN


# create the starter pokemons
level = 30
bulbasaur = Pokemon('Bulbasaur', level, 25, 150)
charmander = Pokemon('Charmander', level, 175, 150)
squirtle = Pokemon('Squirtle', level, 325, 150)
pokemons = [bulbasaur, charmander, squirtle]

# the player's and rival's selected pokemon
player_pokemon = None
rival_pokemon = None

# game loop
game_status = 'select pokemon'
while game_status != 'quit':

    for event in pygame.event.get():
        if event.type == QUIT:
            game_status = 'quit'

        # detect keypress
        if event.type == KEYDOWN:

            # play again
            if event.key == K_y:
                # reset the pokemons
                bulbasaur = Pokemon('Bulbasaur', level, 25, 150)
                charmander = Pokemon('Charmander', level, 175, 150)
                squirtle = Pokemon('Squirtle', level, 325, 150)
                pokemons = [bulbasaur, charmander, squirtle]
                game_status = 'select pokemon'

            # quit
            elif event.key == K_n:
                game_status = 'quit'

        # detect mouse click
        if event.type == MOUSEBUTTONDOWN:

            # coordinates of the mouse click
            mouse_click = event.pos

            # for selecting a pokemon
            if game_status == 'select pokemon':

                # check which pokemon was clicked on
                for i in range(len(pokemons)):

                    if pokemons[i].get_rect().collidepoint(mouse_click):
                        # assign the player's and rival's pokemon
                        player_pokemon = pokemons[i]
                        rival_pokemon = pokemons[(i + 1) % len(pokemons)]

                        # lower the rival pokemon's level to make the battle easier
                        rival_pokemon.level = int(rival_pokemon.level * .75)

                        # set the coordinates of the hp bars
                        player_pokemon.hp_x = 275
                        player_pokemon.hp_y = 250
                        rival_pokemon.hp_x = 50
                        rival_pokemon.hp_y = 50

                        game_status = 'prebattle'

            # for selecting fight or use potion
            elif game_status == 'player turn':

                # check if fight button was clicked
                if fight_button.collidepoint(mouse_click):
                    game_status = 'player move'

                # check if potion button was clicked
                if potion_button.collidepoint(mouse_click):

                    # force to attack if there are no more potions
                    if player_pokemon.num_potions == 0:
                        display_message('No more potions left')
                        time.sleep(2)
                        game_status = 'player move'
                    else:
                        player_pokemon.use_potion()
                        display_message(f'{player_pokemon.name} used potion')
                        time.sleep(2)
                        game_status = 'rival turn'

            # for selecting a move
            elif game_status == 'player move':

                # check which move button was clicked
                for i in range(len(move_buttons)):
                    button = move_buttons[i]

                    if button.collidepoint(mouse_click):
                        move = player_pokemon.moves[i]
                        player_pokemon.perform_attack(rival_pokemon, move)

                        # check if the rival's pokemon fainted
                        if rival_pokemon.current_hp == 0:
                            game_status = 'fainted'
                        else:
                            game_status = 'rival turn'

    # pokemon select screen
    if game_status == 'select pokemon':

        game.fill(white)

        # draw the starter pokemons
        bulbasaur.draw(game)
        charmander.draw(game)
        squirtle.draw(game)

        # draw box around pokemon the mouse is pointing to
        mouse_cursor = pygame.mouse.get_pos()
        for pokemon in pokemons:

            if pokemon.get_rect().collidepoint(mouse_cursor):
                pygame.draw.rect(game, black, pokemon.get_rect(), 2)

        pygame.display.update()

    # get moves from the API and reposition the pokemons
    if game_status == 'prebattle':
        # draw the selected pokemon
        game.fill(white)
        alpha = 255
        player_pokemon.draw(game, alpha)
        pygame.display.update()

        player_pokemon.set_moves()
        rival_pokemon.set_moves()

        # reposition the pokemons
        player_pokemon.x = -50
        player_pokemon.y = 100
        rival_pokemon.x = 250
        rival_pokemon.y = -50

        # resize the sprites
        player_pokemon.size = 300
        rival_pokemon.size = 300
        player_pokemon.set_sprite('back_default')
        rival_pokemon.set_sprite('front_default')

        game_status = 'start battle'

    # start battle animation
    if game_status == 'start battle':

        # rival sends out their pokemon
        alpha = 0
        while alpha < 255:
            game.fill(white)
            rival_pokemon.draw(game, alpha)
            display_message(f'Rival sent out {rival_pokemon.name}!')
            alpha += .4

            pygame.display.update()

        # pause for 1 second
        time.sleep(1)

        # player sends out their pokemon
        alpha = 0
        while alpha < 255:
            game.fill(white)
            player_pokemon.draw(game, alpha)
            rival_pokemon.draw(game, alpha)
            display_message(f'Go {player_pokemon.name}!')
            alpha += .4

            pygame.display.update()

        # draw the hp bars
        player_pokemon.draw_hp(game)
        rival_pokemon.draw_hp(game)

        # determine who goes first
        if rival_pokemon.speed > player_pokemon.speed:
            game_status = 'rival turn'
        else:
            game_status = 'player turn'

        pygame.display.update()

        # pause for 1 second
        time.sleep(1)

    # display the fight and use potion buttons
    if game_status == 'player turn':
        game.fill(white)
        player_pokemon.draw(game)
        rival_pokemon.draw(game)
        player_pokemon.draw_hp(game)
        rival_pokemon.draw_hp(game)

        # create the fight and use potion buttons
        fight_button = create_button(240, 140, 10, 350, 130, 412, 'Fight')
        potion_button = create_button(240, 140, 250, 350, 370, 412, f'Use Potion ({player_pokemon.num_potions})')

        # draw the black border
        pygame.draw.rect(game, black, (10, 350, 480, 140), 3)

        pygame.display.update()

    # display the move buttons
    if game_status == 'player move':

        game.fill(white)
        player_pokemon.draw(game)
        rival_pokemon.draw(game)
        player_pokemon.draw_hp(game)
        rival_pokemon.draw_hp(game)

        # create a button for each move
        move_buttons = []
        for i in range(len(player_pokemon.moves)):
            move = player_pokemon.moves[i]
            button_width = 240
            button_height = 70
            left = 10 + i % 2 * button_width
            top = 350 + i // 2 * button_height
            text_center_x = left + 120
            text_center_y = top + 35
            button = create_button(button_width, button_height, left, top, text_center_x, text_center_y,
                                   move.name.capitalize())
            move_buttons.append(button)

        # draw the black border
        pygame.draw.rect(game, black, (10, 350, 480, 140), 3)

        pygame.display.update()

    # rival selects a random move to attack with
    if game_status == 'rival turn':

        game.fill(white)
        player_pokemon.draw(game)
        rival_pokemon.draw(game)
        player_pokemon.draw_hp(game)
        rival_pokemon.draw_hp(game)

        # empty the display box and pause for 2 seconds before attacking
        display_message('')
        time.sleep(2)

        # select a random move
        move = random.choice(rival_pokemon.moves)
        rival_pokemon.perform_attack(player_pokemon, move)

        # check if the player's pokemon fainted
        if player_pokemon.current_hp == 0:
            game_status = 'fainted'
        else:
            game_status = 'player turn'

        pygame.display.update()

    # one of the pokemons fainted
    if game_status == 'fainted':

        alpha = 255
        while alpha > 0:

            game.fill(white)
            player_pokemon.draw_hp(game)
            rival_pokemon.draw_hp(game)

            # determine which pokemon fainted
            if rival_pokemon.current_hp == 0:
                player_pokemon.draw(game, alpha)
                rival_pokemon.draw(game, alpha)
                display_message(f'{rival_pokemon.name} fainted!')
            else:
                player_pokemon.draw(alpha)
                rival_pokemon.draw(game, alpha)
                display_message(f'{player_pokemon.name} fainted!')
            alpha -= .4

            pygame.display.update()

        game_status = 'gameover'

    # gameover screen
    if game_status == 'gameover':
        display_message('Play again (Y/N)?')

pygame.quit()