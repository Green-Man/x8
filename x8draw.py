import os
import sys
import key_pressed

class X8draw(object):
    
    def __init__(self):
        pass
    
    def welcome(self, game):
        self.clear()
        
        print("Press Space to continue, h to help, x or q to exit")
        try:
            getKey = key_pressed._Getch()
            keyPressed = getKey()
            if keyPressed == " ":
                game.status = "ingame"
            elif keyPressed == "h":
                game.status = "help"
            elif keyPressed == "x" or keyPressed == "q":
                game.status = "exit"
            else:
                game.status = "init"
                self.welcome(game)
        except KeyboardInterrupt:
            game.status = "exit"
        
        return game.status
    
    def grid(self, game):
        shape = game.grid.shape
        getKey = key_pressed._Getch()
        while game.status == "ingame":
            self.clear()
            
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
            
            try:
                keyPressed = getKey()
                
                if keyPressed == "x" or keyPressed == "q":
                    self.clear()
                    sys.exit()
                elif keyPressed == "v":
                    game.spawn()
                    
                #here goes possibly not x-platform code of getting key values
                elif ord(keyPressed) == 27:
                    secondByte = ord(getKey())
                    if secondByte == 91:
                        thirdByte = ord(getKey())
                        if thirdByte==65:
                            game.move("up")
                        elif thirdByte==66:
                            game.move("down")
                        elif thirdByte==67:
                            game.move("right")
                        elif thirdByte==68:
                            game.move("left")
                
                self.grid(game)
                
            except KeyboardInterrupt:
                game.status = "exit"
                sys.exit()
            except Exception, e:
                raise e
                game.status = "exit"
    def help(self):
        self.clear()
        print("help screen")
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')