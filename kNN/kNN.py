import numpy as np
import pandas as pd


def nearestNeighbors(data, y, testObs, K):
    if type(data) is not pd.DataFrame or testObs is not np.array or y is not np.array:
        raise Exception("Invalid input for kNN")
    distVector = data.apply(lambda x: distance(x, testObs), 0) #annoying, can't figure out
    # how to vectorize to get a Pandas series after applying a function to every row
    # and keeping the value
    closestIndices = np.argsort(distVector)[0:k]
    neighbors = y[closetIndices]
    return neighbors.groupby(neighbors).size().max()



def distance(obs1, obs2): #returns the Euclidean distance of the two observations
    if type(obs1) is not np.array or type(obs2) is not np.array:
        raise Exception("invalid input")
    diff = obs1 - obs2
