# split one file into two files
def splitFile(infile, outfile1, outfile2):
    inFd = open(infile, 'r')
    out1Fd = open(outfile1, 'w')
    out2Fd = open(outfile2, 'w')
    lineNum = 0
    for line in inFd.readlines():
        if 0 == lineNum % 2:
            out1Fd.write(line)
        else:
            out2Fd.write(line)
        lineNum = lineNum + 1
    inFd.close()
    out1Fd.close()
    out2Fd.close()

def splitFileWithActive(infile, outfile1, outfile2, minvc7):
    inFd = open(infile, 'r')
    out1Fd = open(outfile1, 'w')
    out2Fd = open(outfile2, 'w')
    lineNum = 0
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vci7list = []
        for i in range(1, 1 + 7):
            vci7list.append(int(fields[i]))
        if minvc7 > sum(vci7list):
            continue
        if 0 == lineNum % 2:
            out1Fd.write(line)
        else:
            out2Fd.write(line)
        lineNum = lineNum + 1
    inFd.close()
    out1Fd.close()
    out2Fd.close()

def splitFileWithInactive(infile, outfile1, outfile2, maxvc7):
    inFd = open(infile, 'r')
    out1Fd = open(outfile1, 'w')
    out2Fd = open(outfile2, 'w')
    lineNum = 0
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vci7list = []
        for i in range(1, 1 + 7):
            vci7list.append(int(fields[i]))
        if maxvc7 <= sum(vci7list):
            continue
        if 0 == lineNum % 2:
            out1Fd.write(line)
        else:
            out2Fd.write(line)
        lineNum = lineNum + 1
    inFd.close()
    out1Fd.close()
    out2Fd.close()


# merge multiple files into one file
def mergeFile(infiles, outfile):
    outFd = open(outfile, 'w')
    for infile in infiles:
        inFd = open(infile, 'r')
        for line in inFd.readlines():
            outFd.write(line)
        inFd.close()
    outFd.close()
    