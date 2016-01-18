# -*- coding: utf-8 -*-

import dataset_generator

def getPercentage(vcilist):
    s = sum(vcilist)
    pctList = []
    for vci in vcilist:
        if 0 == s:
            pctList.append(0)
        else:
            pctList.append(vci * 1. / s)
    return pctList

def getI7I30Pct(infile, outfile):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        outFd.write(line)
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vcilist.append(int(fie))
        pct30List = getPercentage(vcilist)
        pct7List = getPercentage(vcilist[0 : 0 + 7])
        outFd.write(fields[0])
        for pct in pct30List:
            outFd.write('\t' + str('%.02f' % pct))
        outFd.write('\n')
        outFd.write(fields[0])
        for pct in pct7List:
            outFd.write('\t' + str('%.02f' % pct))
        outFd.write('\n')
        #outFd.write(str(burst_detector.hasBurst(vcilist, 7, 0.1)) + '\n')
    inFd.close()
    outFd.close()
    
def getI7Pattern(infile, outfile):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
#         outFd.write(line)
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vcilist.append(int(fie))
        # get pct
        pct7List = getPercentage(vcilist[0 : 0 + 7])
        statelist = []
        # get pattern
        for pct in pct7List:
            if 2 * 1. / 7 > pct:
                statelist.append(0)
            else:
                statelist.append(1)
#         outFd.write(fields[0] + '\t' + str(statelist) + '\n')
        outFd.write(fields[0] + '\t')
        for state in statelist:
            outFd.write(str(state))
        outFd.write('\n')
    inFd.close()
    outFd.close()
    
# consider burst
def getI7Pattern_2(infile, outfile):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
#         outFd.write(line)
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vcilist.append(int(fie))
        # get pct
        pct7List = getPercentage(vcilist[0 : 0 + 7])
        statelist = []
        # get pattern
        for pct in pct7List:
            if 2 * 1. / 7 > pct:
                statelist.append(0)
            elif 0.8 > pct:
                statelist.append(1)
            else:
                statelist.append(2)
#         outFd.write(fields[0] + '\t' + str(statelist) + '\n')
        outFd.write(fields[0] + '\t')
        for state in statelist:
            outFd.write(str(state))
        outFd.write('\n')
    inFd.close()
    outFd.close()
    
# consider more-or-less fast closed to fast 
def getI7NewPattern(infile, outfile):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vcilist.append(int(fie))
        # get pct
        pct7List = getPercentage(vcilist[0 : 0 + 7])
        statelist = []
        # get state list
        for pct in pct7List:
            if 3 * 1. / 7 > pct:
                statelist.append(0)
            else:
                statelist.append(1)
                
        # get new pattern from state list
        # check back
        for i in range(0, 0 + 6):
            if (1 == statelist[i]) and (0 == statelist[i + 1]) and (1. / 7 < pct7List[i + 1]):
                statelist[i + 1] = 1
        # check forward
        for i in range(6, 0, -1):
            if (1 == statelist[i]) and (0 == statelist[i - 1]) and (1. / 7 < pct7List[i - 1]):
                statelist[i - 1] = 1
                
#         outFd.write(line)
#         outFd.write(fields[0])
#         for pct in pct7List:
#             outFd.write('\t' + str('%.02f' % pct))
#         outFd.write('\n')
        outFd.write(fields[0] + '\t')
        for state in statelist:
            outFd.write(str(state))
        outFd.write('\n')
    inFd.close()
    outFd.close()
    
def countI7Pattern(infile, outfile):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    patternCountMap = {}
    total = 0
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, pattern
        if False == (fields[1] in patternCountMap):
            patternCountMap[fields[1]] = 1
        else:
            patternCountMap[fields[1]] = patternCountMap[fields[1]] + 1
        total = total + 1
    patternCountMapSorted = sorted(patternCountMap.items(), lambda i1, i2: cmp(i1[1], i2[1]), reverse = True)
    for state in patternCountMapSorted:
        outFd.write(state[0] + '\t' + str(state[1]) + '\t%.02f' % (state[1] * 100. / total) + '%\n')
    inFd.close()
    outFd.close()

# save the records (N or I) of certain pattern
def getRecordByPattern(patternFile, recordFile, pattern, outFile):
    patternFd = open(patternFile, 'r')
    vidList = []
    for line in patternFd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, pattern
        if pattern == fields[1]:
            vidList.append(fields[0])
    patternFd.close()

    recordFd = open(recordFile, 'r')
    outFd = open(outFile, 'w')
    for line in recordFd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, xxx
        if fields[0] in vidList:
            outFd.write(line)
    recordFd.close()
    outFd.close()
    
def getRecordForOtherPatterns(patternFile, recordFile, patterns, outFile):
    patternFd = open(patternFile, 'r')
    vidList = []
    for line in patternFd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, pattern
        if False == (fields[1] in patterns):
            vidList.append(fields[0])
    patternFd.close()

    recordFd = open(recordFile, 'r')
    outFd = open(outFile, 'w')
    for line in recordFd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, xxx
        if fields[0] in vidList:
            outFd.write(line)
    recordFd.close()
    outFd.close()
    
