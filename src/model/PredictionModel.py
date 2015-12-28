# -*- coding: utf-8 -*-

import math
import PredictionEvaluator

# Log-Linear Model
# ln(y) = ln(x) + c
# y = e^(ln(x) + c)
def predictByLogLinear(x, c):
    return math.exp(math.log(x) + c)

# Linear Model
# y = ax
def predictByLinear(x, a):
    return x * 1. * a

# Multiple Linear Model
# y = a1*x1 + a2*x2 + ... an*xn
def predictByMultipleLinear(x, a):
    if len(x) != len(a):
        return -1
    rv = 0
    for i in range(0, len(x)):
        rv = rv + x[i] * 1. * a[i]
    return rv

def predict(infile):
    fd = open(infile.decode('UTF-8'), 'r')
    predictionFd = open(infile.decode('UTF-8') + '_Prediction', 'w')
    #fdLogLinear = open(infile.decode('UTF-8') + '_Prediction_LogLinear', 'w')
    #fdLinearLS = open(infile.decode('UTF-8') + '_Prediction_LinearLS', 'w')
    #fdLinearLRS = open(infile.decode('UTF-8') + '_Prediction_LinearLRS', 'w')
    obsList = list()
    prdLogLinearList = list()
    prdLinearLsList = list()
    prdLinearLrsList = list()
    for line in fd.readlines():
        # id, n7, n30
        fields = line.strip().split('\t', -1)
        if 0 == int(fields[1]):
            continue
        vObs = int(fields[2])
        vLogLinear = int(predictByLogLinear(int(fields[1]), 0.7884630))
        vLinearLs = int(predictByLinear(int(fields[1]), 2.887398))
        vLinearLrs = int(predictByLinear(int(fields[1]), 1.503376))
        obsList.append(vObs)
        prdLogLinearList.append(vLogLinear)
        prdLinearLsList.append(vLinearLs)
        prdLinearLrsList.append(vLinearLrs)
        predictionFd.write(fields[0] + '\t' + fields[1] + '\t' + fields[2] + '\t' 
                          + str(vLogLinear) + '\t' + str(PredictionEvaluator.getRSE(vObs, vLogLinear)) + '\t' 
                          + str(vLinearLs) + '\t' + str(PredictionEvaluator.getRSE(vObs, vLinearLs)) + '\t'
                          + str(vLinearLrs) + '\t' + str(PredictionEvaluator.getRSE(vObs, vLinearLrs)) + '\n')
    predictionFd.write('Log-Linear MRSE = ' + str(PredictionEvaluator.getMRSE(obsList, prdLogLinearList)) + ', ' 
                       + 'Linear-LS MRSE = ' + str(PredictionEvaluator.getMRSE(obsList, prdLinearLsList)) + ', '
                       + 'Linear-LRS MRSE = ' + str(PredictionEvaluator.getMRSE(obsList, prdLinearLrsList)) + '\n')
    print('Log-Linear MRSE = ' + str(PredictionEvaluator.getMRSE(obsList, prdLogLinearList)) + ', ' 
          + 'Linear-LS MRSE = ' + str(PredictionEvaluator.getMRSE(obsList, prdLinearLsList)) + ', ' 
          + 'Linear-LRS MRSE = ' + str(PredictionEvaluator.getMRSE(obsList, prdLinearLrsList)) + '\n')
    fd.close()
    #fdLogLinear.close()
    #fdLinearLS.close()
    #fdLinearLRS.close()
    predictionFd.close()

if __name__ == '__main__':
    predict('C:\\Documents and Settings\\Administrator\\桌面\\vc\\data\\N7N30')
    # Log-Linear with directly LS
    # Log-Linear with least relative squares
    # Log-Linear with maximum likelihood estimation
    # Linear with directly LS
    # Linear with least relative squares
    
    # check calculated value ?= least relative squares

    # in training set and in test set
