# -*- coding: utf-8 -*-

# get lifetime of each video in I file
# end point: from which at least mindn days, vci < minrate*burst
def getLifetime(infile, outfile, minvc, minrate, mindn):
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
        outFd.write(line)
        # try to find end point of lifetime
        vc = sum(vcilist)
        idx = 0
        for i in range(29, 29 - 30, -1):
            # backwards idx 29 -> 0, find first active day
            if 100 <= vcilist[i] or (minrate <= vcilist[i] * 1. / vc and 10 <= vcilist[i]): 
                idx = i
                break
        inactiveLen = 29 - idx
        # not end
        if mindn > inactiveLen:
            outFd.write(str(inactiveLen) + ' inactive days (not reach), active day idx = ' + str(idx) + ', vci = ' + str(vcilist[idx]) + ', rate = ' + str(vcilist[idx] * 1. / vc) + ', vc = ' + str(vc) + '\n')
        else:
            for i in range(idx + 1, 30):
                outFd.write(str(vcilist[i]) + '\t')
            outFd.write('\n')
            outFd.write(str(inactiveLen) + ' inactive days, active day idx = ' + str(idx) + ', vci = ' + str(vcilist[idx]) + ', rate = ' + str(vcilist[idx] * 1. / vc) + ', vc = ' + str(vc) + '\n')
        outFd.write('\n')    
        
            
    inFd.close()
    outFd.close()
    
if '__main__' == __name__:
    workpath = 'F:/Video_Popularity/'
    
    getLifetime(workpath + 'rawdata/150801+151017/I30', 
                workpath + 'characterization/2_lifetime/lifetime_r1_n5', 
                minvc = 30, minrate = 1./30, mindn = 5)
    
    print('All Done!')