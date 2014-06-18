import numpy as np
import time

class MainGame(object):
    def __init__(self):
        self.dim = 2
        self.size = 4
        self.status = "init"
        
        shape = [self.size for x in xrange(self.dim)]
        self.grid = np.zeros(shape, dtype=Cell)
        
        for y in xrange(self.size):
            for x in xrange(self.size):
                self.grid[x,y] = Cell(0)
        
        self.spawn()
        self.spawn()
    
    
    def spawn(self):
        emptyCells = []
        iterator = np.nditer(self.grid, flags=["multi_index", "refs_ok"])
        while not iterator.finished:
            if iterator[0].item().get() == 0:
                emptyCells.append(iterator.multi_index)
            iterator.iternext()
        if len(emptyCells):
            cellToFill = emptyCells[np.random.randint(len(emptyCells))]
            newCell = Cell(2)
            self.grid[cellToFill] = newCell
    
    
    def move(self, direction):
        self.setUpdated(False)
        
        #Up case
        d = np.array((0, -1))
        for x in xrange(self.size):
            for y in xrange(self.size):
                pos = (x,y)
                if not self.grid[pos].updated:
                    value = self.grid[pos].get()
                    nextNonZero = self.trace(pos, -d)
                    if nextNonZero:
                        #print("%s -> %s" % (pos, nextNonZero))
                        if value:
                            #print("\t%s + %s" % (str(self.grid[pos].get()), str(self.grid[nextNonZero].get())))
                            if self.grid[nextNonZero].get() == self.grid[pos].get():
                                self.grid[pos].double()
                                self.grid[nextNonZero] = Cell(0)
                            else:
                                nextPos = self.nextPos(pos, -d)
                                if self.grid[nextPos] is self.grid[nextNonZero]:
                                    self.grid[nextPos].updated = True
                                else:
                                    self.grid[nextPos] = self.grid[nextNonZero]
                                    self.grid[nextPos].updated = True
                                    self.grid[nextNonZero] = Cell(0)
                        else:
                            self.grid[pos] = self.grid[nextNonZero]
                            self.grid[nextNonZero] = Cell(0)
                    
        #raw_input()
        time.sleep(0.1)
    
    
    def nextPos(self, p,d):
        return tuple([p[i]+d[i] for i in (0,1)])
    
    
    def trace(self, pos, direction):
        
        currentPos = self.nextPos(pos, direction)
        while currentPos[0]<self.size and currentPos[1]<self.size:
            if not self.grid[currentPos].get() == 0:
                #print("%s: %s" % (str(pos), str(currentPos)))
                return currentPos
            else:
                currentPos = self.nextPos(currentPos, direction)
        return None
                
#             print("%s: %g" % (str(pos), self.grid[pos].get()))
#         return self.grid[pos]


    def setUpdated(self, isUpdated):
        
        for x in xrange(self.size):
            for y in xrange(self.size):
                self.grid[(x,y)].updated == isUpdated
        
class Cell(object):
    def __init__(self, v):
        self.value = int(v)
        self.updated = False
    def __eq__(self, other):
        return other == self.value
    def __repr__(self):
        if self.get() == 0:
            return " "
        else:
            u = ""
            if self.updated:
                u = "-"
            return str(self.get())+u
            
    def set(self, v):
        self.value = int(v)
    def get(self):
        return self.value
    def double(self):
        self.value = self.value * 2
