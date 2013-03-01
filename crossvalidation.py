import numpy as np
from project1 import *

def CV(alg, X, Y, k):
    n = Y.size

    xFolds = []
    yFolds = []
    step = n / k
    for i in xrange(k):
        start = step * i
        end = step * (i + 1)
        if i == k-1:
            end = n
        xFolds.append(X[start:end])
        yFolds.append(Y[start:end])

    misses = 0
    for i in xrange(k):
        xTraining = np.vstack(xFolds[:i] + xFolds[i + 1:])
        xTest = xFolds[i]

        yTraining = np.vstack(yFolds[:i] + yFolds[i + 1:])
        yTest = yFolds[i]

        theta = alg(xTraining, yTraining)
        for index, row in enumerate(xTest):
            comparator = np.dot(theta.T, row)
            if np.sign(comparator) != yTest[index]:
                misses += 1

    return misses / float(n)

