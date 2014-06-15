import numpy as np
import random as r
import time

class MainGame(object):
    def __init__(self):
        self.dim = 2
        self.size = 4
        self.status = "init"
        
        shape = [self.size for x in xrange(self.dim)]
        self.grid = np.zeros(shape, dtype=Cell)
        
        for i in xrange(self.size):
            for j in xrange(self.size):
                self.grid[i,j] = Cell(0)
        
        self.spawn()
        
    def spawn(self):
        
        #emptyCells = []
        #iterator = np.nditer(self.grid)
#         while not iterator
#             if cell.get() == 0:
#                 emptyCells.append([])
                
        
        xInit = np.random.randint(4)
        yInit = np.random.randint(4)
        self.grid[xInit][yInit].set(2)
        
    def move(self, dir):
        print(dir)
        for i in xrange(self.size):
            for j in xrange(self.size):
                self.grid[i,j].set(np.random.randint(4))
        time.sleep(0.1)

class Cell(object):
    def __init__(self, v):
        self.value = int(v)
    def __repr__(self):
        if self.get() == 0:
            return " "
        else:
            return str(self.get())
            
    def set(self, v):
        self.value = int(v)
    def get(self):
        return self.value