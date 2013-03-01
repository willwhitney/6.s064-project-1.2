## Project 1.2 Part C

### Experiment

In my tests, I used these parameters.

    number of folds = 10
    number of epochs = 10
    lambda = 0.01

### Results

In this test, the averaged perceptron algorithm performed the best, with an error rate of about 0.15.

    Error Rate for mostPrevalentClass: 0.332857142857
    Error Rate for perceptronL: 0.167142857143
    Error Rate for perceptronA: 0.154285714286
    Error Rate for hlsgdL: 0.197142857143
    Error Rate for hlsgdA: 0.168571428571



## Project 1.2 Part D

### Experiment

In running this experiment, I constructed a function `buildLearningCurve(alg, X, Y)`, which: 

1. split the X and Y matrices into the 70/30 training/test sets
2. for each subset 10%, 20%, 30%, etc of the training set:
	a. trained `alg` on that subset
	b. tested `alg`'s performance on both that training subset and the test set
3. returned the triple `(trainSetSizes, trainErrors, testErrors)` of all the results of `alg`

Then, I created a function `plotAllLearningCurves()` which ran `buildLearningCurve` for each of the five algorithms and plotted the results as an error fraction, #errors / #datapoints, where #datapoints was, respectively, the size of the training subset or the size of the test set.

### Results

![Y-axis is in error rate.](./learning_curves.png "Learning Curves")

Though this may be hard to see from the graphs, `perceptronA` and `hlsgdA` had very similar results on the largest of the training samples, `perceptronA` at about 18% error and `hlsgdA` at about 16.5%. `perceptronA` seems to learn the most smoothly, but we would need more data to verify that. As might be expected, the performance of the 'last' versions of the algorithms is somewhat more unreliable than that of the 'average' versions, since there can be 'bounce', or oscillation, in the quality of whichever $$$\theta$$$ is returned.