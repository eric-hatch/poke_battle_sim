# File: hydrate_pokemon.py
# Name: Eric Hatch
#
# This file contains the implementation for the pokemon hydrating functions.

import pokemon
import os

def get_poke_name(line):
    token_list = line.split()
    return token_list[1][4:]

def parse_stats(stat_line):
    tokens = stat_line.split()
    stats = {}
    stats['hp'] = tokens[1][: -1]
    stats['atk'] = tokens[2][: -1]
    stats['defs'] = tokens[3][: -1]
    stats['spd'] = tokens[4][: -1]
    stats['spc'] = tokens[5]
    return stats

def parse_types(type_line):
    tokens = type_line.split()
    types = {}
    types['type1'] = tokens[1][: -1]
    types['type2'] = tokens[2]
    return types

def parse_poke_data(poke_name):
    poke_dict = {}
    os.chdir('base_stats')
    for f in os.listdir():
        with open(f, 'r') as poke_data:
            topline = poke_data.readline()
            poke = get_poke_name(topline)
            if poke == poke_name:
                lines = poke_data.read().splitlines()
                poke_dict['stats'] = parse_stats(lines[1])
                poke_dict['types'] = parse_types(lines[4])
                break
    os.chdir('..')
    return poke_dict

def get_pokemon(poke_string):
    poke_data = parse_poke_data(poke_string)
    print(poke_data)
    return poke_data


