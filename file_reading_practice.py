# File: file_reading_practice.py
# Name: Eric Hatch
#
# This file is used to practice python file reading.

import os

def main():
    print('hello world')

    #looping through all the file names in the directory
    os.chdir('base_stats')
    for f in os.listdir():
        print(f)

        #opening a file
        with open('/Users/enchatch/Documents/Programming/git_repos/poke_battle_sim/base_stats/' + f, 'r') as poke_data:

            #iterating over lines
            for line in poke_data:
                print(line)

if __name__ == "__main__":
    main()