def getPatternRecords(patternFile, recordFile, patterns):
    outfiles = []
    for p in patterns:
        getRecordByPattern(patternFile, recordFile, p, recordFile + '_' + p)
        outfiles.append(recordFile + '_' + p)
    getRecordForOtherPatterns(patternFile, recordFile, patterns, recordFile + '_others')
    outfiles.append(recordFile + '_others')
    return outfiles
    
def getDatesets(infiles, trainingfile, testfile):
    traininglist = []
    testlist = []
    for f in infiles:
        dataset_generator.splitFile(f, f + '_training', f + '_test')
        traininglist.append(f + '_training')
        testlist.append(f + '_test')
    dataset_generator.mergeFile(traininglist, trainingfile)
    dataset_generator.mergeFile(testlist, testfile)
    
def getActiveDatesets(infiles, trainingfile, testfile, minvc7):
    traininglist = []
    testlist = []
    for f in infiles:
        dataset_generator.splitFileWithActive(f, f + '_training', f + '_test', minvc7)
        traininglist.append(f + '_training')
        testlist.append(f + '_test')
    dataset_generator.mergeFile(traininglist, trainingfile)
    dataset_generator.mergeFile(testlist, testfile)
    
def getInactiveDatesets(infiles, trainingfile, testfile, maxvc7):
    traininglist = []
    testlist = []
    for f in infiles:
        dataset_generator.splitFileWithInactive(f, f + '_training', f + '_test', maxvc7)
        traininglist.append(f + '_training')
        testlist.append(f + '_test')
    dataset_generator.mergeFile(traininglist, trainingfile)
    dataset_generator.mergeFile(testlist, testfile)
    

if __name__ == '__main__':
    workpath = 'F:/Video_Popularity/'
    #workpath = '/Users/ouyangshuxin/Documents/work/Video_Popularity/'
    
    # get training/test dataset
#     getDatesets([workpath + 'rawdata/150801+151017/I30'], 
#                 workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_training', 
#                 workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_test')
# 
#     # for training set
#     getI7I30Pct(workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_training', 
#                 workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_training_pct')
#     getI7NewPattern(workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_training', 
#                  workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_training_I7pattern')
#     countI7Pattern(workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_training_I7pattern', 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_training_I7pattern_count')
#     
#     # for test set
#     getI7I30Pct(workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_test', 
#                 workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_test_pct')
#     getI7NewPattern(workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_test', 
#                  workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_test_I7pattern')
#     countI7Pattern(workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_test_I7pattern', 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_test_I7pattern_count')
#       
#     # for total
#     getI7I30Pct(workpath + 'rawdata/150801+151017/I30', 
#                 workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_total_pct')
#     getI7NewPattern(workpath + 'rawdata/150801+151017/I30', 
#                  workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_total_I7pattern')
#     countI7Pattern(workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_total_I7pattern', 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_total_I7pattern_count')
  
    # get pattern records of the training set for para
    getPatternRecords(workpath + 'analysis/2_predict_value/PBML/150801+151017/4patterns/I30_training_I7pattern', 
                      workpath + 'analysis/2_predict_value/PBML/150801+151017/4patterns_bp/randomForest/I30_training_bp_predicted', 
                      ['1000000', '1100000', '0000000'])
    
    # get pattern records of the test set
    getPatternRecords(workpath + 'analysis/2_predict_value/PBML/150801+151017/4patterns/I30_test_I7pattern', 
                      workpath + 'analysis/2_predict_value/PBML/150801+151017/4patterns_bp/randomForest/I30_test_bp_predicted', 
                      ['1000000', '1100000', '0000000'])














# generate dataset

#     # for auto generation
#     getI7I30Pct(workpath + 'rawdata/150801+151017/I30', 
#                 workpath + 'analysis/2_predict_value/PBML/150801+151017_auto/percentage')
#     getI7Pattern(workpath + 'rawdata/150801+151017/I30', 
#                  workpath + 'analysis/2_predict_value/PBML/150801+151017_auto/I7_pattern')
#     countI7Pattern(workpath + 'analysis/2_predict_value/PBML/150801+151017_auto/I7_pattern', 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017_auto/I7_pattern_count')
#     pr = getPatternRecords(workpath + 'analysis/2_predict_value/PBML/150801+151017_auto/I7_pattern', 
#                            workpath + 'rawdata/150801+151017/I30', 
#                            ['1000000', '1100000', '0000000', '0100000', '1010000'], 
#                            workpath + 'analysis/2_predict_value/PBML/150801+151017_auto/')
#     getDatesets(pr, 
#                 workpath + 'analysis/2_predict_value/PBML/150801+151017_auto/I30_training', 
#                 workpath + 'analysis/2_predict_value/PBML/150801+151017_auto/I30_test')

#     # get active dataset
#     getActiveDatesets([workpath + 'rawdata/150801+151017/I30'], 
#                 workpath + 'analysis/2_predict_value/PBML/150801+151017_active/4patterns/I30_active_training', 
#                 workpath + 'analysis/2_predict_value/PBML/150801+151017_active/4patterns/I30_active_test', 
#                 14)
# 
#     # get active dataset
#     getInactiveDatesets([workpath + 'rawdata/150801+151017/I30'], 
#                 workpath + 'analysis/2_predict_value/PBML/150801+151017_active/4patterns/I30_inactive_training', 
#                 workpath + 'analysis/2_predict_value/PBML/150801+151017_active/4patterns/I30_inactive_test', 
#                 14)



    print('All Done!')
