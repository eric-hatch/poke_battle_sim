# File: battle.py
# Name: Eric Hatch
#
# This file contains data for the battle simulation.

import hydrate
import ui
import teams


def battle(user, opponent):
    num_alive_user = len(user)
    num_alive_opponent = len(opponent)
    curr_user_pokemon = user[0]
    curr_opponent_pokemon = opponent[0]

    print('An anonymous trainer has challenged you to a battle!')
    ui.sendout_message(False, opponent[0].name)
    ui.sendout_message(True, user[0].name)

    while True:
        print('\n')
        ui.print_health(curr_user_pokemon, curr_opponent_pokemon)
        command = input('| Fight | Pokemon | Quit | : ')
        if command == 'Quit':
            break
        if command == 'Pokemon':
            ui.display_team(user, 'YOUR', True)
            while True:
                input('What pokemon do you want to switch to? (or type \'back\'): ')
        if command == 'Fight':
            break


def main():
    print('Welcome to the Pokemon Battle Simulator!')
    print('\n')
    user_team = hydrate.team(teams.get_user_team())
    opponent_team = hydrate.team(teams.get_opponent_team())
    ui.display_team(user_team, 'YOUR', False)
    ui.display_team(opponent_team, 'OPPONENT\'s', False)
    battle(user_team, opponent_team)
    print('Thanks for playing the Pokemon Battle Simulator. Shutting down...')


if __name__ == "__main__":
    main()