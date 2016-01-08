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
    rv = [len(rseLogLinearList), sum(rseLogLinearList), len(rseLinearLrsList), sum(rseLinearLrsList)]
    #print(rv)
    return rv
    
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
    rv = [len(rseMultiLinearLrsList), sum(rseMultiLinearLrsList)]
    #print(rv)
    return rv
    
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
    rv = [len(rseMultiLinearLrsList), sum(rseMultiLinearLrsList)]
    #print(rv)
    return rv
    
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
    rv = [len(rseMultiLinearLrsList), sum(rseMultiLinearLrsList)]
    #print(rv)
    return rv
    
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

def evaluateModels(patterns, testprefix, outprefix, logLinearPara, linearLrsPara, multiLinearLrsPara, pbmlParas):
    if len(patterns) != len(pbmlParas):
        return -1
    #rv = [len(rseMultiLinearLrsList), sum(rseMultiLinearLrsList)]
    total = 0
    rseLogLinear = 0
    rseLinear = 0
    rseMultiLinear = 0
    rsePBML = 0
    for i in range(0, len(patterns)):
        print('Pattern ' + patterns[i] + ': ')
        rv = predictByBaseN7(testprefix + patterns[i], 
                             outprefix + patterns[i] + '_baseN7', 
                             logLinearPara, linearLrsPara)
        total = total + rv[0]
        rseLogLinear = rseLogLinear + rv[1]
        rseLinear = rseLinear + rv[3]
        
        rv = predictByBaseI7(testprefix + patterns[i], 
                             outprefix + patterns[i] + '_baseI7', 
                             multiLinearLrsPara)
        rseMultiLinear = rseMultiLinear + rv[1]
        
        rv = predictByPBML(testprefix + patterns[i], 
                           outprefix + patterns[i] + '_pbml', 
                           pbmlParas[i])
        rsePBML = rsePBML + rv[1]
        print('')
    print('Total LogLinear MRSE = ' + str(rseLogLinear/total) + \
          '\nTotal Linear MRSE = ' + str(rseLinear/total) + \
          '\nTotal MultiLinear MRSE = ' + str(rseMultiLinear/total) + \
          '\nTotal PBML MRSE = ' + str(rsePBML/total))
    
def evaluateModels_BP(patterns, testprefix, outprefix, pbmlBpParas):
    if len(patterns) != len(pbmlBpParas):
        return -1
    #rv = [len(rseMultiLinearLrsList), sum(rseMultiLinearLrsList)]
    total = 0
    rsePBML_BP = 0
    for i in range(0, len(patterns)):
        print('Pattern ' + patterns[i] + ': ')
        rv = predictByPBML_BP(testprefix + patterns[i], 
                           outprefix + patterns[i] + '_pbml_bp', 
                           pbmlBpParas[i])
        total = total + rv[0]
        rsePBML_BP = rsePBML_BP + rv[1]
        print('')
    print('Total PBML_BP MRSE = ' + str(rsePBML_BP/total))
        
def evaluateFitting(patterns, testprefix, outprefix, logLinearPara, linearLrsPara, multiLinearLrsPara, pbmlParas):
    if len(patterns) != len(pbmlParas):
        return -1
    for i in range(0, len(patterns)):
        print('Pattern ' + patterns[i] + ': ')
        predictByBaseN7(testprefix + patterns[i], 
                        outprefix + patterns[i] + '_baseN7', 
                        logLinearPara, linearLrsPara)
        predictByBaseI7(testprefix + patterns[i], 
                        outprefix + patterns[i] + '_baseI7', 
                        multiLinearLrsPara)
        predictByPBML(testprefix + patterns[i], 
                      outprefix + patterns[i] + '_pbml', 
                      pbmlParas[i])

if __name__ == '__main__':
    workpath = 'F:/Video_Popularity/'
    #workpath = '/Users/ouyangshuxin/Documents/work/Video_Popularity/'
    
#     evaluateModels(['1000000', '1100000', '0000000', 'others'], 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_test_', 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017/rse_test_', 
#                    0.3462903, 1.234574, 
#                    [1.175979, 1.308160, 1.227412, 1.508363, 1.369082, 1.761802, 2.181996], 
#                    [
#                     [1.177099, 1.297660, 1.190649, 1.574289, 1.383345, 1.701904, 1.952588], 
#                     [1.159775, 1.171434, 1.375740, 1.811068, 2.083094, 2.023532, 3.838278], 
#                     [1.357835, 1.421140, 1.010211, 1.411544, 1.276410, 1.917169, 3.392477], 
#                     [1.292994, 1.170078, 1.124354, 1.163465, 1.144220, 1.238313, 1.373610]
#                     ])
# 
#     print('')
    
    evaluateModels_BP(['1000000', '1100000', '0000000', 'others'], 
                      workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/rpart/I30_test_bp_predicted_', 
                      workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/rpart/rse_test_bp_predicted_', 
                      [
                       [1.13303836, 1.56778510, 1.20767206, 1.58905120, 1.39188641, 1.69839068, 1.95462689, 0.08701042], 
                       [1.15581926, 1.15783083, 1.44377293, 1.80954588, 2.08781147, 2.00973751, 3.84432552, 0.05316459], 
                       [1.3829860, 1.4128814, 1.0033576, 1.4065036, 1.2773998, 1.9314988, 3.3870238, -0.0958026], 
                       [1.28568256, 1.17118281, 1.12463257, 1.16319225, 1.14511441, 1.23762807, 1.37416835, 0.01585824]
                       ])
    
