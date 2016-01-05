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

# replaced by the next function, using I file instead of N file
# def predictByBaseN7(infile, outfile, logLinearPara, linearLrsPara):
#     fd = open(infile.decode('UTF-8'), 'r')
#     predictionFd = open(outfile.decode('UTF-8'), 'w')
#     
#     rseLogLinearList = []
#     rseLinearLrsList = []
#     logLinearPara = logLinearPara
#     linearLrsPara = linearLrsPara
#     
#     for line in fd.readlines():
#         fields = line.strip().split('\t', -1)
#         # id, n1, ..., n30
#         predictionFd.write(fields[0] + '\t' + fields[7] + '\t' + fields[30])
#         n7 = int(fields[7])
#         obsN30 = int(fields[30])
#         # Log-Linear
#         prdN30 = predictByLogLinear(n7, logLinearPara)
#         rse = calcu_error.getRSE(obsN30, prdN30)
#         rseLogLinearList.append(rse)
#         predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
#         # Linear-LRS
#         prdN30 = predictByLinear(n7, linearLrsPara)
#         rse = calcu_error.getRSE(obsN30, prdN30)
#         rseLinearLrsList.append(rse)
#         predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
#         
#         predictionFd.write('\n')
#     
#     mrseStr = 'Log-Linear MRSE = ' + str(sum(rseLogLinearList) / len(rseLogLinearList)) + ', ' \
#                 + 'Linear-LRS MRSE = ' + str(sum(rseLinearLrsList) / len(rseLinearLrsList))
#     predictionFd.write(mrseStr + '\n')
#     print(mrseStr)
#     fd.close()
#     predictionFd.close()
    
def predictByBaseN7(infile, outfile, logLinearPara, linearLrsPara):
    fd = open(infile.decode('UTF-8'), 'r')
    predictionFd = open(outfile.decode('UTF-8'), 'w')
    
    rseLogLinearList = []
    rseLinearLrsList = []
    logLinearPara = logLinearPara
    linearLrsPara = linearLrsPara
    
    for line in fd.readlines():
        fields = line.strip().split('\t', -1)
        # id, i1, ..., i30
        iList = []
        for i in range(1, 1 + 30):
            iList.append(int(fields[i]))
        n7 = sum(iList[0 : 7])
        obsN30 = sum(iList)
        predictionFd.write(fields[0] + '\t' + str(obsN30))
        # Log-Linear
        prdN30 = predictByLogLinear(n7, logLinearPara)
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseLogLinearList.append(rse)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        # Linear-LRS
        prdN30 = predictByLinear(n7, linearLrsPara)
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseLinearLrsList.append(rse)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        
        predictionFd.write('\n')
    
    mrseStr = 'Log-Linear MRSE = ' + str(sum(rseLogLinearList) / len(rseLogLinearList)) + ', ' \
                + 'Linear-LRS MRSE = ' + str(sum(rseLinearLrsList) / len(rseLinearLrsList))
    predictionFd.write(mrseStr + '\n')
    print(mrseStr)
    fd.close()
    predictionFd.close()
    
def predictByBaseI7(infile, outfile, multiLinearLrsPara):
    fd = open(infile.decode('UTF-8'), 'r')
    predictionFd = open(outfile.decode('UTF-8'), 'w')
    
    rseMultiLinearLrsList = []
    multiLinearLrsPara = multiLinearLrsPara
    
    for line in fd.readlines():
        fields = line.strip().split('\t', -1)
        # id, i1, ..., i30
        iList = []
        for i in range(1, 1 + 30):
            iList.append(int(fields[i]))
        obsN30 = sum(iList)
        predictionFd.write(fields[0] + '\t' + str(obsN30))
        # Multi-Linear-LRS
        prdN30 = predictByMultiLinear(iList[0 : 7], multiLinearLrsPara)
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseMultiLinearLrsList.append(rse)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        
        predictionFd.write('\n')
    
    mrseStr = 'Multi-Linear-LRS MRSE = ' + str(sum(rseMultiLinearLrsList) / len(rseMultiLinearLrsList))
    predictionFd.write(mrseStr + '\n')
    print(mrseStr)
    fd.close()
    predictionFd.close()
    
