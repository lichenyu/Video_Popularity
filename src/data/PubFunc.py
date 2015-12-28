

def getVcByVci(vciList):
    vcList = list()
    curVc = 0
    for vci in vciList:
        curVc = curVc + vci
        vcList.append(curVc)
    return vcList

def getVciByVc(vcList):
    vciList = list()
    vciList.append(vcList[0])
    for i in range(1, len(vcList)):
        vciList.append(vcList[i] - vcList[i - 1])
    return vciList

if __name__ == '__main__':
    print(getVcByVci([1,2,3,4,5]))
    print(getVciByVc([1,2,3,4,5]))