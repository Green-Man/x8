#!/usr/bin/python
import sys

import x8draw as drawer
import main

if len(sys.argv) > 1:
    if sys.argv[1] == "-d":
        import pydevd;pydevd.settrace()

draw = drawer.X8draw()
game = main.MainGame()


#draw.welcome(game)

if game.status == "ingame":
    draw.grid(game)
else:
    #draw.grid(game, waitInput = False)
    print("You lose. Looser!")
