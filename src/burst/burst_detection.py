# -*- coding: utf-8 -*-

import data.data_extractor as data_extractor

def getPercentage(vcilist):
    s = sum(vcilist)
    pctList = []
    for vci in vcilist:
        if 0 == s:
            pctList.append(0)
        else:
            pctList.append(vci * 1. / s)
    return pctList

def getI30Pct(infile, outfile):
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
        outFd.write(fields[0])
        for pct in pct30List:
            outFd.write('\t' + str('%.02f' % pct))
        outFd.write('\n')
    inFd.close()
    outFd.close()

def typeBurstSlow(pctList):
    # not begin with burst
    if((3 * 1. / 30) >= pctList[0]):
        return False
    else:
        # check if has more than 1 burst
        flag = True
        for pct in pctList[1 : 30]:
            if (3 * 1. / 30) < pct:
                if False == flag:
                    return False
            else:
                flag = False
        return True
    
def getBurstSlow(infile, outfile):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vcilist.append(int(fie))
        pct30List = getPercentage(vcilist)
        if typeBurstSlow(pct30List):
            outFd.write(line)
    inFd.close()
    outFd.close()
    
def typeSteady(pctList):
    for pct in pctList:
        if (3 * 1. / 30) < pct:
            return False
    return True

def getAverageRateAfterBurst(pctlist):
    # find burst (vci > 2. * 1 / length(vcilist))
    idx = 0
    for i in range(len(pctlist)-1, -1, -1):
        if (2. / len(pctlist)) < pctlist[i]:
            idx = i
    while (1. / len(pctlist)) < pctlist[idx + 1]:
        idx = idx + 1
    #return pctlist[idx + 1 : len(pctlist)]
    return sum(pctlist[idx + 1 : len(pctlist)]) / len(pctlist[idx + 1 : len(pctlist)])
        
def getRateForBurstSlow(infile, outfile):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
#         outFd.write(line)
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vcilist.append(int(fie))
        pct7List = getPercentage(vcilist[0:7]) 
        #outFd.write(fields[0] + '\t' + '%.06f\n' % getAverageRateAfterBurst(pct7List) \
        outFd.write(fields[0] + '\t' + str(sum(vcilist[0:7])) + '\t' + str(sum(vcilist)) \
                    + '\t' + str(getAverageRateAfterBurst(pct7List)) + '\n')
    inFd.close()
    outFd.close()
    
def getI7N30(infile, outfile):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vcilist.append(int(fie))
        outFd.write(fields[0])
        for i in range(0, 7):
            outFd.write('\t' + str(vcilist[i]))
        outFd.write('\t' + str(sum(vcilist)) + '\n')
    inFd.close()
    outFd.close()
 
def getN7N30(infile, outfile):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vcilist.append(int(fie))
        outFd.write(fields[0] + '\t' + str(sum(vcilist[0:7])) + '\t' + str(sum(vcilist)) + '\n')
    inFd.close()
    outFd.close()

if __name__ == '__main__':
    getI30Pct('F:\\Video_Popularity\\rawdata\\150801+151017\\I30', 
              'F:\\Video_Popularity\\src\\burst\\150801+151017\\percentage')
    
    # get type data
    getBurstSlow('F:\\Video_Popularity\\rawdata\\150801+151017\\I30', 
                 'F:\\Video_Popularity\\src\\burst\\150801+151017\\I30_BurstSlow')
    data_extractor.getNIxN30('F:\\Video_Popularity\\src\\burst\\150801+151017\\I30_BurstSlow', 
                            'F:\\Video_Popularity\\src\\burst\\150801+151017\\N7N30_BurstSlow', 
                            'F:\\Video_Popularity\\src\\burst\\150801+151017\\I7N30_BurstSlow', 7)
    #getN7N30('I30_BurstSlow', 'N7N30_BurstSlow')
    #getI7N30('I30_BurstSlow', 'I7N30_BurstSlow')
    #getRateForBurstSlow('I30_BurstSlow', 'BurstSlow_rate')
    
    print('All Done!')