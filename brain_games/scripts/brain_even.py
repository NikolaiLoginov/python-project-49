#!/usr/bin/env python3
from brain_games.game_even import game_even, is_even, welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    game_even(name)


if __name__ == '__main__':
    main()
