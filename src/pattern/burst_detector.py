# -*- coding: utf-8 -*-

def hasBurst(vcilist, indidx, threshold):
    vc = sum(vcilist)
    burst = False
    for vci in vcilist[indidx : 30]:
        if threshold <= (vci * 1. / vc):
            burst = True
    return burst

def addBurstFlag2I(infile, outfile, indidx, threshold):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vcilist.append(int(fie))
        vc = sum(vcilist)
        burst = False
        for vci in vcilist[indidx : 30]:
            if threshold <= (vci * 1. / vc):
                burst = True
        if burst:
            outFd.write(line.strip() + '\t1\n')
        else:
            outFd.write(line.strip() + '\t0\n')
    inFd.close()
    outFd.close()

if __name__ == '__main__':
    print(hasBurst([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                   7, 
                   0.1))

    print('All Done!')
