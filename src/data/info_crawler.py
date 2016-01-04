# -*- coding: utf-8 -*-

import urllib2, time, json

def sendRequest(url, info_str):
    tryNum = 0
    while True:
        if 0 < tryNum and 0 == tryNum % 10:
            time.sleep(60)
        try:
            print(info_str)
            resFd = urllib2.urlopen(url, timeout = 15)
            res = resFd.read()
        except urllib2.HTTPError as e:
            print(str(e))
            print('Retrying...')
            tryNum = tryNum + 1
        except urllib2.URLError as e:
            print(str(e))
            print('Retrying...')
            tryNum = tryNum + 1
        except Exception as e:
            print(str(e))
            print('Retrying...')
            tryNum = tryNum + 1
        else:
            print('Success')
            return res

def getVideoMetadata(infile, outfile, cid = '4fa043e1446bdf29'):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    
    getVideoMetadataURL = 'https://openapi.youku.com/v2/videos/show_batch.json'
    cidStr = 'client_id=' + cid
    vid50List = []
    
    # seqnum for request
    qSeq = 1
    for line in inFd.readlines():
        # vid, ...
        vid50List.append(line.strip().split('\t', -1)[0])
        if 50 == len(vid50List):
            vidsStr = 'video_ids=' + vid50List[0]
            for vid in vid50List[1:]:
                vidsStr = vidsStr + ',' + vid
            finalURL = getVideoMetadataURL + '?' + cidStr + '&' + vidsStr
            res = sendRequest(finalURL, 'Querying NO.' + str((qSeq - 1) * 50 + 1) + '-' + str(qSeq * 50) + ' ' +  finalURL)
            outFd.write(res + '\n')
            qSeq = qSeq + 1
            vid50List = []
    if 0 != len(vid50List):
        vidsStr = 'video_ids=' + vid50List[0]
        for vid in vid50List[1:]:
            vidsStr = vidsStr + ',' + vid
        finalURL = getVideoMetadataURL + '?' + cidStr + '&' + vidsStr
        res = sendRequest(finalURL, 'Querying NO.' + str((qSeq - 1) * 50 + 1) + '-' + str(qSeq * 50) + ' ' +  finalURL)
        outFd.write(res + '\n')
        qSeq = qSeq + 1
        vid50List = []
        
    inFd.close()
    outFd.close()

# get uid list from video metadata batch
def getUserList(infile, outfile):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    
    userList = set()
    videoNum = 0
    for line in inFd.readlines():
        metadataBatch = json.loads(line)
        for metadata in metadataBatch['videos']:
            if False == (metadata['user']['id'] in userList):
                userList.add(metadata['user']['id'])
            videoNum = videoNum + 1
    for uid in userList:
        outFd.write(uid + '\n')
    print('Total ' + str(videoNum) + ' Videos by ' + str(len(userList)) + ' Users')
    
    inFd.close()
    outFd.close()
    
def getUserMetadata(infile, outfile, cid = '4fa043e1446bdf29'):
    inFd = open(infile, 'r')
    outFd = open(outfile, 'w')
    
    getUserMetadataURL = 'https://openapi.youku.com/v2/users/show.json'
    cidStr = 'client_id=' + cid
    
    qSeq = 1
    for line in inFd.readlines():
        # uid, ...
        uidStr = 'user_id=' + line.strip().split('\t', -1)[0]
        finalURL = getUserMetadataURL + '?' + cidStr + '&' + uidStr
        res = sendRequest(finalURL, 'Querying NO.' + str(qSeq) + ' ' + finalURL)
        outFd.write(res + '\n')
        qSeq = qSeq + 1
        
    inFd.close()
    outFd.close()

def test():
    print('All Done!')

if __name__ == '__main__':
    test()
    