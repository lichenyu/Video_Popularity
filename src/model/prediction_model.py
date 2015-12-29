# -*- coding: utf-8 -*-

import math
import calcu_error

# Log-Linear Model
# ln(y) = ln(x) + c
# y = e^(ln(x) + c)
def predictByLogLinear(x, c):
    if 0 == x:
        return 0
    else:
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

def predictByN7(infile, outfile):
    fd = open(infile.decode('UTF-8'), 'r')
    predictionFd = open(outfile.decode('UTF-8'), 'w')
    #rseLogLinearList = []
    #rseLinearLsList = []
    rseLinearLrsList = []
    #seLogLinearList = []
    #seLinearLsList = []
    #seLinearLrsList = []
    #logLinearPara = 0.3466935
    #linearLsPara = 1.293118
    linearLrsPara = 1.235237
    for line in fd.readlines():
        fields = line.strip().split('\t', -1)
        # id, n7, n30
        predictionFd.write(fields[0] + '\t' + fields[1] + '\t' + fields[2])
        n7 = int(fields[1])
        obsN30 = int(fields[2])
        # Log-Linear
        #prdN30 = int(predictByLogLinear(n7, logLinearPara))
        #rse = calcu_error.getRSE(obsN30, prdN30)
        #rseLogLinearList.append(rse)
        #se = calcu_error.getSE(obsN30, prdN30)
        #seLogLinearList.append(se)
        #predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        # Linear-LS
        #prdN30 = int(predictByLinear(n7, linearLsPara))
        #rse = calcu_error.getRSE(obsN30, prdN30)
        #rseLinearLsList.append(rse)
        #se = calcu_error.getSE(obsN30, prdN30)
        #seLinearLsList.append(se)
        #predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        # Linear-LRS
        prdN30 = int(round(predictByLinear(n7, linearLrsPara)))
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseLinearLrsList.append(rse)
        #se = calcu_error.getSE(obsN30, prdN30)
        #seLinearLrsList.append(se)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        
        predictionFd.write('\n')
    
#     mrseStr = 'Log-Linear MRSE = ' + str(sum(rseLogLinearList) / len(rseLogLinearList)) + ', ' \
#                 + 'Linear-LS MRSE = ' + str(sum(rseLinearLsList) / len(rseLinearLsList)) + ', ' \
#                 + 'Linear-LRS MRSE = ' + str(sum(rseLinearLrsList) / len(rseLinearLrsList)) + '\n' \
#                 + 'Log-Linear MSE = ' + str(sum(seLogLinearList) / len(seLogLinearList)) + ', ' \
#                 + 'Linear-LS MSE = ' + str(sum(seLinearLsList) / len(seLinearLsList)) + ', ' \
#                 + 'Linear-LRS MSE = ' + str(sum(seLinearLrsList) / len(seLinearLrsList)) + '\n'
    mrseStr = 'Linear-LRS MRSE = ' + str(sum(rseLinearLrsList) / len(rseLinearLrsList)) + '\n'
    predictionFd.write(mrseStr)
    print(mrseStr)
    fd.close()
    predictionFd.close()
    
def predictByI7(infile, outfile):
    fd = open(infile.decode('UTF-8'), 'r')
    predictionFd = open(outfile.decode('UTF-8'), 'w')
    #rseMultiLinearLsList = []
    rseMultiLinearLrsList = []
    #seMultiLinearLsList = []
    ##seMultiLinearLrsList = []
    #multiLinearLsPara = [1.2682858, 0.9973000, 1.6227158, 0.4786203, 1.7795820, 2.3959505, 1.6855002]
    multiLinearLrsPara = [1.179124, 1.289353, 1.241006, 1.506698, 1.352725, 1.731021, 2.237415]
    for line in fd.readlines():
        fields = line.strip().split('\t', -1)
        # id, i1, ..., i7, n30
        predictionFd.write(fields[0] + '\t' + fields[8])
        iList = []
        for i in range(1, 1 + 7):
            iList.append(int(fields[i]))
        obsN30 = int(fields[8])
        # Linear-LS
        #prdN30 = int(predictByMultipleLinear(iList, multiLinearLsPara))
        #rse = calcu_error.getRSE(obsN30, prdN30)
        #rseMultiLinearLsList.append(rse)
        #se = calcu_error.getSE(obsN30, prdN30)
        #seMultiLinearLsList.append(se)
        #predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        # Linear-LRS
        prdN30 = int(round(predictByMultipleLinear(iList, multiLinearLrsPara)))
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseMultiLinearLrsList.append(rse)
        #se = calcu_error.getSE(obsN30, prdN30)
        #seMultiLinearLrsList.append(se)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        
        predictionFd.write('\n')
    
