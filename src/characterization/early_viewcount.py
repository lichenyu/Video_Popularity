# -*- coding: utf-8 -*-

# extract the popularity evolution pattern for each video from a I file
def extractBurstAfter7(infile, outfile, minburst):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vciList = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vciList.append(int(fie))
        vc = sum(vciList)
        for i in range(7, 30):
            r = vciList[i] * 1. / vc
            if minburst <= r:
                outFd.write(line)
                break
    inFd.close()
    outFd.close()
    
def getRecordByPattern(patternFile, recordFile, pattern, outFile):
    patternFd = open(patternFile, 'r')
    vidList = []
    for line in patternFd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vc, pattern
        if pattern == fields[2]:
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
    
def getOtherRecords(curFiles, recordFile, outFile):
    vidSet = set()
    for f in curFiles:
        curFd = open(f, 'r')
        for line in curFd.readlines():
            fields = line.strip().split('\t', -1)
            # vid, vci...
            if False == (fields[0] in vidSet):
                vidSet.add(fields[0])
        curFd.close()
    recordFd = open(recordFile, 'r')
    outFd = open(outFile, 'w')
    for line in recordFd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci...
        if False == (fields[0] in vidSet):
            outFd.write(line)
    recordFd.close()
    outFd.close()

if __name__ == '__main__':
    workpath = 'F:/Video_Popularity/'
    
    extractBurstAfter7(workpath + 'rawdata/150801+151017/I30', 
                       workpath + 'characterization/4_early_stage/I30_burst_after7', 
                       minburst = 3 * 1. / 30)
    getRecordByPattern(workpath + 'characterization/3_evolution_pattern/evolution_pattern', 
                       workpath + 'rawdata/150801+151017/I30', 
                       '0', 
                       workpath + 'characterization/4_early_stage/I30_pattern0', 
                       )
    getOtherRecords([
                     workpath + 'characterization/4_early_stage/I30_burst_after7', 
                     workpath + 'characterization/4_early_stage/I30_pattern0'
                     ], 
                    workpath + 'rawdata/150801+151017/I30', 
                    workpath + 'characterization/4_early_stage/I30_others')
    
    print('All Done!')