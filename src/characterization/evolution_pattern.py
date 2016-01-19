# -*- coding: utf-8 -*-

def mergePattern(patternList):
    pattern = ''
    last = patternList[0]
    pattern = pattern + str(last)
    for i in range(1, len(patternList)):
        if last != patternList[i]:
            last = patternList[i]
            pattern = pattern + str(last)
    return pattern

# extract the popularity evolution pattern for each video from a I file
def extract(infile, outfile, minburst, details):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vciList = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vciList.append(int(fie))
        vc = sum(vciList)
        patternList = []
        for vci in vciList:
            r = vci * 1. / vc
            if minburst <= r:
                patternList.append(1)
            else:
                patternList.append(0)
        # change 101 in patternList to 111
        for i in range(1, 29):
            if 0 == patternList[i] and 1 == patternList[i-1] and 1 == patternList[i+1]:
                patternList[i] = 1
        pattern = mergePattern(patternList)
        
        if False == details:
            outFd.write(fields[0] + '\t' + str(sum(vciList)) + '\t' + pattern + '\n')
        else:
            # details
            outFd.write(line)
            for vci in vciList:
                r = vci * 1. / vc
                outFd.write('%0.2f' % r + '\t')
            outFd.write('\n')
            outFd.write(str(patternList) + '\n')
            outFd.write(pattern + '\n')
        
    inFd.close()
    outFd.close()
    
def count(infile, outfile, minvc = 0):
    patternMap = {}
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    total = 0
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vc, pattern
        if 0 < minvc and minvc > int(fields[1]):
            continue
        if fields[2] in patternMap:
            patternMap[fields[2]] = patternMap[fields[2]] + 1
        else:
            patternMap[fields[2]] = 1
        total = total + 1
    patternMap = sorted(patternMap.items(), lambda i1, i2: cmp(i1[1], i2[1]), reverse = True)
    for pattern in patternMap:
        outFd.write(pattern[0] + '\t' + str(pattern[1]) + '\t%.02f' % (pattern[1] * 100. / total) + '%\n')
    inFd.close()
    outFd.close()

if '__main__' == __name__:
    workpath = 'F:/Video_Popularity/'
    
    extract(workpath + 'rawdata/150801+151017/I30', 
            workpath + 'characterization/3_evolution_pattern/evolution_pattern_details', 
            minburst = 3 * 1. / 30, details = True)
    
    extract(workpath + 'rawdata/150801+151017/I30', 
            workpath + 'characterization/3_evolution_pattern/evolution_pattern', 
            minburst = 3 * 1. / 30, details = False)
    
    count(workpath + 'characterization/3_evolution_pattern/evolution_pattern', 
          workpath + 'characterization/3_evolution_pattern/evolution_pattern_count_all')
    
    count(workpath + 'characterization/3_evolution_pattern/evolution_pattern', 
          workpath + 'characterization/3_evolution_pattern/evolution_pattern_count_active', 
          30)
    
    print('All Done!')