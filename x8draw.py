import os
import sys
import key_pressed

class X8draw(object):
    
    def __init__(self):
        pass
    
    def welcome(self, game):
        self.clear()
        
        print("Press Space to continue, h to help, x to exit")
        try:
            getKey = key_pressed._Getch()
            keyPressed = getKey()
            if keyPressed == " ":
                game.status = "ingame"
            elif keyPressed == "h":
                game.status = "help"
            elif keyPressed == "x":
                game.status = "exit"
            else:
                game.status = "init"
                self.welcome(game)
        except KeyboardInterrupt:
            game.status = "exit"
        
        return game.status
    
    def grid(self, game):
        self.clear()
        if game.status == "pass":
            print("miss key")
        print("GRID")
        getKey = key_pressed._Getch()
        while game.status == "ingame":
            try:
                keyPressed = getKey()
                
                if keyPressed == "x":
                    self.clear()
                    sys.exit()
                    
                #here goes possibly not x-platform code of getting key values
                elif ord(keyPressed) == 27:
                    secondByte = ord(getKey())
                    if secondByte == 91:
                        thirdByte = ord(getKey())
                        if thirdByte==65:
                                print "up"
                        elif thirdByte==66:
                                print "down"
                        elif thirdByte==67:
                                print "right"
                        elif thirdByte==68:
                                print "left"
#                 else:
#                     #game.status == "pass"
#                     self.grid(game)
            except KeyboardInterrupt:
                game.status = "exit"
                sys.exit()
            except Exception, e:
                game.status = "exit"
    def help(self):
        self.clear()
        print("help screen")
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')