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

def predict(infile, outfile):
    fd = open(infile.decode('UTF-8'), 'r')
    predictionFd = open(outfile.decode('UTF-8'), 'w')
    rseLogLinearList = list()
    rseLinearLrsList = list()
    for line in fd.readlines():
        fields = line.strip().split('\t', -1)
        # id, n7, n30
        predictionFd.write(fields[0] + '\t' + fields[1] + '\t' + fields[2])
        n7 = int(fields[1])
        obsN30 = int(fields[2])
        # Log-Linear
        prdN30 = predictByLogLinear(n7, 0.369021)
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseLogLinearList.append(rse)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        # Linear-LRS
        prdN30 = predictByLinear(int(fields[1]), 1.238497)
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseLinearLrsList.append(rse)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        
        predictionFd.write('\n')
    
    mrseStr = 'Log-Linear MRSE = ' + str(sum(rseLogLinearList) / len(rseLogLinearList)) + ', ' \
                + 'Linear-LRS MRSE = ' + str(sum(rseLinearLrsList) / len(rseLinearLrsList)) + '\n'
    predictionFd.write(mrseStr)
    print(mrseStr)
    fd.close()
    #fdLogLinear.close()
    #fdLinearLS.close()
    #fdLinearLRS.close()
    predictionFd.close()

if __name__ == '__main__':
    predict('F:\\Video_Popularity\\rawdata\\training.txt', 
            'F:\\Video_Popularity\\analysis\\2_predict_value\\training.txt_Prediction')
    