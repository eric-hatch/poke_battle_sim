# File: parse.py
# Name: Eric Hatch
#
# This file contains parsing functions and formatting functions for user input data.

import os

######################
# POKEMON INPUT DATA #
######################
def is_valid_poke_input(string):
    tokens = string.split()

    if len(tokens) != 2:
        print('Input Error: not enough arguments')
        return False

    if int(tokens[1]) < 0 or int(tokens[1]) > 100:
        print('Input Error: not a valid level')
        return False

    with open('data/dex.txt') as dex:
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
    poke_data['level'] = int(tokens[1])

    return poke_data

######################
# BASE POKEMON DATA #
######################

def name_tokens(line):
    token_list = line.split()
    return token_list[1][4:]

def base_stats(stat_line):
    tokens = stat_line.split()
    stats = {}
    stats['hp'] = int(tokens[1][: -1])
    stats['atk'] = int(tokens[2][: -1])
    stats['defs'] = int(tokens[3][: -1])
    stats['spd'] = int(tokens[4][: -1])
    stats['spc'] = int(tokens[5])
    return stats

def types(type_line):
    tokens = type_line.split()
    types = {}
    types['type1'] = tokens[1][: -1]
    types['type2'] = tokens[2]
    return types

def base_poke_data(input_poke_name):
    poke_dict = {}
    os.chdir('data/base_stats')
    for f in os.listdir():
        with open(f, 'r') as base_poke_data:
            top_line = base_poke_data.readline()
            parsed_poke_name = name_tokens(top_line)
            if parsed_poke_name == input_poke_name:
                poke_dict['name'] = parsed_poke_name
                poke_data_lines = base_poke_data.read().splitlines()
                poke_dict['stats'] = base_stats(poke_data_lines[1])
                poke_dict['types'] = types(poke_data_lines[4])
                break
    os.chdir('..')
    os.chdir('..')
    return poke_dict

#########
# MOVES #
#########

def moveset(name):
    moveset = []
    with open('data/movesets.txt') as f:
        for line in f:
            upper_line = line.upper()
            if upper_line[:len(name)] == name:
                for i in range(4):
                    move_tokens = f.readline().split('- ')
                    moveset.append(move_tokens[1][: -1])
                return moveset
    print(name + ' does not have a moveset yet. Sorry about that!')
    exit()

if __name__ == "__main__":
    moveset('ALAKAZAM')
