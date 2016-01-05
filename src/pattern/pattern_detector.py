# -*- coding: utf-8 -*-

import dataset_generator
import burst_detector

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
        outFd.write(str(burst_detector.hasBurst(vcilist, 7, 0.1)) + '\n')
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

if __name__ == '__main__':
    workpath = 'F:/Video_Popularity/'

#     getI7I30Pct(workpath + 'rawdata/150801+151017/I30', 
#                 workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/percentage')
#     burst_detector.addBurstFlag2I(workpath + 'rawdata/150801+151017/I30', 
#                                   workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_BP', 
#                                   7, 0.1)
    burst_detector.extractBurstRecords(workpath + 'rawdata/150801+151017/I30', 
                                       workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_BP_value', 
                                       7, 0.1)
#     getI7Pattern(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_BP', 
#                  workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I7_pattern')
#     countI7Pattern(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I7_pattern', 
#                    workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I7_pattern_count')
#     
#     # rank 1
#     getRecordByPattern(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I7_pattern', 
#                        workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_BP', 
#                        '1000000', 
#                        workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000')
#     # rank 2
#     getRecordByPattern(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I7_pattern', 
#                        workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_BP', 
#                        '1100000', 
#                        workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000')
#     # rank 3
#     getRecordByPattern(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I7_pattern', 
#                        workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_BP', 
#                        '0000000', 
#                        workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000')    
#     # rank 4
#     getRecordByPattern(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I7_pattern', 
#                        workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_BP', 
#                        '0100000', 
#                        workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000')
#     # rank 5
#     getRecordByPattern(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I7_pattern', 
#                        workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_BP', 
#                        '1010000', 
#                        workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000')
#     # others
#     getRecordForOtherPatterns(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I7_pattern', 
#                              workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_BP', 
#                              ['1000000', '1100000', '0000000', '0100000', '1010000'], 
#                              workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others')
# 
#     dataset_generator.splitFile(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000', 
#                                 workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_training', 
#                                 workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_test')
#     
#     dataset_generator.splitFile(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000', 
#                                 workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_training', 
#                                 workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_test')
#     
#     dataset_generator.splitFile(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000', 
#                                 workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_training', 
#                                 workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_test')
#     
#     dataset_generator.splitFile(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000', 
#                                 workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_training', 
#                                 workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_test')
#     
#     dataset_generator.splitFile(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000', 
#                                 workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_training', 
#                                 workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_test')
#     
#     dataset_generator.splitFile(workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others', 
#                                 workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_training', 
#                                 workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_test')
#      
#     dataset_generator.mergeFile(
#                                 [workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1000000_training', 
#                                  workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1100000_training', 
#                                  workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_training', 
#                                  workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0100000_training', 
#                                  workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_1010000_training', 
#                                  workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_training'], 
#                                 workpath + 'analysis/2_predict_value/PBML+BP/150801+151017/I30_training'
#                                 )

    print('All Done!')
