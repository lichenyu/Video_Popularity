import math

def getRSE(observed, predicted):
    return math.pow((observed * 1. - predicted) / observed, 2)

def getSE(observed, predicted):
    return math.pow((observed * 1. - predicted), 2)

if __name__ == '__main__':
    pass