# File: pokemon.py
# Name: Eric Hatch
#
# This file contains Pokemon class data.

import parse
import math

class Pokemon:

    max_EV = 65535
    max_IV = 31

    def __init__(self, name, level):
        self.name = name
        self.level = level

        base_data = parse.base_poke_data(name)

        self.base_type1 = base_data['types']['type1']
        self.base_type2 = base_data['types']['type2']

        self.total_hp = Pokemon.calc_total_hp(base_data['stats']['hp'], level, Pokemon.max_EV, Pokemon.max_IV)
        self.atk = Pokemon.calc_stat(base_data['stats']['atk'], level, Pokemon.max_EV, Pokemon.max_IV)
        self.defs = Pokemon.calc_stat(base_data['stats']['defs'], level, Pokemon.max_EV, Pokemon.max_IV)
        self.spd = Pokemon.calc_stat(base_data['stats']['spd'], level, Pokemon.max_EV, Pokemon.max_IV)
        self.spc = Pokemon.calc_stat(base_data['stats']['spc'], level, Pokemon.max_EV, Pokemon.max_IV)

        self.curr_hp = self.total_hp
        self.evasion = 1
        self.accuracy = 1
        self.status = None

        moveset = parse.moveset(name)

        self.move1 = moveset[0].upper()
        self.move2 = moveset[1].upper()
        self.move3 = moveset[2].upper()
        self.move4 = moveset[3].upper()



    @staticmethod
    def calc_total_hp(base, level, ev, iv):
        return math.floor((((base + iv) * 2 + (math.sqrt(ev) / 4)) * level) / 100) + level + 10

    @staticmethod
    def calc_stat(base, level, ev, iv):
        return math.floor((((base + iv) * 2 + (math.sqrt(ev) / 4)) * level) / 100) + 5
