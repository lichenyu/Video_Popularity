# -*- coding: utf-8 -*-

import info_crawler as crawler

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
    
# # get NxN30 and IxN30 for a I30 file 
# def getNIxN30(infile, outNfile, outIfile, x):
#     inFd = open(infile.decode('UTF-8'), 'r')
#     outNFd = open(outNfile.decode('UTF-8'), 'w')
#     outIFd = open(outIfile.decode('UTF-8'), 'w')
#     for line in inFd.readlines():
#         vcilist = []
#         fields = line.strip().split('\t')
#         # vid, n1, n2, n3, ... , n30
#         for i in range(1, 1 + 30):
#             vcilist.append(int(fields[i]))
#         # NxN30 output
#         outNFd.write(fields[0] + '\t' + str(sum(vcilist[0 : x])) + '\t' + str(sum(vcilist)) + '\t')
#         # IxN30 output
#         outIFd.write(fields[0])
#         for i in range(1, 1 + x):
#             outIFd.write('\t' + fields[i])
#         outIFd.write('\t' + str(sum(vcilist)) + '\n')
#     inFd.close()
#     outNFd.close()
#     outIFd.close()


if __name__ == '__main__':
    workpath = 'F:/Video_Popularity/'
#     infiles = [workpath + 'rawdata/150801+151017/151017-151115', workpath + 'rawdata/150801+151017/150801-150901']
#     getN30(infiles, workpath + 'rawdata/150801+151017/N30')
#     getI30(infiles, workpath + 'rawdata/150801+151017/I30')
#     getNxN30(workpath + 'rawdata/150801+151017/N30', workpath + 'rawdata/150801+151017/N7N30', 7)
#     getIxN30(workpath + 'rawdata/150801+151017/I30', workpath + 'rawdata/150801+151017/I7N30', 7)
    crawler.getVideoMetadata(workpath + 'rawdata/150801+151017/N30', workpath + 'rawdata/150801+151017/VideoMetadata')
    crawler.getUserList(workpath + 'rawdata/150801+151017/VideoMetadata', workpath + 'rawdata/150801+151017/UserList')
    crawler.getUserMetadata(workpath + 'rawdata/150801+151017/UserList', workpath + 'rawdata/150801+151017/UserMetadata')
    print('All Done!')