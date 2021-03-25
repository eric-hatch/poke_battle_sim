# File: ui.py
# Name: Eric Hatch
#
# This file contains functions that describe printouts of all kinds.

import math

def display_team(team, string, extra):
    print('-——' + string + ' TEAM——-')
    for i in range(len(team)):
        print('POKEMON #' + str(i) +': ' + team[i].name + ' Lvl.' + str(team[i].level))
        if extra:
            print('HP: ' + str(team[i].curr_hp) + ' / ' + str(team[i].total_hp))
            print('STATUS: ' + str(team[i].status))
    print('\n')

def sendout_message(user, pokemon):
    if user == True:
        print('Go ' + pokemon + '!')
    else:
        print('The anonymous trainer sent out ' + pokemon + '!')

###############
# Health Bars #
###############
def print_health_bar(pokemon):
    percent = pokemon.curr_hp / pokemon.total_hp
    num_blocks = math.floor(percent * 32)
    num_empty = 32 - num_blocks
    print(pokemon.name + '\'s HEALTH: |' + ('x' * num_blocks) + (' ' * num_empty) + '|')

def print_health(user_pokemon, opponent_pokemon):
    print('Anonymous Trainer\'s ' + opponent_pokemon.name + ':')
    print_health_bar(opponent_pokemon)
    print('Your ' + user_pokemon.name + ': ' + str(user_pokemon.curr_hp) + ' / ' + str(user_pokemon.total_hp) + 'HP')
    print_health_bar(user_pokemon)