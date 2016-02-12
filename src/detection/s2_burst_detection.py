# -*- coding: utf-8 -*-

def detectBurst(infile, outfile, indidate, threshold):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vciList = []
        # vid, i1, i2, ..., i30
        for i in range(1, 1 + 30):
            vciList.append(int(fields[i]))
        vc = sum(vciList)
        burst = False
        for vci in vciList[indidate : 30]:
            if threshold <= (vci * 1. / vc):
                burst = True
                break
        if True == burst:
            outFd.write(line.strip() + '\t1\n')
        else:
            outFd.write(line.strip() + '\t0\n')
    inFd.close()
    outFd.close()
