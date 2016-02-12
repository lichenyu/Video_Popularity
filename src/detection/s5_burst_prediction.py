# -*- coding: utf-8 -*-

def getPredictionResults(labelfile, prdfile, outfile):
    prdMap = {}
    prdFd = open(prdfile, 'r')
    for line in prdFd.readlines():
        # vid, bl, bp
        fields = line.strip().split('\t', -1)
        prdMap[fields[0]] = fields[2]
    prdFd.close()
    
    inFd = open(labelfile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, i1, i2, ..., i30
        if fields[0] in prdMap:
            outFd.write(fields[0])
            for i in range(1, 1 + 30):
                outFd.write('\t' + fields[i])
            outFd.write('\t' + prdMap[fields[0]] + '\n')
        # for the vids without metadata
        else:
            outFd.write(line)
    inFd.close()
    outFd.close()
    