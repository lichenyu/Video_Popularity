# -*- coding: utf-8 -*-
import pubfunc

def getN7N30(infiles, outfile, positiveCheck = True):
    outFd = open(outfile.decode('UTF-8'), 'w')
    for infile in infiles:
        inFd = open(infile.decode('UTF-8'), 'r')
        for line in inFd.readlines():
            fields = line.strip().split('\t')
            # vid, n1, n2, ..., n30, ...
            if 30 + 1 <= len(fields):
                if positiveCheck and 0 == int(fields[30]):
                    continue
                outFd.write(fields[0] + '\t' + fields[7] + '\t' + fields[30] + '\n')
        inFd.close()
    outFd.close()
    
# def getN7N30_positive(infiles, outfile):
#     outFd = open(outfile.decode('UTF-8'), 'w')
#     for infile in infiles:
#         inFd = open(infile.decode('UTF-8'), 'r')
#         for line in inFd.readlines():
#             fields = line.strip().split('\t')
#             if 30 + 1 <= len(fields) and 0 < int(fields[7]):
#                 outFd.write(fields[0] + '\t' + fields[7] + '\t' + fields[30] + '\n')
#         inFd.close()
#     outFd.close()
    
# -----check n30 == 0
def getI7N30(infiles, outfile, positiveCheck = True):
    outFd = open(outfile.decode('UTF-8'), 'w')
    n7List = []
    for infile in infiles:
        inFd = open(infile.decode('UTF-8'), 'r')
        for line in inFd.readlines():
            fields = line.strip().split('\t')
            # vid, n1, n2, n3, ... , n30, ...
            if 30 + 1 <= len(fields):
                if positiveCheck and 0 == int(fields[30]):
                    continue
                for i in range(1, 7 + 1):
                    n7List.append(int(fields[i]))
                i7List = pubfunc.getVciByVc(n7List)
                outFd.write(fields[0])
                for i in range(0, 7):
                    outFd.write('\t' + str(i7List[i]))
                outFd.write('\t' + fields[30] + '\n')
                n7List = []
        inFd.close()
    outFd.close()

if __name__ == '__main__':
    infiles = ['F:\\Video_Popularity\\rawdata\\151017-151115', 'F:\\Video_Popularity\\rawdata\\1500801-150901']
    getN7N30(infiles, 'F:\\Video_Popularity\\rawdata\\N7N30')
    getI7N30(infiles, 'F:\\Video_Popularity\\rawdata\\I7N30')
    print('All Done!')