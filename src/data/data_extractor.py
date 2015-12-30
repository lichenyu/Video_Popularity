# -*- coding: utf-8 -*-
    
def getI30(infiles, outfile, positiveCheck = True):
    outFd = open(outfile.decode('UTF-8'), 'w')
    for infile in infiles:
        inFd = open(infile.decode('UTF-8'), 'r')
        for line in inFd.readlines():
            fields = line.strip().split('\t')
            # vid, n1, n2, n3, ... , n30, ...
            if 30 + 1 <= len(fields):
                if positiveCheck and 0 == int(fields[30]):
                    continue
                outFd.write(fields[0] + '\t' + fields[1])
                for i in range(2, 1 + 30):
                    outFd.write('\t' + str(int(fields[i]) - int(fields[i-1])))
                outFd.write('\n')
        inFd.close()
    outFd.close()
    
def getN30(infiles, outfile, positiveCheck = True):
    outFd = open(outfile.decode('UTF-8'), 'w')
    for infile in infiles:
        inFd = open(infile.decode('UTF-8'), 'r')
        for line in inFd.readlines():
            fields = line.strip().split('\t')
            # vid, n1, n2, n3, ... , n30, ...
            if 30 + 1 <= len(fields):
                if positiveCheck and 0 == int(fields[30]):
                    continue
                outFd.write(fields[0])
                for i in range(1, 1 + 30):
                    outFd.write('\t' + fields[i])
                outFd.write('\n')
        inFd.close()
    outFd.close()
    
def getNxN30(infile, outfile, x):
    inFd = open(infile.decode('UTF-8'), 'r')
    outFd = open(outfile.decode('UTF-8'), 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t')
        # vid, n1, n2, n3, ... , n30
        outFd.write(fields[0] + '\t' + fields[x] + '\t' + fields[30] + '\n')
    inFd.close()
    outFd.close()
    
def getIxN30(infile, outfile, x):
    inFd = open(infile.decode('UTF-8'), 'r')
    outFd = open(outfile.decode('UTF-8'), 'w')
    for line in inFd.readlines():
        vcilist = []
        fields = line.strip().split('\t')
        # vid, n1, n2, n3, ... , n30
        for i in range(1, 1 + 30):
            vcilist.append(int(fields[i]))
        outFd.write(fields[0])
        for i in range(1, 1 + x):
            outFd.write('\t' + fields[i])
        outFd.write('\t' + str(sum(vcilist)) + '\n')
    inFd.close()
    outFd.close()


if __name__ == '__main__':
    infiles = ['F:\\Video_Popularity\\rawdata\\150801+151017\\151017-151115', 'F:\\Video_Popularity\\rawdata\\150801+151017\\150801-150901']
    #getN30(infiles, 'F:\\Video_Popularity\\rawdata\\150801+151017\\N30')
    #getI30(infiles, 'F:\\Video_Popularity\\rawdata\\150801+151017\\I30')
    getNxN30('F:\\Video_Popularity\\rawdata\\150801+151017\\N30', 'F:\\Video_Popularity\\rawdata\\150801+151017\\N7N30', 7)
    getIxN30('F:\\Video_Popularity\\rawdata\\150801+151017\\I30', 'F:\\Video_Popularity\\rawdata\\150801+151017\\I7N30', 7)
    print('All Done!')