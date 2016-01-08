# -*- coding: utf-8 -*-

def hasBurst(vcilist, indidx, threshold):
#     if 3 * indidx > sum(vcilist[0 : indidx]):
#         return False
    vc = sum(vcilist)
    burst = False
    for vci in vcilist[indidx : 30]:
        if threshold <= (vci * 1. / vc):
            burst = True
            break
    return burst

def addBurstFlag2I(infile, outfile, indidx, threshold):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for i in range(1, 1 + 30):
            vcilist.append(int(fields[i]))
        if hasBurst(vcilist, indidx, threshold):
            outFd.write(line.strip() + '\t1\n')
        else:
            outFd.write(line.strip() + '\t0\n')
    inFd.close()
    outFd.close()
    
def addBurstPrediction2I(infile, prfile, outfile, indidx, threshold):  
    prMap = {}
    prFd = open(prfile, 'r')
    for line in prFd.readlines():
        # vid bp bp_predicted
        fields = line.strip().split('\t', -1)
        prMap[fields[0]] = fields[2]
    prFd.close()
    
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, i1, i2, ..., i30
        if fields[0] in prMap:
            outFd.write(line.strip() + '\t' + prMap[fields[0]] + '\n')
        else:
            vcilist = []
            # vid, i1, i2, ..., i30
            for i in range(1, 1 + 30):
                vcilist.append(int(fields[i]))
            if hasBurst(vcilist, indidx, threshold):
                outFd.write(line.strip() + '\t1\n')
            else:
                outFd.write(line.strip() + '\t0\n')
    inFd.close()
    outFd.close()
    
    
    
    
    
def extractBurstValueRecords(infile, outfile, indidx, threshold):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vcilist.append(int(fie))
        vc = sum(vcilist)
        burst = 0
        for vci in vcilist[indidx : 30]:
            if threshold <= (vci * 1. / vc):
                burst = vci
                break
        if 0 < burst:
            outFd.write(line.strip() + '\t' + str(burst) + '\n')
            
    inFd.close()
    outFd.close()
    
def extractBurstValueRecordsWithMin(infile, outfile, indidx, minpct, minburst):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vcilist.append(int(fie))
        vc = sum(vcilist)
        burst = 0
        for vci in vcilist[indidx : 30]:
            if minpct <= (vci * 1. / vc):
                burst = vci
                break
        if minburst <= burst:
            outFd.write(line.strip() + '\t' + str(burst) + '\n')
            
    inFd.close()
    outFd.close()

if __name__ == '__main__':
    workpath = 'F:/Video_Popularity/'
    
#     addBurstFlag2I(workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_training', 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/training/I30_training_bp', 
#                    7, 0.1)

    print('All Done!')
