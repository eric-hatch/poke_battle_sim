# File: hydrate_pokemon_team.py
# Name: Eric Hatch
#
# This file contains the implementation for the pokemon hydrating functions.


import pokemon

def team(team_base_data):
    team = []
    for poke in team_base_data:
        team.append(pokemon.Pokemon(poke['name'], poke['level']))
    return team



