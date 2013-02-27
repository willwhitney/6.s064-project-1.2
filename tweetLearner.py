import numpy as np

######################################################################
#   General file handling, etc.
######################################################################

def slurp_file(filename):
    f = open(filename)
    lines = []
    for line in f:
        lines.append(line.rstrip())
    return lines

def processFile(pathX = 'train-tweet.txt', pathY = 'train-answer.txt'):
    tw = slurp_file(pathX) # list of tweets in strings
    X = tweetsToX(tw)
    Y = np.transpose(np.array([[int(y) for y in slurp_file(pathY)]]))
    XY = np.random.permutation(np.hstack([X, Y]))
    (X, Y) = np.hsplit(XY, [-1])
    return (X, Y)

def splitTweets(percent, voc = None):
    (X, Y) = processFile(voc = voc)
    n = int(len(X) * percent)
    (X1, X2) = np.vsplit(X, [n])
    (Y1, Y2) = np.vsplit(Y, [n])
    return (X1, Y1, X2, Y2)

######################################################################
##  Making a learning curve plot
######################################################################

# trainSetSizes is a list of numbers specifying the training set sizes
# (will be used as the x values for both plots

# trainErrors is a list of numbers between 0 and 1; same length as
# trainSetSizes

# testErrors is a list of numbers between 0 and 1; same length as
# trainSetSizes

import pylab as pl

def plotTrainTestCurves(trainSetSizes, trainErrors, testErrors):
    fig = pl.figure()
    ax = fig.add_subplot(111)
    ax.cla()
    ax.plot(trainSetSizes, trainErrors, color = 'blue')
    ax.plot(trainSetSizes, testErrors, color = 'red')

    
