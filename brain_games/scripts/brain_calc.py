#!/usr/bin/env python3
from brain_games.games.game_even import welcome_user
from brain_games.games.game_calc import game_calc, welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    game_calc(name)


if __name__ == '__main__':
    main()