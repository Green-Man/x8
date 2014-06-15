#!/usr/bin/python


import x8draw as drawer
import main

#import pydevd;pydevd.settrace()

draw = drawer.X8draw()
game = main.MainGame()


draw.welcome(game)

if game.status == "ingame":
    draw.grid(game)
elif game.status == "help":
    draw.help()
else:
    draw.clear()