#     
#     evaluateFitting(['1000000', '0000000', '1100000', 'others'], 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017_active/4patterns/I30_active_training_', 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017_active/4patterns/rse_active_training_', 
#                    0.3462903, 1.234574, 
#                    [1.175979, 1.308160, 1.227412, 1.508363, 1.369082, 1.761802, 2.181996], 
#                    [
#                     [1.172852, 1.157283, 1.141730, 1.728174, 1.726009, 1.862370, 2.066463], 
#                     [1.455354, 1.210279, 1.032734, 1.511062, 1.074896, 1.694086, 3.855173], 
#                     [1.143831, 1.151531, 1.380812, 1.954694, 2.124467, 2.421991, 4.125015], 
#                     [1.290821, 1.182476, 1.123870, 1.115366, 1.160633, 1.343272, 1.463081]
#                     ])

    
#     evaluateFitting(['1000000', '1100000', '0000000', '1110000', '0010000', 'others'], 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017_newpattern/', 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017_newpattern/', 
#                    0.3462903, 1.234574, 
#                    [1.175979, 1.308160, 1.227412, 1.508363, 1.369082, 1.761802, 2.181996], 
#                    [
#                     [1.177099, 1.297660, 1.190649, 1.574289, 1.383345, 1.701904, 1.952588], 
#                     [1.159775, 1.171434, 1.375740, 1.811068, 2.083094, 2.023532, 3.838278], 
#                     [1.357835, 1.421140, 1.010211, 1.411544, 1.276410, 1.917169, 3.392477], 
#                     [1.3036099, 1.1794771, 0.9822319, 1.2310219, 0.7703616, 4.8851593, 4.0956121], 
#                     [0.9320525, 1.8519616, 1.0693444, 1.7431395, 2.2926660, 2.0958357, 2.5337601], 
#                     [1.078327, 1.129176, 1.195657, 1.186257, 1.187825, 1.258989, 1.412242]
#                     ])
    
    
#     evaluateModels(['1000000', '1100000', '0000000', '0100000', '1010000', 'others'], 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017_random_dataset/', 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017_random_dataset/', 
#                    0.3462903, 1.234574, 
#                    [1.175979, 1.308160, 1.227412, 1.508363, 1.369082, 1.761802, 2.181996], 
#                    [
#                     [1.161568, 1.312689, 1.244425, 1.682606, 1.494106, 2.120614, 2.875775], 
#                     [1.228459, 1.058724, 1.184574, 2.385043, 2.283053, 1.541102, 4.535384], 
#                     [2.2480531, 1.3150635, 1.1062172, 0.8487065, 1.2022408, 1.3689275, 4.5996419], 
#                     [1.8800013, 0.9997683, 0.9001105, 1.4124715, 1.5416789, 3.3567989, 2.8979119], 
#                     [1.2552717, 1.3788060, 0.8933426, 2.1052292, 2.9542444, 1.4094730, 3.4225826], 
#                     [1.104101, 1.435237, 1.155101, 1.240993, 1.238420, 1.385056, 1.531328]
#                     ])

#     evaluateModels(['1000000', '1100000', '0000000', '0100000', '1010000', 'others'], 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017_auto/', 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017_auto/', 
#                    0.3452315, 1.236304, 
#                    [1.180141, 1.290875, 1.236982, 1.533545, 1.369576, 1.767452, 2.133439], 
#                    [
#                     [1.165725, 1.246080, 1.268853, 1.830004, 1.503788, 1.970634, 3.043560], 
#                     [1.211600, 1.092533, 1.204722, 2.423859, 2.362118, 1.973938, 3.828769], 
#                     [1.8710562, 0.7292189, 1.4115649, 1.2689845, 1.5307522, 0.7547255, 5.7702485], 
#                     [1.7260303, 1.0113645, 1.0631047, 1.8750424, 0.7510338, 3.4531069, 2.4238536], 
#                     [1.248046, 1.041718, 0.970693, 2.397707, 2.101312, 1.510596, 4.089463], 
#                     [1.221962, 1.466071, 1.107178, 1.195812, 1.175891, 1.413031, 1.431739]
#                     ])

#     evaluateModels(['2000000', '1000000', '1100000', '0000000', '0100000', '1010000', '0010000', 'others'], 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2_auto/', 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017_2_auto/', 
#                    0.3484038, 1.235833, 
#                    [1.177785, 1.309063, 1.220432, 1.494015, 1.387594, 1.730061, 2.203738], 
#                    [
#                     [1.1949192, 1.1258028, 0.8759515, 1.2185588, 1.0140954, 1.1790830, 1.6929797], 
#                     [1.020864, 1.650731, 1.402532, 1.805735, 1.689735, 2.170273, 3.326809], 
#                     [1.211600, 1.092533, 1.204722, 2.423859, 2.362118, 1.973938, 3.828769], 
#                     [1.8710562, 0.7292189, 1.4115649, 1.2689845, 1.5307522, 0.7547255, 5.7702485], 
#                     [1.5031454, 0.9552199, 1.2769401, 1.5995035, 0.8891453, 2.9900238, 4.5620508], 
#                     [1.248046, 1.041718, 0.970693, 2.397707, 2.101312, 1.510596, 4.089463], 
#                     [1.431300, 1.022123, 1.002467, 1.347643, 2.042787, 1.361212, 2.747711], 
#                     [1.168850, 1.140689, 1.132781, 1.235572, 1.254579, 1.411175, 1.452834]
#                     ])
    
