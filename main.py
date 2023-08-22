"""
Starts the game
"""

import sys

from TheGame import TheGame


def main():
    the_game = TheGame()
    if sys.argv[0] == "main.py" and len(sys.argv) == 1:
        print("No starting command entered")
        return 0
    if len(sys.argv) == 1:
        the_game.game_loop()
    if sys.argv[0] == "main.py" and len(sys.argv) <= 3:
        if len(sys.argv) > 3:
            print("too many arguments")
            return 0
        if f"{sys.argv[1]}".lower() == "start":
            the_game.game_loop()


if __name__ == '__main__':
    main()
