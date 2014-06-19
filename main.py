import numpy as np

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
            if np.random.random() < 0.1:
                newCell = Cell(4)
            else:
                newCell = Cell(2)
            self.grid[cellToFill] = newCell
    
    
    def move(self, direction):
        
        d = np.array(direction)
        xRange = xrange(self.size)
        yRange = xrange(self.size)
        if d[1] > 0:
            yRange = reversed(yRange)
        if d[0] > 0:
            xRange = reversed(xRange)
        for y in yRange:
            for x in xRange:
                pos = (x,y)
                value = self.grid[pos].get()
                nextNonZero = self.trace(pos, -d)
                if nextNonZero:
                    if value:
                        if self.grid[nextNonZero].get() == self.grid[pos].get():
                            self.grid[pos].double()
                            self.grid[nextNonZero] = Cell(0)
                    else:
                        self.grid[pos].set(self.grid[nextNonZero].get())
                        self.grid[nextNonZero] = Cell(0)
        self.spawn()
    
    
    def nextPos(self, p,d):
        return tuple([p[i]+d[i] for i in xrange(2)])
    
    
    def trace(self, pos, direction):
        currentPos = self.nextPos(pos, direction)
        while   currentPos[0]<self.size and\
                currentPos[1]<self.size and\
                currentPos[0]>=0 and\
                currentPos[1]>=0:
            if not self.grid[currentPos].get() == 0:
                return currentPos
            else:
                currentPos = self.nextPos(currentPos, direction)
        return None
    
    
class Cell(object):
    def __init__(self, v):
        self.value = int(v)
    def __eq__(self, other):
        return other == self.value
    def __repr__(self):
        if self.get() == 0:
            return " "
        else:
            return str(self.get())
            
    def set(self, v):
        self.value = int(v)
    def get(self):
        return self.value
    def double(self):
        self.value = self.value * 2
