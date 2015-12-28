# -*- coding: utf-8 -*-

def getN7N30(infiles, outfile):
    outFd = open(outfile.decode('UTF-8'), 'w')
    for infile in infiles:
        inFd = open(infile.decode('UTF-8'), 'r')
        for line in inFd.readlines():
            fields = line.strip().split('\t')
            if 30 + 1 <= len(fields):
                outFd.write(fields[0] + '\t' + fields[1] + '\t' + fields[30] + '\n')
        inFd.close()
    outFd.close()
    
def getN7N30_positive(infiles, outfile):
    outFd = open(outfile.decode('UTF-8'), 'w')
    for infile in infiles:
        inFd = open(infile.decode('UTF-8'), 'r')
        for line in inFd.readlines():
            fields = line.strip().split('\t')
            if 30 + 1 <= len(fields) and 0 < int(fields[1]):
                outFd.write(fields[0] + '\t' + fields[1] + '\t' + fields[30] + '\n')
        inFd.close()
    outFd.close()

if __name__ == '__main__':
    infiles = ['C:\\Documents and Settings\\Administrator\\桌面\\vc\\data\\151017-151115', 'C:\\Documents and Settings\\Administrator\\桌面\\vc\\data\\1500801-150901']
    #getN7N30(infiles, 'C:\\Documents and Settings\\Administrator\\桌面\\vc\\data\\N7N30')
    getN7N30_positive(infiles, 'C:\\Documents and Settings\\Administrator\\桌面\\vc\\data\\N7N30_p')
    print('All Done!')