def predictByPBML(infile, outfile, multiLinearLrsPara):
    fd = open(infile.decode('UTF-8'), 'r')
    predictionFd = open(outfile.decode('UTF-8'), 'w')
    
    rseMultiLinearLrsList = []
    multiLinearLrsPara = multiLinearLrsPara
    
    for line in fd.readlines():
        fields = line.strip().split('\t', -1)
        # id, i1, ..., i30
        iList = []
        for i in range(1, 1 + 30):
            iList.append(int(fields[i]))
        obsN30 = sum(iList)
        predictionFd.write(fields[0] + '\t' + str(obsN30))
        # Multi-Linear-LRS
        prdN30 = predictByMultiLinear(iList[0 : 7], multiLinearLrsPara)
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseMultiLinearLrsList.append(rse)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        
        predictionFd.write('\n')
    
    mrseStr = 'Proposed PBML MRSE = ' + str(sum(rseMultiLinearLrsList) / len(rseMultiLinearLrsList))
    predictionFd.write(mrseStr + '\n')
    print(mrseStr)
    fd.close()
    predictionFd.close()
    
def predictByPBML_BP(infile, outfile, multiLinearLrsPara):
    fd = open(infile.decode('UTF-8'), 'r')
    predictionFd = open(outfile.decode('UTF-8'), 'w')
    
    rseMultiLinearLrsList = []
    multiLinearLrsPara = multiLinearLrsPara
    
    for line in fd.readlines():
        fields = line.strip().split('\t', -1)
        # id, i1, ..., i30, indicator
        iList = []
        for i in range(1, 1 + 30):
            iList.append(int(fields[i]))
        obsN30 = sum(iList)
        indicator = int(fields[31])
        predictionFd.write(fields[0] + '\t' + str(obsN30))
        # fList = [i1, ..., i7, indicator * n7]
        fList = iList[0 : 7]
        fList.append(indicator * sum(fList))
        # Multi-Linear-LRS
        prdN30 = predictByMultiLinear(fList, multiLinearLrsPara)
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseMultiLinearLrsList.append(rse)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        
        predictionFd.write('\n')
    
    mrseStr = 'Proposed PBML+BP MRSE = ' + str(sum(rseMultiLinearLrsList) / len(rseMultiLinearLrsList))
    predictionFd.write(mrseStr + '\n')
    print(mrseStr)
    fd.close()
    predictionFd.close()
    
# burst with intercept
def predictByPBML_BP2(infile, outfile, multiLinearLrsPara):
    fd = open(infile.decode('UTF-8'), 'r')
    predictionFd = open(outfile.decode('UTF-8'), 'w')
    
    rseMultiLinearLrsList = []
    multiLinearLrsPara = multiLinearLrsPara
    
    for line in fd.readlines():
        fields = line.strip().split('\t', -1)
        # id, i1, ..., i30, indicator
        iList = []
        for i in range(1, 1 + 30):
            iList.append(int(fields[i]))
        obsN30 = sum(iList)
        indicator = int(fields[31])
        predictionFd.write(fields[0] + '\t' + str(obsN30))
        # fList = [i1, ..., i7, indicator * n7, indicator]
        fList = iList[0 : 7]
        fList.append(indicator * sum(fList))
        fList.append(indicator)
        # Multi-Linear-LRS
        prdN30 = predictByMultiLinear(fList, multiLinearLrsPara)
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseMultiLinearLrsList.append(rse)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        
        predictionFd.write('\n')
    
    mrseStr = 'Proposed PBML+BP2 MRSE = ' + str(sum(rseMultiLinearLrsList) / len(rseMultiLinearLrsList))
    predictionFd.write(mrseStr + '\n')
    print(mrseStr)
    fd.close()
    predictionFd.close()
    
