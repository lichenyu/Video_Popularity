# -*- coding: utf-8 -*-

import math

def getRSE(observed, predicted):
    return math.pow((observed * 1. - predicted) / observed, 2)

def getSE(observed, predicted):
    return math.pow((observed * 1. - predicted), 2)

# Log-Linear Model
# ln(y) = ln(x) + c
# y = e^(ln(x) + c)
def predictByLogLinear(x, c):
    if 0 == x:
        return 0
    else:
        return int(round(math.exp(math.log(x) + c)))

# Linear Model
# y = ax
def predictByLinear(x, a):
    return int(round(x * 1. * a))

# Multiple Linear Model
# y = a1*x1 + a2*x2 + ... an*xn
def predictByMultiLinear(x, a):
    if len(x) != len(a):
        return -1
    rv = 0
    for i in range(0, len(x)):
        rv = rv + x[i] * 1. * a[i]
    return int(round(rv))

def evaluateLogLinear(infile, outfile, logLinearPara):
    inFd = open(infile.decode('UTF-8'), 'r')
    outFd = open(outfile.decode('UTF-8'), 'w')
    rseList = []
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        # id, i1, ..., i30
        vciList = []
        for i in range(1, 1 + 30):
            vciList.append(int(fields[i]))
        n7 = sum(vciList[0 : 7])
        obsN30 = sum(vciList)
        prdN30 = predictByLogLinear(n7, logLinearPara)
        rse = getRSE(obsN30, prdN30)
        rseList.append(rse)
        outFd.write(fields[0] + '\t' + str(obsN30) + '\t' + str(prdN30) + '\t' + str(rse) + '\n')
    mrseStr = 'Log-Linear: Count = ' + str(len(rseList)) + ', MRSE = ' + str(sum(rseList) / len(rseList))
    print(mrseStr)
    outFd.write(mrseStr + '\n')
    inFd.close()
    outFd.close()
    rv = [len(rseList), sum(rseList)]
    return rv

def evaluateMultiLinear(infile, outfile, multiLinearParas):
    inFd = open(infile.decode('UTF-8'), 'r')
    outFd = open(outfile.decode('UTF-8'), 'w')
    rseList = []
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        # id, i1, ..., i30
        vciList = []
        for i in range(1, 1 + 30):
            vciList.append(int(fields[i]))
        obsN30 = sum(vciList)
        prdN30 = predictByMultiLinear(vciList[0 : 7], multiLinearParas)
        rse = getRSE(obsN30, prdN30)
        rseList.append(rse)
        outFd.write(fields[0] + '\t' + str(obsN30) + '\t' + str(prdN30) + '\t' + str(rse) + '\n')
    mrseStr = 'Multi-Linear: Count = ' + str(len(rseList)) + ', MRSE = ' + str(sum(rseList) / len(rseList))
    print(mrseStr)
    outFd.write(mrseStr + '\n')
    inFd.close()
    outFd.close()
    rv = [len(rseList), sum(rseList)]
    return rv

def evaluateEPBP_ML(infile, outfile, modelParas):
    inFd = open(infile.decode('UTF-8'), 'r')
    outFd = open(outfile.decode('UTF-8'), 'w')
    rseList = []
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        # id, i1, ..., i30
        vciList = []
        for i in range(1, 1 + 30):
            vciList.append(int(fields[i]))
        obsN30 = sum(vciList)
        burst = int(fields[31])
        # fList = [i1, ..., i7, burst * n7]
        fList = vciList[0 : 7]
        fList.append(burst * sum(fList))
        prdN30 = predictByMultiLinear(fList, modelParas)
        rse = getRSE(obsN30, prdN30)
        rseList.append(rse)
        outFd.write(fields[0] + '\t' + str(obsN30) + '\t' + str(prdN30) + '\t' + str(rse) + '\n')
    mrseStr = 'EPBP_ML: Count = ' + str(len(rseList)) + ', MRSE = ' + str(sum(rseList) / len(rseList))
    print(mrseStr)
    outFd.write(mrseStr + '\n')
    inFd.close()
    outFd.close()
    rv = [len(rseList), sum(rseList)]
    return rv

# base models: log-linear, multi-linear
def evaluateBaseModels(patterns, testprefix, outprefix, logLinearPara, multiLinearLrsPara):
    # rv = [len(rseList), sum(rseList)]
    total = 0
    rseLogLinear = 0
    rseMultiLinear = 0
    for i in range(0, len(patterns)):
        print('Pattern ' + patterns[i] + ': ')
        
        rv = evaluateLogLinear(testprefix + patterns[i], 
                               outprefix + patterns[i] + '_loglinear', 
                               logLinearPara)
        total = total + rv[0]
        rseLogLinear = rseLogLinear + rv[1]
        
        rv = evaluateMultiLinear(testprefix + patterns[i], 
                                 outprefix + patterns[i] + '_multilinear', 
                                 multiLinearLrsPara)
        rseMultiLinear = rseMultiLinear + rv[1]
        
        print('')
    print('Total Count = ' + str(total) + \
          '\nLogLinear MRSE = ' + str(rseLogLinear/total) + \
          '\nTotal MultiLinear MRSE = ' + str(rseMultiLinear/total))
    
def evaluateProposedModels(patterns, testprefix, outprefix, pbmlBpParas):
    # rv = [len(rseList), sum(rseList)]
    total = 0
    rseEPBP_ML = 0
    for i in range(0, len(patterns)):
        print('Pattern ' + patterns[i] + ': ')
        rv = evaluateEPBP_ML(testprefix + patterns[i], 
                             outprefix + patterns[i] + '_epbp_ml', 
                             pbmlBpParas[i])
        total = total + rv[0]
        rseEPBP_ML = rseEPBP_ML + rv[1]
        print('')
    print('Total Count = ' + str(total) + \
          '\nEPBP_ML MRSE = ' + str(rseEPBP_ML/total))
