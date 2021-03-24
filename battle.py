# File: battle.py
# Name: Eric Hatch
#
# This file contains data for the battle simulation.

import hydrate_pokemon

def is_valid_string(input):
    pass

def start_sequence():
    print('Welcome to the Pokemon Battle Simulator.')
    print('Please enter the names of three pokemon that you want to fight with.')
    pokemon1 = input("Enter the name and level of your first Pokemon: ")
    hydrate_pokemon.get_pokemon(pokemon1)
    pokemon2 = input("Enter the name and level of your second Pokemon: ")
    hydrate_pokemon.get_pokemon(pokemon2)
    pokemon3 = input("Enter the name and level of your third Pokemon: ")
    hydrate_pokemon.get_pokemon(pokemon3)


def battle():
    start_sequence()
