
def getTrends(stateSeq):
    trendList = []
    for i in range(1, len(stateSeq)):
        if stateSeq[i-1] > stateSeq[i]:
            trendList.append(-1)
        elif stateSeq[i-1] == stateSeq[i]:
            trendList.append(0)
        else:
            #stateSeq[i-1] < stateSeq[i]
            if (0.2 * stateSeq[i-1]) < (stateSeq[i] - stateSeq[i-1]) and 1 < (stateSeq[i] - stateSeq[i-1]): 
                trendList.append(1)
            else:
                trendList.append(0)
    return trendList

def getMaxEqualDownNum(trendList):
    lastMax = 0
    cur = 0
    for i in range(0, len(trendList)):
        if 0 >= trendList[i]:
            cur = cur + 1
            if cur > lastMax:
                lastMax = cur
        else:
            cur = 0
    return lastMax

if '__main__' == __name__:
    workpath = 'F:/Video_Popularity/'
    
#     # get trend list
#     trendMap = {}
#     fd = open(workpath + 'analysis/2_predict_value/PBML/150801+151017_random_dataset/I30_test_1000000', 'r')
#     for line in fd.readlines():
#         fields = line.strip().split('\t', -1)
#         vciList = []
#         for i in range(1, 1+7):
#             vciList.append(int(fields[i]))
#         trendMap[fields[0]] = []
#         trendList = getTrends(vciList)
#         trendMap[fields[0]].append(trendList)
#         trendMap[fields[0]].append(getMaxEqualDownNum(trendList))
#     fd.close()
#     
#     fd = open(workpath + 'analysis/2_predict_value/PBML/150801+151017_random_dataset/rse_test_1000000_baseI7', 'r')
#     outfd = open(workpath + 'analysis/2_predict_value/PBML/150801+151017_random_dataset/rse_test_1000000_baseI7_trends', 'w')
#     for line in fd.readlines():
#         fields = line.strip().split('\t', -1)
#         if 2 < len(fields):
#             outfd.write(line.strip() + '\t' + str(trendMap[fields[0]][1]) + '\n')
#     fd.close()
#     outfd.close()



    inFd = open(workpath + 'analysis/2_predict_value/PBML/150801+151017_random_dataset/I30_training_0000000', 'r')
    outFd = open(workpath + 'analysis/2_predict_value/PBML/150801+151017_random_dataset_trends/I30_training_0000000', 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vciList = []
        for i in range(1, 1+7):
            vciList.append(int(fields[i]))
        trendList = getTrends(vciList)
        outFd.write(line.strip() + '\t' + str(getMaxEqualDownNum(trendList)) + '\n')
    inFd.close()
    outFd.close()
    
    inFd = open(workpath + 'analysis/2_predict_value/PBML/150801+151017_random_dataset/I30_test_0000000', 'r')
    outFd = open(workpath + 'analysis/2_predict_value/PBML/150801+151017_random_dataset_trends/I30_test_0000000', 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vciList = []
        for i in range(1, 1+7):
            vciList.append(int(fields[i]))
        trendList = getTrends(vciList)
        outFd.write(line.strip() + '\t' + str(getMaxEqualDownNum(trendList)) + '\n')
    inFd.close()
    outFd.close()
    
    print('All Done!')
    
    
    
    
    