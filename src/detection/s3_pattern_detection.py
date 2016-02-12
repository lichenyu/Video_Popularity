# -*- coding: utf-8 -*-

def getPct(vcilist):
    s = sum(vcilist)
    pctList = []
    for vci in vcilist:
        if 0 == s:
            pctList.append(0)
        else:
            pctList.append(vci * 1. / s)
    return pctList

def getPctInfo(infile, outfile, indidate):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        outFd.write(line)
        fields = line.strip().split('\t', -1)
        vciList = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vciList.append(int(fie))
        totalPcts = getPct(vciList)
        outFd.write(fields[0])
        for pct in totalPcts:
            outFd.write('\t' + str('%.02f' % pct))
        outFd.write('\n')
        indiPcts = getPct(vciList[0 : 0 + indidate])
        outFd.write(fields[0])
        for pct in indiPcts:
            outFd.write('\t' + str('%.02f' % pct))
        outFd.write('\n')
    inFd.close()
    outFd.close()

def getIndiPattern(infile, outfile, indidate):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vciList = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vciList.append(int(fie))
        indiPcts = getPct(vciList[0 : 0 + indidate])
        stateList = []
        # get state list
        for pct in indiPcts:
            if 3 * 1. / 7 > pct:
                stateList.append(0)
            else:
                stateList.append(1)
        # get new pattern from state list
        for i in range(0, 0 + indidate - 1):
            if (1 == stateList[i]) and (0 == stateList[i + 1]) and (1. / 7 < indiPcts[i + 1]):
                stateList[i + 1] = 1
        for i in range(6, 0, -1):
            if (1 == stateList[i]) and (0 == stateList[i - 1]) and (1. / 7 < indiPcts[i - 1]):
                stateList[i - 1] = 1
        # output
        outFd.write(fields[0] + '\t')
        for state in stateList:
            outFd.write(str(state))
        outFd.write('\n')
    inFd.close()
    outFd.close()
    
def countIndiPattern(infile, outfile):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    # pattern, count
    patternMap = {}
    total = 0
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, pattern
        if False == (fields[1] in patternMap):
            patternMap[fields[1]] = 1
        else:
            patternMap[fields[1]] = patternMap[fields[1]] + 1
        total = total + 1
    patternMapSorted = sorted(patternMap.items(), lambda i1, i2: cmp(i1[1], i2[1]), reverse = True)
    for state in patternMapSorted:
        outFd.write(state[0] + '\t' + str(state[1]) + '\t%.02f' % (state[1] * 100. / total) + '%\n')
    inFd.close()
    outFd.close()
    
def getRecordsByPattern(recordFile, patternFile, patterns):
    outFdList = []
    for p in patterns:
        outFdList.append(open(recordFile + '_' + p, 'w'))
    outFdList.append(open(recordFile + '_others', 'w'))
    
    patternFd = open(patternFile, 'r')
    videoPatternMap = {}
    for line in patternFd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, pattern
        videoPatternMap[fields[0]] = fields[1] 
    patternFd.close()

    recordFd = open(recordFile, 'r')
    for line in recordFd.readlines():
        fields = line.strip().split('\t', -1)
        curPattern = videoPatternMap[fields[0]]
        if curPattern in patterns:
            outFdList[patterns.index(curPattern)].write(line)
        else:
            outFdList[len(patterns)].write(line)
    recordFd.close()
    for fd in outFdList:
        fd.close()