# burst with i and no intercept
def predictByPBML_BP3(infile, outfile, multiLinearLrsPara):
    fd = open(infile.decode('UTF-8'), 'r')
    predictionFd = open(outfile.decode('UTF-8'), 'w')
    
    rseMultiLinearLrsList = []
    multiLinearLrsPara = multiLinearLrsPara
    
    for line in fd.readlines():
        fields = line.strip().split('\t', -1)
        # id, i1, ..., i30, indicator
        iList = []
        for i in range(1, 1 + 30):
            iList.append(int(fields[i]))
        obsN30 = sum(iList)
        indicator = int(fields[31])
        predictionFd.write(fields[0] + '\t' + str(obsN30))
        # fList = [i1, ..., i7, indicator * i1, ,,,, indicator * i7]
        fList = iList[0 : 7]
        for i in range(0, 7):
            fList.append(indicator * fList[i])
        # Multi-Linear-LRS
        prdN30 = predictByMultiLinear(fList, multiLinearLrsPara)
        rse = calcu_error.getRSE(obsN30, prdN30)
        rseMultiLinearLrsList.append(rse)
        predictionFd.write('\t' + str(prdN30) + '\t' + str(rse))
        
        predictionFd.write('\n')
    
    mrseStr = 'Proposed PBML+BP3 MRSE = ' + str(sum(rseMultiLinearLrsList) / len(rseMultiLinearLrsList))
    predictionFd.write(mrseStr + '\n')
    print(mrseStr)
    fd.close()
    predictionFd.close()
    

if __name__ == '__main__':
    #workpath = 'F:/Video_Popularity/'
    workpath = '/Users/ouyangshuxin/Documents/work/Video_Popularity/'
    
    
    
    print('Type 0000000: ')
    predictByBaseN7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_0000000_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_0000000_test_baseN7', 
                    0.3484038, 1.235833)
    predictByBaseI7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_0000000_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_0000000_test_baseI7', 
                    [1.177785, 1.309063, 1.220432, 1.494015, 1.387594, 1.730061, 2.203738])
    predictByPBML(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_0000000_test', 
                  workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_0000000_test_pbml', 
                  [1.8710562, 0.7292189, 1.4115649, 1.2689845, 1.5307522, 0.7547255, 5.7702485])
    
    print('Type 0010000: ')
    predictByBaseN7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_0010000_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_0010000_test_baseN7', 
                    0.3484038, 1.235833)
    predictByBaseI7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_0010000_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_0010000_test_baseI7', 
                    [1.177785, 1.309063, 1.220432, 1.494015, 1.387594, 1.730061, 2.203738])
    predictByPBML(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_0010000_test', 
                  workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_0010000_test_pbml', 
                  [1.431300, 1.022123, 1.002467, 1.347643, 2.042787, 1.361212, 2.747711])
    
    print('Type 0100000: ')
    predictByBaseN7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_0100000_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_0100000_test_baseN7', 
                    0.3484038, 1.235833)
    predictByBaseI7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_0100000_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_0100000_test_baseI7', 
                    [1.177785, 1.309063, 1.220432, 1.494015, 1.387594, 1.730061, 2.203738])
    predictByPBML(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_0100000_test', 
                  workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_0100000_test_pbml', 
                  [1.5031454, 0.9552199, 1.2769401, 1.5995035, 0.8891453, 2.9900238, 4.5620508])
    
    print('Type 1000000: ')
    predictByBaseN7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_1000000_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_1000000_test_baseN7', 
                    0.3484038, 1.235833)
    predictByBaseI7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_1000000_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_1000000_test_baseI7', 
                    [1.177785, 1.309063, 1.220432, 1.494015, 1.387594, 1.730061, 2.203738])
    predictByPBML(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_1000000_test', 
                  workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_1000000_test_pbml', 
                  [1.020864, 1.650731, 1.402532, 1.805735, 1.689735, 2.170273, 3.326809])

    print('Type 1010000: ')
    predictByBaseN7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_1010000_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_1010000_test_baseN7', 
                    0.3484038, 1.235833)
    predictByBaseI7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_1010000_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_1010000_test_baseI7', 
                    [1.177785, 1.309063, 1.220432, 1.494015, 1.387594, 1.730061, 2.203738])
    predictByPBML(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_1010000_test', 
                  workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_1010000_test_pbml', 
                  [1.248046, 1.041718, 0.970693, 2.397707, 2.101312, 1.510596, 4.089463])
    
    print('Type 1100000: ')
    predictByBaseN7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_1100000_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_1100000_test_baseN7', 
                    0.3484038, 1.235833)
    predictByBaseI7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_1100000_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_1100000_test_baseI7', 
                    [1.177785, 1.309063, 1.220432, 1.494015, 1.387594, 1.730061, 2.203738])
    predictByPBML(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_1100000_test', 
                  workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_1100000_test_pbml', 
                  [1.211600, 1.092533, 1.204722, 2.423859, 2.362118, 1.973938, 3.828769])
    
    print('Type 2000000: ')
    predictByBaseN7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_2000000_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_2000000_test_baseN7', 
                    0.3484038, 1.235833)
    predictByBaseI7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_2000000_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_2000000_test_baseI7', 
                    [1.177785, 1.309063, 1.220432, 1.494015, 1.387594, 1.730061, 2.203738])
    predictByPBML(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_2000000_test', 
                  workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_2000000_test_pbml', 
                  [1.1949192, 1.1258028, 0.8759515, 1.2185588, 1.0140954, 1.1790830, 1.6929797])

    print('Type others: ')
    predictByBaseN7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_others_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_others_test_baseN7', 
                    0.3484038, 1.235833)
    predictByBaseI7(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_others_test', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_others_test_baseI7', 
                    [1.177785, 1.309063, 1.220432, 1.494015, 1.387594, 1.730061, 2.203738])
    predictByPBML(workpath + 'analysis/2_predict_value/PBML/150801+151017_2/I30_others_test', 
                  workpath + 'analysis/2_predict_value/PBML/150801+151017_2/rse_others_test_pbml', 
                  [1.168850, 1.140689, 1.132781, 1.235572, 1.254579, 1.411175, 1.452834])
        
    
    
