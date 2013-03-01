import numpy as np
import random

def randomIndex(n):
    return random.randint(0, n-1)

class CountingIndex:
    countingIndexCount = 0
    def fn(self, n):
        self.countingIndexCount += 1
        return self.countingIndexCount % n

# Make a new sequential counter
# countingIndex = CountingIndex().fn

def generateRandom2DData(n, sep = 2, shuffle = True, c1 = None, c2 = None):
    #np.random.seed(0)
    if c1 == None:
        c1 = [0, np.random.randn(), np.random.randn()]
    if c2 == None: 
        c2 = c1 + sep * np.abs(np.array([0, np.random.randn(),
                                         np.random.randn()]))
    
    X = np.r_[np.random.randn(n, 3) + c1, 
              np.random.randn(n, 3) + c2]
    X[:,0] = 1

    Y = np.array([[-1]*n + [1]*n]).T
    if shuffle:
        XY = np.random.permutation(np.hstack([X,Y]))
        (X, Y) = np.hsplit(XY, [-1])
    return X, Y

# A simple test case
X1 = np.array([[1, 1, 2], [1, -1, 2], [1, 1, -2], [1, -1, -2], [1, 0, 2]])
Y1 = np.array([[1], [1], [-1], [-1], [-1]])

