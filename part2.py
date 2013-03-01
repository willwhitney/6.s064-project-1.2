import part1
import crossvalidation
import project1
import numpy as np

def slurp_file(filename):
    f = open(filename)
    lines = []
    for line in f:
        lines.append(line.rstrip())
    return lines

def processFile(pathX = 'train-tweet.txt', pathY = 'train-answer.txt'):
    tw = slurp_file(pathX) # list of tweets in strings
    X = part1.tweetsToX(tw)
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
    trainPlot = ax.plot(trainSetSizes, trainErrors, color = 'blue')
    testPlot = ax.plot(trainSetSizes, testErrors, color = 'red')
    ax.legend(["Training Error", "Test Error"])
    pl.show()



k = 10
numEpochs = 10
l = 0.01

def perceptronL(X, Y):
    return part1.perceptronL(X, Y, numEpochs)

def perceptronA(X, Y):
    return part1.perceptronA(X, Y, numEpochs)

def hlsgdL(X, Y):
    return part1.hlsgdL(X, Y, l, project1.CountingIndex().fn, numEpochs)

def hlsgdA(X, Y):
    return part1.hlsgdA(X, Y, l, project1.CountingIndex().fn, numEpochs)

def crossValidateAll():
    print "\nCross-validating all algorithms."
    X, Y = processFile()
    funcs = [part1.mostPrevalentClass, perceptronL, perceptronA, hlsgdL, hlsgdA]
    for func in funcs:
        print "Results for " + func.__name__
        print crossvalidation.CV(func, X, Y, k)

def buildLearningCurve(alg, X, Y):
    xTraining = X[: X.shape[0] * 7 / float(10)]
    yTraining = Y[: Y.shape[0] * 7 / float(10)]

    xTest = X[X.shape[0] * 7 / float(10):]
    yTest = Y[Y.shape[0] * 7 / float(10):]

    trainSetSizes = []
    trainErrors = []
    testErrors = []
    for i in range(1, 11):
        xT = xTraining[: xTraining.shape[0] * i / float(10)]
        yT = yTraining[: yTraining.shape[0] * i / float(10)]

        theta = alg(xT, yT)
        trainSetSizes.append(xT.shape[0])
        
        misses = 0
        for index, row in enumerate(xT):
            comparator = np.dot(theta.T, row)
            if np.sign(comparator) != yT[index]:
                misses += 1

        trainErrors.append(misses)


        misses = 0
        for index, row in enumerate(xTest):
            comparator = np.dot(theta.T, row)
            if np.sign(comparator) != yTest[index]:
                misses += 1

        testErrors.append(misses)

    return (trainSetSizes, trainErrors, testErrors)

def plotAllLearningCurves():
    X, Y = processFile()
    testSetSize = X[X.shape[0] * 7 / float(10):].shape[0]
    funcs = [part1.mostPrevalentClass, perceptronL, perceptronA, hlsgdL, hlsgdA]
    fig = pl.figure()
    ax = None
    for i, func in enumerate(funcs):
        trainSetSizes, trainErrors, testErrors = buildLearningCurve(func, X, Y)
        trainErrorRates = [trainErrors[j] / float(trainSetSizes[j]) for j, val in enumerate(trainErrors)]
        testErrorRates = [testErrors[j] / float(testSetSize) for j, val in enumerate(testErrors)]
        ax = fig.add_subplot(2, 3, i + 1)
        ax.cla()
        ax.set_title(func.__name__)
        trainPlot = ax.plot(trainSetSizes, trainErrorRates, color = 'blue')
        testPlot = ax.plot(trainSetSizes, testErrorRates, color = 'red')
    ax.legend(["Training Error", "Test Error"])
    pl.show()
        

def tweetsToXWordcounter(tweetList):
    wordList = []
    tweetVectors = []

    for tweet in tweetList:
        words = sorted(part1.stringToWordList(tweet))
        tweetVectors.append(words)
        for word in words:
            wordList.append(word)

    wordList.sort()
    wordDict = {}
    i = 1
    for word in wordList:
        if word not in wordDict:
            wordDict[word] = i
            i += 1

    X = np.zeros((len(wordDict) + 1, len(tweetList)))
    for i, tweet in enumerate(tweetVectors):
        wordCounts = {}
        for word in tweet:
            if word not in wordCounts:
                wordCounts[word] = 1
            else:
                wordCounts[word] += 1
        X[0, i] = 1
        for word in tweet:
            X[wordDict[word], i] = wordCounts[word]

    return X.T

def processFileWithCounts(pathX = 'train-tweet.txt', pathY = 'train-answer.txt'):
    tw = slurp_file(pathX) # list of tweets in strings
    X = tweetsToXWordcounter(tw)
    Y = np.transpose(np.array([[int(y) for y in slurp_file(pathY)]]))
    XY = np.random.permutation(np.hstack([X, Y]))
    (X, Y) = np.hsplit(XY, [-1])
    return (X, Y)

def cvAlgsWithWordCounts():
    print "\nCross-validating all algorithms, using word counts."
    X, Y = processFileWithCounts()
    funcs = [part1.mostPrevalentClass, perceptronL, perceptronA, hlsgdL, hlsgdA]
    for func in funcs:
        print "Results for " + func.__name__
        print crossvalidation.CV(func, X, Y, k)


crossValidateAll()
cvAlgsWithWordCounts()