# not consider very fast (2 state)
#     print('Type 0000000: ')
#     predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0000000_test_baseN7', 
#                     0.3452315, 1.236304)
#     predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0000000_test_baseI7', 
#                     [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
#     predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test', 
#                   workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0000000_test_pbml', 
#                     [1.8710562, 0.7292189, 1.4115649, 1.2689845, 1.5307522, 0.7547255, 5.7702485])
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0000000_test_pbml_bp', 
#                     [1.7614136, 0.7850340, 1.5547683, 1.1535014, 1.3793718, 0.8130685, 5.4033738, 0.2575609])
#     
#     print('Type 1000000: ')
#     predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1000000_test_baseN7', 
#                     0.3452315, 1.236304)
#     predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1000000_test_baseI7', 
#                     [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
#     predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test', 
#                   workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1000000_test_pbml', 
#                     [1.165725, 1.246080, 1.268853, 1.830004, 1.503788, 1.970634, 3.043560])
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1000000_test_pbml_bp', 
#                     [1.057131, 1.383293, 1.340171, 1.776463, 1.652662, 1.954112, 2.799800, 0.330536])
#     
#     print('Type 0100000: ')
#     predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0100000_test_baseN7', 
#                     0.3452315, 1.236304)
#     predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0100000_test_baseI7', 
#                     [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
#     predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test', 
#                   workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0100000_test_pbml', 
#                     [1.7260303, 1.0113645, 1.0631047, 1.8750424, 0.7510338, 3.4531069, 2.4238536])
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0100000_test_pbml_bp', 
#                     [1.5193861, 0.9575424, 1.0533085, 2.2046819, 0.7254957, 3.4022394, 2.0214843, 0.4183901])
#     
#     print('Type 1010000: ')
#     predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1010000_test_baseN7', 
#                     0.3452315, 1.236304)
#     predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1010000_test_baseI7', 
#                     [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
#     predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test', 
#                   workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1010000_test_pbml', 
#                     [1.248046, 1.041718, 0.970693, 2.397707, 2.101312, 1.510596, 4.089463])
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1010000_test_pbml_bp', 
#                     [0.9158504, 1.3290235, 1.1209561, 1.5431008, 2.7434331, 1.3978658, 2.5385364, 0.3780278])
#     
#     print('Type 1100000: ')
#     predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1100000_test_baseN7', 
#                     0.3452315, 1.236304)
#     predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1100000_test_baseI7', 
#                     [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
#     predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test', 
#                   workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1100000_test_pbml', 
#                     [1.211600, 1.092533, 1.204722, 2.423859, 2.362118, 1.973938, 3.828769])
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1100000_test_pbml_bp', 
#                     [1.1565211, 1.0175316, 1.4262594, 2.2382570, 2.5459688, 2.0686217, 3.4963375, 0.3323833])
#     
#     print('Type others: ')
#     predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_others_test_baseN7', 
#                     0.3452315, 1.236304)
#     predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_others_test_baseI7', 
#                     [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
#     predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test', 
#                   workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_others_test_pbml', 
#                     [1.221962, 1.466071, 1.107178, 1.195812, 1.175891, 1.413031, 1.431739])
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_others_test_pbml_bp', 
#                     [0.9234874, 1.3241801, 1.1098779, 1.1782202, 1.1850964, 1.2139418, 1.3704516, 0.5497892])
    
    
    
    
    
    # choose which kind of BP model to use
