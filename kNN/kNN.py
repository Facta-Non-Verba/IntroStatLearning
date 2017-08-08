import numpy as np
import pandas as pd


def nearestNeighbors(data, y, testObs, K): #find dataset later to play around with
    if type(data) is not pd.DataFrame or testObs is not np.array or y is not np.array:
        raise Exception("Invalid input for kNN")
    testArr = pd.concat(testObs*(data[0].count()))
    diff = data - testArr
    sqDiff = diff**2
    distVector = diff.cumsum().apply(numpy.sqrt)
    closestIndices = np.argsort(distVector)[0:k]
    neighbors = y[closetIndices]
    return neighbors.groupby(neighbors).size().max()
