# File: teams.py
# Name: Eric Hatch
#
# This file contains data for making the user and opponent teams.

import parse
import random

#############
# User Team #
#############
def get_user_team():
    print('Please enter the names of three pokemon that you want to fight with.')
    team = []
    pokemon1 = parse.poke_input('starting')
    team.append(pokemon1)
    pokemon2 = parse.poke_input('second')
    team.append(pokemon2)
    pokemon3 = parse.poke_input('third')
    team.append(pokemon3)
    print('\n')
    return team

#################
# Opponent Team #
#################
def get_random_poke():
    pokemon = {}
    poke_num = random.randint(0, 35)
    with open('data/movesets.txt') as f:
        movesets_lines = f.read().splitlines()
        pokemon['name'] = movesets_lines[poke_num * 6].upper()
    pokemon['level'] = random.randint(75, 100)
    return pokemon


def get_opponent_team():
    team = []
    for i in range(0, 3):
        team.append(get_random_poke())
    return team