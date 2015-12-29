from tarfile import LENGTH_LINK

#def detectBurst(vcilist):
    
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
    if((3 * 1. / 30) >= pctList[0]):
        return False
    else:
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
        vci7list = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 7]:
            vci7list.append(int(fie))
        pct7List = getPercentage(vci7list) 
#         outFd.write(fields[0])
#         for pct in pct7List:
#             outFd.write('\t' + str('%.06f' % pct))
#         outFd.write('\n')
#         for s in getAverageRateAfterBurst(pct7List):
#             outFd.write(str('%.06f\t' % s))
#         outFd.write('\n')
        #outFd.write(str(sum(getAverageRateAfterBurst(pct7List)) / len(getAverageRateAfterBurst(pct7List))) + '\n')
        #outFd.write('%.06f\n' % getAverageRateAfterBurst(pct7List))
        outFd.write(fields[0] + '\t' + '%.06f\n' % getAverageRateAfterBurst(pct7List))
    inFd.close()
    outFd.close()
    
def getI7N30(infile, outfile):

def getN7N30(infile, outfile):    

if __name__ == '__main__':
    #getI30Pct('F:\\Video_Popularity\\rawdata\\I30', 'percentage')
    
    # get type data
    #getBurstSlow('F:\\Video_Popularity\\rawdata\\I30', 'I30_BurstSlow')
    getRateForBurstSlow('I30_BurstSlow', 'BurstSlow_rate')
    
    print('All Done!')