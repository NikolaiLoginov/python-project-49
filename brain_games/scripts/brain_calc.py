#!/usr/bin/env python3
from brain_games.games.game_calc import get_question, QUESTION_TEXT
from brain_games.engine import launch_game


def main():
    launch_game(get_question, QUESTION_TEXT)


if __name__ == '__main__':
    main()
