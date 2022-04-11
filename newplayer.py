#!/usr/bin/env python3

import sys
import time
import os


def clear():
    os.system('clear')


def type_delay(char, delay=0.1):
    for l in char:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(delay)


def newPlayer():
    crsr = "> "
    # ask the player for input of their name
    clear()

    player = input(
        f"{crsr}Welcome vagabond, what is thy name? \n\n{crsr}").strip().title()

    # print("")
    for char in player:
        type_delay(char)

    print(", welcome to the Game of Dragons!")
    # print(type(player))
    return player