#     print('Type 0000000: ')
#     predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0000000_test_baseN7', 
#                     0.3452315, 1.236304)
#     predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0000000_test_baseI7', 
#                     [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
#     predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test', 
#                   workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0000000_test_pbml', 
#                     [1.8710562, 0.7292189, 1.4115649, 1.2689845, 1.5307522, 0.7547255, 5.7702485])
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0000000_test_pbml_bp', 
#                     [1.7614136, 0.7850340, 1.5547683, 1.1535014, 1.3793718, 0.8130685, 5.4033738, 0.2575609])
#     predictByPBML_BP2(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0000000_test_pbml_bp2', 
#                     [1.7507877, 0.7885185, 1.5802827, 1.1328696, 1.3629325, 0.8130727, 5.4268258, 0.2430426, 1.2266701])
#     predictByPBML_BP3(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0000000_test_pbml_bp3', 
#                     [2.16961245, 0.08946878, 1.65246444, 1.19958584, 0.97762418, 0.26737922, 6.95238911, -1.20983841, 3.14012018, -0.14696968, 1.69638779, 0.81775329, 1.27895007, -4.36759440])
#     print('training')
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0000000_training_pbml_bp', 
#                     [1.7614136, 0.7850340, 1.5547683, 1.1535014, 1.3793718, 0.8130685, 5.4033738, 0.2575609])
#     predictByPBML_BP2(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_training', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0000000_training_pbml_bp2', 
#                     [1.7507877, 0.7885185, 1.5802827, 1.1328696, 1.3629325, 0.8130727, 5.4268258, 0.2430426, 1.2266701])
#     predictByPBML_BP3(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_training', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0000000_training_pbml_bp3', 
#                     [2.16961245, 0.08946878, 1.65246444, 1.19958584, 0.97762418, 0.26737922, 6.95238911, -1.20983841, 3.14012018, -0.14696968, 1.69638779, 0.81775329, 1.27895007, -4.36759440])
#     
#     print('Type 1000000: ')
#     predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1000000_test_baseN7', 
#                     0.3452315, 1.236304)
#     predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1000000_test_baseI7', 
#                     [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
#     predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test', 
#                   workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1000000_test_pbml', 
#                     [1.165725, 1.246080, 1.268853, 1.830004, 1.503788, 1.970634, 3.043560])
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1000000_test_pbml_bp', 
#                     [1.057131, 1.383293, 1.340171, 1.776463, 1.652662, 1.954112, 2.799800, 0.330536])
#     predictByPBML_BP2(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1000000_test_pbml_bp2', 
#                     [1.0500594, 1.4320842, 1.3415727, 1.7814291, 1.6620398, 1.9735765, 2.8098801, 0.2642447, 0.6936268])
#     predictByPBML_BP3(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1000000_test_pbml_bp3', 
#                     [1.05571313, 1.44115896, 1.31599297, 1.65143458, 1.59488202, 1.87127787, 2.89653419, 0.33562175, 0.02931116, 0.51418154, 0.79889651, 0.67660315, 0.64597410, 0.07490420])
#     print('training')
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1000000_training_pbml_bp', 
#                     [1.057131, 1.383293, 1.340171, 1.776463, 1.652662, 1.954112, 2.799800, 0.330536])
#     predictByPBML_BP2(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1000000_training_pbml_bp2', 
#                     [1.0500594, 1.4320842, 1.3415727, 1.7814291, 1.6620398, 1.9735765, 2.8098801, 0.2642447, 0.6936268])
#     predictByPBML_BP3(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1000000_training_pbml_bp3', 
#                     [1.05571313, 1.44115896, 1.31599297, 1.65143458, 1.59488202, 1.87127787, 2.89653419, 0.33562175, 0.02931116, 0.51418154, 0.79889651, 0.67660315, 0.64597410, 0.07490420])
#     
#     print('Type 0100000: ')
#     predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0100000_test_baseN7', 
#                     0.3452315, 1.236304)
#     predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0100000_test_baseI7', 
#                     [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
#     predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test', 
#                   workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0100000_test_pbml', 
#                     [1.7260303, 1.0113645, 1.0631047, 1.8750424, 0.7510338, 3.4531069, 2.4238536])
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0100000_test_pbml_bp', 
#                     [1.5193861, 0.9575424, 1.0533085, 2.2046819, 0.7254957, 3.4022394, 2.0214843, 0.4183901])
#     predictByPBML_BP2(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0100000_test_pbml_bp2', 
#                     [1.5193900, 0.9558768, 1.0536993, 2.2139826, 0.7382476, 3.4138136, 2.0116178, 0.4047228, 0.4133979])
#     predictByPBML_BP3(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0100000_test_pbml_bp3', 
#                     [1.6151018, 0.9832243, 1.0459892, 1.8917865, 0.4528121, 2.9415528, 2.3342308, -0.1000309, 0.2540251, 0.9310223, 3.0357306, 2.6703050, 1.0988935, -0.9702572])
#     print('training')
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0100000_training_pbml_bp', 
#                     [1.5193861, 0.9575424, 1.0533085, 2.2046819, 0.7254957, 3.4022394, 2.0214843, 0.4183901])
#     predictByPBML_BP2(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0100000_training_pbml_bp2', 
#                     [1.5193900, 0.9558768, 1.0536993, 2.2139826, 0.7382476, 3.4138136, 2.0116178, 0.4047228, 0.4133979])
#     predictByPBML_BP3(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_0100000_training_pbml_bp3', 
#                     [1.6151018, 0.9832243, 1.0459892, 1.8917865, 0.4528121, 2.9415528, 2.3342308, -0.1000309, 0.2540251, 0.9310223, 3.0357306, 2.6703050, 1.0988935, -0.9702572])
#     
#     print('Type 1010000: ')
#     predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1010000_test_baseN7', 
#                     0.3452315, 1.236304)
#     predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1010000_test_baseI7', 
#                     [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
#     predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test', 
#                   workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1010000_test_pbml', 
#                     [1.248046, 1.041718, 0.970693, 2.397707, 2.101312, 1.510596, 4.089463])
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1010000_test_pbml_bp', 
#                     [0.9158504, 1.3290235, 1.1209561, 1.5431008, 2.7434331, 1.3978658, 2.5385364, 0.3780278])
#     predictByPBML_BP2(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1010000_test_pbml_bp2', 
#                     [0.8587573, 1.3984583, 1.1443644, 1.8473396, 2.9097714, 1.4518243, 2.7395714, 0.2341117, 0.9327927])
#     predictByPBML_BP3(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1010000_test_pbml_bp3', 
#                     [0.9128640, 1.2390323, 1.1083235, 1.8926415, 2.5115712, 0.8716050, 6.6905723, 0.3446650, -0.1568057, 0.5897414, -0.7199097, 1.6649710, 1.7890285, -4.7079366])
#     print('training')
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1010000_training_pbml_bp', 
#                     [0.9158504, 1.3290235, 1.1209561, 1.5431008, 2.7434331, 1.3978658, 2.5385364, 0.3780278])
#     predictByPBML_BP2(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1010000_training_pbml_bp2', 
#                     [0.8587573, 1.3984583, 1.1443644, 1.8473396, 2.9097714, 1.4518243, 2.7395714, 0.2341117, 0.9327927])
#     predictByPBML_BP3(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1010000_training_pbml_bp3', 
#                     [0.9128640, 1.2390323, 1.1083235, 1.8926415, 2.5115712, 0.8716050, 6.6905723, 0.3446650, -0.1568057, 0.5897414, -0.7199097, 1.6649710, 1.7890285, -4.7079366])
#     
#     print('Type 1100000: ')
#     predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1100000_test_baseN7', 
#                     0.3452315, 1.236304)
#     predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1100000_test_baseI7', 
#                     [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
#     predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test', 
#                   workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1100000_test_pbml', 
#                     [1.211600, 1.092533, 1.204722, 2.423859, 2.362118, 1.973938, 3.828769])
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1100000_test_pbml_bp', 
#                     [1.1565211, 1.0175316, 1.4262594, 2.2382570, 2.5459688, 2.0686217, 3.4963375, 0.3323833])
#     predictByPBML_BP2(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1100000_test_pbml_bp2', 
#                     [1.15636491, 1.01746573, 1.42678712, 2.23928134, 2.54740085, 2.06971526, 3.49757359, 0.33133045, 0.01313545])
#     predictByPBML_BP3(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1100000_test_pbml_bp3', 
#                     [1.1677518, 1.0204268, 1.4445000, 2.1712955, 2.4278582, 1.8371449, 3.4127033, 0.2757639, 0.3365404, 0.2860151, 0.5574621, 0.9327317, 1.3185340, 0.6510481])
#     print('training')
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1100000_training_pbml_bp', 
#                     [1.1565211, 1.0175316, 1.4262594, 2.2382570, 2.5459688, 2.0686217, 3.4963375, 0.3323833])
#     predictByPBML_BP2(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1100000_training_pbml_bp2', 
#                     [1.15636491, 1.01746573, 1.42678712, 2.23928134, 2.54740085, 2.06971526, 3.49757359, 0.33133045, 0.01313545])
#     predictByPBML_BP3(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_1100000_training_pbml_bp3', 
#                     [1.1677518, 1.0204268, 1.4445000, 2.1712955, 2.4278582, 1.8371449, 3.4127033, 0.2757639, 0.3365404, 0.2860151, 0.5574621, 0.9327317, 1.3185340, 0.6510481])
#     
#     print('Type others: ')
#     predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_others_test_baseN7', 
#                     0.3452315, 1.236304)
#     predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test', 
#                     workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_others_test_baseI7', 
#                     [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
#     predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test', 
#                   workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_others_test_pbml', 
#                     [1.221962, 1.466071, 1.107178, 1.195812, 1.175891, 1.413031, 1.431739])
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_others_test_pbml_bp', 
#                     [0.9234874, 1.3241801, 1.1098779, 1.1782202, 1.1850964, 1.2139418, 1.3704516, 0.5497892])
#     predictByPBML_BP2(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_others_test_pbml_bp2', 
#                     [0.9397577, 1.3175548, 1.1060454, 1.1753779, 1.1795415, 1.2099109, 1.3601354, 0.5727515, -0.2098142])
#     predictByPBML_BP3(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_others_test_pbml_bp3', 
#                     [0.9972825, 1.3554087, 1.1079926, 1.1348593, 1.1580822, 1.2597280, 1.2199951, 0.2957532, 0.2267084, 0.5071388, 0.8832313, 0.6499500, 0.4220974, 1.3271604])
#     print('training')
#     predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_others_training_pbml_bp', 
#                     [0.9234874, 1.3241801, 1.1098779, 1.1782202, 1.1850964, 1.2139418, 1.3704516, 0.5497892])
#     predictByPBML_BP2(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_others_training_pbml_bp2', 
#                     [0.9397577, 1.3175548, 1.1060454, 1.1753779, 1.1795415, 1.2099109, 1.3601354, 0.5727515, -0.2098142])
#     predictByPBML_BP3(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_training', 
#                      workpath + 'analysis/2_predict_value/PBML+BP3/150801+151017/rse_others_training_pbml_bp3', 
#                     [0.9972825, 1.3554087, 1.1079926, 1.1348593, 1.1580822, 1.2597280, 1.2199951, 0.2957532, 0.2267084, 0.5071388, 0.8832313, 0.6499500, 0.4220974, 1.3271604])
#     
    