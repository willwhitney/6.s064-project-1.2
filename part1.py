import string
import numpy as np
import tweetLearner as tl

def stringToWordList(s):
    s = s.lower()
    
    for char in s:
        if char in string.digits or char in string.punctuation:
            s = s.replace(char, ' ' + char + ' ')

    return s.split()


def tweetsToX(tweetList):
    wordList = []
    tweetVectors = []

    for tweet in tweetList:
        words = sorted(stringToWordList(tweet))
        tweetVectors.append(words)
        for word in words:
            wordList.append(word)

    wordList.sort()
    # print wordList
    wordDict = {}
    i = 1
    for word in wordList:
        if word not in wordDict:
            wordDict[word] = i
            i += 1

    # print wordDict

    X = np.zeros((len(wordDict) + 1, len(tweetList)))
    for i, tweet in enumerate(tweetVectors):
        # print tweet
        X[0, i] = 1
        for word in tweet:
            X[wordDict[word], i] = 1

    return X.T

def mostPrevalentClass(X, Y):
    resultCounts = {}

    for elem in Y:
        elem = elem[0]
        if elem not in resultCounts:
            resultCounts[elem] = 1
        else:
            resultCounts[elem] += 1

    best = None
    for key in resultCounts:
        if best == None or resultCounts[key] > resultCounts[best]:
            best = key

    # print best
    theta = np.zeros((X.shape[1], 1))
    # print theta
    theta[0] = best
    return theta

def perceptronL(X, Y, numEpochs):
    theta = np.zeros(X[1].size)
    thetas = [theta]

    epochs = 0
    while epochs < numEpochs:
        missed = False
        for i, row in enumerate(X):
            comparator = np.dot(theta, row)
            if np.sign(comparator) != Y[i]:
                missed = True
                theta = theta + Y[i] * X[i]
                thetas.append(theta)

        epochs += 1
        if missed == False:
            result = np.array(theta)[np.newaxis]
            return result.T
    
    result = np.array(theta)[np.newaxis]
    return result.T

def perceptronA(X, Y, numEpochs):
    n = Y.size
    theta = np.zeros(X[1].size)
    thetaA = theta

    epochs = 0
    while epochs < numEpochs:
        missed = False
        for i, row in enumerate(X):
            comparator = np.dot(theta, row)
            if np.sign(comparator) != Y[i]:
                missed = True
                theta = theta + Y[i] * X[i]
                w = (1 / float(2 * n))
                thetaA = (1 - w) * thetaA + w * theta

        epochs += 1

    result = np.array(thetaA)[np.newaxis]
    return result.T

def nu(epoch):
    return 1 / (1.0 + epoch)

def epoch(updates, n):
    return int(updates / n)

def hlsgdL(X, Y, l, nextIndex, numEpochs):
    n = Y.size
    theta = np.zeros(X[1].size)

    updates = 0
    while epoch(updates, n) < numEpochs:
        i = nextIndex(n)

        updateContribution = 0
        if Y[i] * np.dot(theta, X[i]) <= 1:
            updateContribution = Y[i] * X[i]

        thetaBar = np.concatenate(([0], theta[1:]))
        # print theta
        # print thetaBar

        update = l * thetaBar - updateContribution
        theta = theta - nu(epoch(updates, n)) * (update)

        # print theta
        updates += 1

    result = np.array(theta)[np.newaxis]
    # print result.T
    return result.T

def hlsgdA(X, Y, l, nextIndex, numEpochs):
    n = Y.size
    theta = np.zeros(X[1].size)
    thetaA = theta

    updates = 0
    while epoch(updates, n) < numEpochs:
        i = nextIndex(n)

        updateContribution = 0
        if Y[i] * np.dot(theta, X[i]) <= 1:
            updateContribution = Y[i] * X[i]

        thetaBar = np.concatenate(([0], theta[1:]))
        # print theta
        # print thetaBar

        update = l * thetaBar - updateContribution
        theta = theta - nu(epoch(updates, n)) * (update)
        w = (1 / float(2 * n))
        thetaA = (1 - w) * thetaA + w * theta

        # print theta
        updates += 1

    result = np.array(thetaA)[np.newaxis]
    # print result.T
    return result.T

# X1 = np.array([[1, 1, 2], [1, -1, 2], [1, 1, -2], [1, -1, -2], [1, 0, 2]])
# Y1 = np.array([[1], [1], [-1], [-1], [-1]])
# print perceptronA(X1, Y1, 10)

# tweetList = tl.slurp_file('train-tweet.txt')
# tweetList = ['OMG!! 2awful a movie.', 'Awesome++ Can you top this?']
# print tweetsToX(tweetList)















