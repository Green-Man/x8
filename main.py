import numpy as np

class MainGame(object):
    def __init__(self):
        self.dim = 2
        self.size = 4
        self.status = "ingame"
        self.emptyCells = None
        
        shape = [self.size for x in xrange(self.dim)]
        self.grid = np.zeros(shape, dtype=Cell)
        
        for y in xrange(self.size):
            for x in xrange(self.size):
                self.grid[x,y] = Cell(0)
        
        self.spawn()
        self.spawn()
    
    def spawn(self):
        self.emptyCells = []
        iterator = np.nditer(self.grid, flags=["multi_index", "refs_ok"])
        while not iterator.finished:
            if iterator[0].item().get() == 0:
                self.emptyCells.append(iterator.multi_index)
            iterator.iternext()
        if len(self.emptyCells):
            cellToFill = self.emptyCells[np.random.randint(len(self.emptyCells))]
            if np.random.random() < 0.1:
                newCell = Cell(4)
            else:
                newCell = Cell(2)
            self.grid[cellToFill] = newCell
            return True
        else:
            return False
    
    
    def move(self, direction, fake=False):
        self.isMoved = False
        d = np.array(direction)
        xRange = range(self.size)
        yRange = range(self.size)
        if d[1] > 0:
            yRange =  [val for val in reversed(yRange)]
        if d[0] > 0:
            xRange = [val for val in reversed(xRange)]
        
        def merge(pos, d):
            value = self.grid[pos].get()
            nextNonZero = self.nextNonZeroPos(pos, d)
            if nextNonZero:
                if value:
                    if self.grid[nextNonZero].get() == self.grid[pos].get():
                        if not fake:
                            self.grid[pos].double()
                            self.grid[nextNonZero] = Cell(0)
                        self.isMoved = True
                else:
                    if not fake:
                        self.grid[pos].set(self.grid[nextNonZero].get())
                        self.grid[nextNonZero] = Cell(0)
                    self.isMoved = True
                    if not fake:
                        currentTracePos = yRange.index(pos[1])
                        for  yt in yRange[currentTracePos:]:
                            merge((pos[0], yt), d)
        
        for x in xRange:
            for y in yRange:
                pos = (x,y)
                merge(pos, -d)
        
        if not fake:
            if self.isMoved:
                self.spawn()
            if not self.isMoved:
                if not self.isMovePossible():
                    self.status = "lose"
    
    def isMovePossible(self):
        for tryDir in [(0,1), (0,-1), (1,0), (-1,0),]:
            dirct = tryDir
            self.move(dirct, fake=True)
            if self.isMoved:
                break
        return self.isMoved
    
    def nextPos(self, p,d):
        return tuple([p[i]+d[i] for i in xrange(2)])
    
    
    def nextNonZeroPos(self, pos, direction):
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
