# -*- coding: utf-8 -*-

def splitDatesets(infiles, trainingOut, testOut):
    trainingFd = open(trainingOut, 'w')
    testFd = open(testOut, 'w')
    for f in infiles:
        inFd = open(f, 'r')
        lineNum = 0
        for line in inFd.readlines():
            if 0 == lineNum % 2:
                trainingFd.write(line)
            else:
                testFd.write(line)
            lineNum = lineNum + 1
        inFd.close()
    trainingFd.close()
    testFd.close()
