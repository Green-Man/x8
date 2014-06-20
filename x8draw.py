import os
import sys
import key_pressed
from wx import GetKeyState

class X8draw(object):
    
    def __init__(self):
        pass
    
    def grid(self, game, waitInput=True):
        self.clear()
        shape = game.grid.shape
        for y in range(shape[1]*4+1):
            if y % 4 == 0:
                print("# "*(4*(shape[0])+1)) #horizontal continuous line
            elif (y+1) % 4 == 0 or (y-1) % 4 == 0:
                row = ("#"+7*" ")*shape[0]+"#"
                print(row) #horizontal row with spaces only
            else:
                row = []
                for x in range((shape[0])):
                    number = str(game.grid[x][(y/4)])
                    l = len(number)
                    even = int(l%2 ==0)
                    row.append("#"+((7-l)/2+even)*" "+number+(7-l)/2*" ")
                print("".join(row)+"#")
        
        getKey = None
        if waitInput:
            getKey = key_pressed._Getch()
        while game.status == "ingame" and getKey:
            keyPressed = getKey()
            if keyPressed == "x" or keyPressed == "q":
                self.clear()
                sys.exit()
            #here goes possibly not x-platform code of getting key values
            elif ord(keyPressed) == 27:
                secondByte = ord(getKey())
                if secondByte == 91:
                    thirdByte = ord(getKey())
                    if thirdByte==65:
                        game.move((0,-1))
                    elif thirdByte==66:
                        game.move((0,1))
                    elif thirdByte==67:
                        game.move((1,0))
                    elif thirdByte==68:
                        game.move((-1,0))
            self.grid(game)
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')