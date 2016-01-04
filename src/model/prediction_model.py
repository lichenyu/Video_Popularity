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
        # id, i1, ..., i30
        iList = []
        for i in range(1, 1 + 31):
            iList.append(int(fields[i]))
        obsN30 = sum(iList[0:30])
        predictionFd.write(fields[0] + '\t' + str(obsN30))
        fList = iList[0 : 7]
        fList.append(iList[30]*sum(iList[0:7]))
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
    
    

if __name__ == '__main__':
    workpath = 'F:/Video_Popularity/'
    
    print('Type 0000000: ')
    predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test', 
                    workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0000000_test_baseN7', 
                    0.3452315, 1.236304)
    predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test', 
                    workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0000000_test_baseI7', 
                    [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
    predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test', 
                  workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0000000_test_pbml', 
                    [1.8710562, 0.7292189, 1.4115649, 1.2689845, 1.5307522, 0.7547255, 5.7702485])
    predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test', 
                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0000000_test_pbml_bp', 
                    [1.7614136, 0.7850340, 1.5547683, 1.1535014, 1.3793718, 0.8130685, 5.4033738, 0.2575609])
    
    print('Type 1000000: ')
    predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test', 
                    workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1000000_test_baseN7', 
                    0.3452315, 1.236304)
    predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test', 
                    workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1000000_test_baseI7', 
                    [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
    predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test', 
                  workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1000000_test_pbml', 
                    [1.165725, 1.246080, 1.268853, 1.830004, 1.503788, 1.970634, 3.043560])
    predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test', 
                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1000000_test_pbml_bp', 
                    [1.057131, 1.383293, 1.340171, 1.776463, 1.652662, 1.954112, 2.799800, 0.330536])
    
    print('Type 0100000: ')
    predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test', 
                    workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0100000_test_baseN7', 
                    0.3452315, 1.236304)
    predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test', 
                    workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0100000_test_baseI7', 
                    [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
    predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test', 
                  workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0100000_test_pbml', 
                    [1.7260303, 1.0113645, 1.0631047, 1.8750424, 0.7510338, 3.4531069, 2.4238536])
    predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test', 
                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_0100000_test_pbml_bp', 
                    [1.5193861, 0.9575424, 1.0533085, 2.2046819, 0.7254957, 3.4022394, 2.0214843, 0.4183901])
    
    print('Type 1010000: ')
    predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test', 
                    workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1010000_test_baseN7', 
                    0.3452315, 1.236304)
    predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test', 
                    workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1010000_test_baseI7', 
                    [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
    predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test', 
                  workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1010000_test_pbml', 
                    [1.248046, 1.041718, 0.970693, 2.397707, 2.101312, 1.510596, 4.089463])
    predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test', 
                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1010000_test_pbml_bp', 
                    [0.9158504, 1.3290235, 1.1209561, 1.5431008, 2.7434331, 1.3978658, 2.5385364, 0.3780278])
    
    print('Type 1100000: ')
    predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test', 
                    workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1100000_test_baseN7', 
                    0.3452315, 1.236304)
    predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test', 
                    workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1100000_test_baseI7', 
                    [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
    predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test', 
                  workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1100000_test_pbml', 
                    [1.211600, 1.092533, 1.204722, 2.423859, 2.362118, 1.973938, 3.828769])
    predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test', 
                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_1100000_test_pbml_bp', 
                    [1.1565211, 1.0175316, 1.4262594, 2.2382570, 2.5459688, 2.0686217, 3.4963375, 0.3323833])
    
    print('Type others: ')
    predictByBaseN7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test', 
                    workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_others_test_baseN7', 
                    0.3452315, 1.236304)
    predictByBaseI7(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test', 
                    workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_others_test_baseI7', 
                    [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439])
    predictByPBML(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test', 
                  workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_others_test_pbml', 
                    [1.221962, 1.466071, 1.107178, 1.195812, 1.175891, 1.413031, 1.431739])
    predictByPBML_BP(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test', 
                     workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/rse_others_test_pbml_bp', 
                    [0.9234874, 1.3241801, 1.1098779, 1.1782202, 1.1850964, 1.2139418, 1.3704516, 0.5497892])
    