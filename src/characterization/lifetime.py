# -*- coding: utf-8 -*-

import math

# get lifetime of each video in I file
# end point: from which at least mindn inactive days
# active day definition: 
# vci > maxinactive
# or 
# vci * 1. / vc >= minrate and vci >= minactive
def getActiveLifetime(infile, outfile, minvc = 30, maxinactive = 99, minrate = 1./30, minactive = 10, mindn = 5):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vcilist.append(int(fie))
        # inactive videos 
        if(minvc > sum(vcilist)):
            continue
        # try to find end point of lifetime
        vc = sum(vcilist)
        idx = 0
        for i in range(29, 29 - 30, -1):
            # backwards idx 29 -> 0, find first active day
            if maxinactive < vcilist[i] or (minrate <= vcilist[i] * 1. / vc and minactive <= vcilist[i]): 
                idx = i
                break
        inactiveLen = 29 - idx
        
#         # details
#         outFd.write(line)
#         # not end
#         if mindn > inactiveLen:
#             outFd.write(str(inactiveLen) + ' inactive days (not reach), active day idx = ' + str(idx) + ', vci = ' + str(vcilist[idx]) + ', rate = ' + str(vcilist[idx] * 1. / vc) + ', vc = ' + str(vc) + '\n')
#         else:
#             for i in range(idx + 1, 30):
#                 outFd.write(str(vcilist[i]) + '\t')
#             outFd.write('\n')
#             outFd.write(str(inactiveLen) + ' inactive days, active day idx = ' + str(idx) + ', vci = ' + str(vcilist[idx]) + ', rate = ' + str(vcilist[idx] * 1. / vc) + ', vc = ' + str(vc) + '\n')
#         outFd.write('\n')
        
        # not end
        if mindn > inactiveLen:
            outFd.write(fields[0] + '\t31\n')
        else:
            outFd.write(fields[0] + '\t' + str(idx + 1) + '\n')
            
    inFd.close()
    outFd.close()
    
def getInactiveLifetime(infile, outfile, maxvc = 29, maxinactive = 99, minrate = 1./30, minactive = 0.5, mindn = 5):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vcilist.append(int(fie))
        # active videos 
        if(maxvc < sum(vcilist)):
            continue
        # try to find end point of lifetime
        vc = sum(vcilist)
        maxvci = max(vcilist)
        idx = 0
        for i in range(29, 29 - 30, -1):
            # backwards idx 29 -> 0, find first active day
            if maxinactive < vcilist[i] or (minrate <= vcilist[i] * 1. / vc and minactive * maxvci <= vcilist[i]): 
                idx = i
                break
        inactiveLen = 29 - idx
        
#         # details
#         outFd.write(line)
#         # not end
#         if mindn > inactiveLen:
#             outFd.write(str(inactiveLen) + ' inactive days (not reach), active day idx = ' + str(idx) + ', vci = ' + str(vcilist[idx]) + ', rate = ' + str(vcilist[idx] * 1. / vc) + ', vc = ' + str(vc) + '\n')
#         else:
#             for i in range(idx + 1, 30):
#                 outFd.write(str(vcilist[i]) + '\t')
#             outFd.write('\n')
#             outFd.write(str(inactiveLen) + ' inactive days, active day idx = ' + str(idx) + ', vci = ' + str(vcilist[idx]) + ', rate = ' + str(vcilist[idx] * 1. / vc) + ', vc = ' + str(vc) + '\n')
#         outFd.write('\n')
        
        # not end
        if mindn > inactiveLen:
            outFd.write(fields[0] + '\t31\n')
        else:
            outFd.write(fields[0] + '\t' + str(idx + 1) + '\n')
            
    inFd.close()
    outFd.close()
    
def getLifetime(infile, outfile, vciThreshold = 100, rateThreshold = 1.5 * 1. / 30, dayThreshold = 5):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    for line in inFd.readlines():
        fields = line.strip().split('\t', -1)
        vcilist = []
        # vid, i1, i2, ..., i30
        for fie in fields[1 : 1 + 30]:
            vcilist.append(int(fie))
        # try to find end point of lifetime
        vc = sum(vcilist)
        #maxvci = max(vcilist)
        threshold = vciThreshold if vciThreshold < rateThreshold * vc else math.ceil(rateThreshold * vc)
        threshold = 2 if 1 == threshold else threshold
        idx = 0
        for i in range(29, 29 - 30, -1):
            # backwards idx 29 -> 0, find first active day
            if threshold <= vcilist[i]: 
                idx = i
                break
        inactiveLen = 29 - idx
        
#         # details
#         outFd.write(line)
#         # not end
#         if dayThreshold > inactiveLen:
#             outFd.write(str(inactiveLen) + ' inactive days (not reach), active day idx = ' + str(idx) + ', vci = ' + str(vcilist[idx]) + ', threshold = ' + str(rateThreshold) + ' * ' + str(vc) + ' = ' + str(math.ceil(rateThreshold * vc)) + '\n')
#         else:
#             for i in range(idx + 1, 30):
#                 outFd.write(str(vcilist[i]) + '\t')
#             outFd.write('\n')
#             outFd.write(str(inactiveLen) + ' inactive days, active day idx = ' + str(idx) + ', vci = ' + str(vcilist[idx]) + ', threshold = ' + str(rateThreshold) + ' * ' + str(vc) + ' = ' + str(math.ceil(rateThreshold * vc)) + '\n')
#         outFd.write('\n')
        
        # not end
        if dayThreshold > inactiveLen:
            outFd.write(fields[0] + '\t' + str(vc) + '\t31\n')
        else:
            outFd.write(fields[0] + '\t' + str(vc) + '\t' + str(idx + 1) + '\n')
            
    inFd.close()
    outFd.close()
    
if '__main__' == __name__:
    workpath = 'F:/Video_Popularity/'
    
#     getActiveLifetime(workpath + 'rawdata/150801+151017/I30', 
#                 workpath + 'characterization/2_lifetime/lifetime_active', 
#                 minrate = 0.5 * 1./30)
#     
#     getInactiveLifetime(workpath + 'rawdata/150801+151017/I30', 
#                 workpath + 'characterization/2_lifetime/lifetime_inactive', 
#                 minrate = 0.5 * 1./30)

    getLifetime(workpath + 'rawdata/150801+151017/I30', 
                workpath + 'characterization/2_lifetime/lifetime')
    
    print('All Done!')