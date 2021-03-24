# File: parse.py
# Name: Eric Hatch
#
# This file contains parsing functions and formatting functions for user input data.

def is_valid_poke_input(string):
    tokens = string.split()

    if len(tokens) != 2:
        print('Input Error: not enough arguments')
        return False

    if int(tokens[1]) < 0 or int(tokens[1]) > 100:
        print('Input Error: not a valid level')
        return False

    with open('dex.txt') as dex:
        for line in dex:
            poke = line.split('_')
            if tokens[0].upper() == poke[1][: -1]:
                return True
    print('Input Error: not a valid pokemon')
    return False

def poke_input(num):
    poke_data = {}
    while True:
        pokemon = input('Enter the name and level of your ' + num + ' Pokemon: ')
        if is_valid_poke_input(pokemon):
            break
    tokens = pokemon.split()
    poke_data['name'] = tokens[0].upper()
    poke_data['level'] = tokens[1]
    return poke_data

