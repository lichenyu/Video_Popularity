import math

# def getMRSE(observed, predicted):
#     if len(observed) != len(predicted):
#         return -1
#     rseList = list()
#     for i in range(0, len(observed)):
#         rseList.append(math.pow((observed[i] * 1. - predicted[i]) / observed[i], 2))
#     return sum(rseList) / len(rseList)

def getRSE(observed, predicted):
    return math.pow((observed * 1. - predicted) / observed, 2)

# def getMSE(observed, predicted):
#     if len(observed) != len(predicted):
#         return -1
#     seList = list()
#     for i in range(0, len(observed)):
#         seList.append(math.pow((observed[i] * 1. - predicted[i]), 2))
#     return sum(seList) / len(seList)

def getSE(observed, predicted):
    return math.pow((observed * 1. - predicted), 2)

if __name__ == '__main__':
    obs = list()
    obs.append(1.)
    obs.append(2.)
    obs.append(3)
    obs.append(4)
    obs.append(5)
    pre = list()
    pre.append(2)
    pre.append(4)
    pre.append(6)
    pre.append(8)
    pre.append(10)
    
    #print(getMRSE(obs, pre))
    #print(getMSE(obs, pre))
    
    #print(getRSE(9, 8.5))
    #print(getSE(9, 8.5))