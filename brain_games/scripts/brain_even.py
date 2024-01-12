#!/usr/bin/env python3
from brain_games.games.game_even import game_even, welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    game_even(name)


if __name__ == '__main__':
    main()
