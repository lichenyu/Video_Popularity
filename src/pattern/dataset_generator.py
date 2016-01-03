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

# merge multiple files into one file
def mergeFile(infiles, outfile):
    outFd = open(outfile, 'w')
    for infile in infiles:
        inFd = open(infile, 'r')
        for line in inFd.readlines():
            outFd.write(line)
        inFd.close()
    outFd.close()
    