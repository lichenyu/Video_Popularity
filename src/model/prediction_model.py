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

def predictByBaseN7(infile, outfile):
    fd = open(infile.decode('UTF-8'), 'r')
    predictionFd = open(outfile.decode('UTF-8'), 'w')
    
    rseLogLinearList = []
    rseLinearLrsList = []
    logLinearPara = 0.3466935
    linearLrsPara = 1.235237
    
    for line in fd.readlines():
        fields = line.strip().split('\t', -1)
        # id, n7, n30
        predictionFd.write(fields[0] + '\t' + fields[1] + '\t' + fields[2])
        n7 = int(fields[1])
        obsN30 = int(fields[2])
        # Log-Linear
        prdN30 = int(round(predictByLogLinear(n7, logLinearPara)))
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseLogLinearList.append(rse)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        # Linear-LRS
        prdN30 = int(round(predictByLinear(n7, linearLrsPara)))
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseLinearLrsList.append(rse)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        
        predictionFd.write('\n')
    
    mrseStr = 'Log-Linear MRSE = ' + str(sum(rseLogLinearList) / len(rseLogLinearList)) + ', ' \
                + 'Linear-LRS MRSE = ' + str(sum(rseLinearLrsList) / len(rseLinearLrsList)) + '\n'
    predictionFd.write(mrseStr)
    print(mrseStr)
    fd.close()
    predictionFd.close()
    
def predictByBaseI7(infile, outfile):
    fd = open(infile.decode('UTF-8'), 'r')
    predictionFd = open(outfile.decode('UTF-8'), 'w')
    
    rseMultiLinearLrsList = []
    multiLinearLrsPara = [1.179124, 1.289353, 1.241006, 1.506698, 1.352725, 1.731021, 2.237415]
    
    for line in fd.readlines():
        fields = line.strip().split('\t', -1)
        # id, i1, ..., i7, n30
        predictionFd.write(fields[0] + '\t' + fields[8])
        iList = []
        for i in range(1, 1 + 7):
            iList.append(int(fields[i]))
        obsN30 = int(fields[8])
        # Linear-LRS
        prdN30 = int(round(predictByMultipleLinear(iList, multiLinearLrsPara)))
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseMultiLinearLrsList.append(rse)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        
        predictionFd.write('\n')
    
    mrseStr = 'Multi-Linear-LRS MRSE = ' + str(sum(rseMultiLinearLrsList) / len(rseMultiLinearLrsList)) + '\n'
    predictionFd.write(mrseStr)
    print(mrseStr)
    fd.close()
    predictionFd.close()
    
#def predictByProposedForBurstSlow(infile, outfile):


if __name__ == '__main__':
    predictByBaseN7('F:\\Video_Popularity\\rawdata\\150801+151017\\N7N30', 
            'F:\\Video_Popularity\\analysis\\2_predict_value\\150801+151017\\N7N30_Prediction')
    predictByBaseI7('F:\\Video_Popularity\\rawdata\\150801+151017\\I7N30', 
            'F:\\Video_Popularity\\analysis\\2_predict_value\\150801+151017\\I7N30_Prediction')
    
    