#     mrseStr = 'Multi-Linear-LS MRSE = ' + str(sum(rseMultiLinearLsList) / len(rseMultiLinearLsList)) + ', ' \
#                 + 'Multi-Linear-LRS MRSE = ' + str(sum(rseMultiLinearLrsList) / len(rseMultiLinearLrsList)) + '\n' \
#                 + 'Multi-Linear-LS MSE = ' + str(sum(seMultiLinearLsList) / len(seMultiLinearLsList)) + ', ' \
#                 + 'Multi-Linear-LRS MSE = ' + str(sum(seMultiLinearLrsList) / len(seMultiLinearLrsList)) + '\n'
    mrseStr = 'Multi-Linear-LRS MRSE = ' + str(sum(rseMultiLinearLrsList) / len(rseMultiLinearLrsList)) + '\n'
    predictionFd.write(mrseStr)
    print(mrseStr)
    fd.close()
    predictionFd.close()
    
def predictByProposedForBurstSlow(infile, outfile):
    fd = open(infile.decode('UTF-8'), 'r')
    predictionFd = open(outfile.decode('UTF-8'), 'w')
    rseList = []
    para = 1.169527
    for line in fd.readlines():
        fields = line.strip().split('\t', -1)
        # id, n7, n30, rate
        predictionFd.write(fields[0] + '\t' + fields[1] + '\t' + fields[2])
        n7 = int(fields[1])
        obsN30 = int(fields[2])
        # n30 = a * n7
        prdN30 = int(round(para * n7))
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseList.append(rse)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        
        predictionFd.write('\n')
    
    mrseStr = 'Proposed Method MRSE = ' + str(sum(rseList) / len(rseList)) + '\n'
    predictionFd.write(mrseStr)
    print(mrseStr)
    fd.close()
    predictionFd.close()

if __name__ == '__main__':
#     predictByN7('F:\\Video_Popularity\\rawdata\\N7N30', 
#             'F:\\Video_Popularity\\analysis\\2_predict_value\\N7N30_Prediction')
#     predictByI7('F:\\Video_Popularity\\rawdata\\I7N30', 
#             'F:\\Video_Popularity\\analysis\\2_predict_value\\I7N30_Prediction')
    # Log-Linear with directly LS
    # Log-Linear with least relative squares
    # Log-Linear with maximum likelihood estimation
    # Linear with directly LS
    # Linear with least relative squares
    
    # check calculated value ?= least relative squares

    # in training set and in test set
    
    
    predictByN7('F:\\Video_Popularity\\src\\burst\\N7N30_BurstSlow', 
            'F:\\Video_Popularity\\analysis\\2_predict_value\\N7N30_BurstSlow_Prediction')
    predictByI7('F:\\Video_Popularity\\src\\burst\\I7N30_BurstSlow', 
            'F:\\Video_Popularity\\analysis\\2_predict_value\\I7N30_BurstSlow_Prediction')
    predictByProposedForBurstSlow('F:\\Video_Popularity\\src\\burst\\BurstSlow_rate', 
                                  'F:\\Video_Popularity\\analysis\\2_predict_value\\Proposed_BurstSlow_Prediction')
