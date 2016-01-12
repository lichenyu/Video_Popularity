# -*- coding: utf-8 -*-
import json, re
from types import NoneType, UnicodeType
import burst_detector

def getUserFeatures(userfile):
    userMap = {}
    inFd = open(userfile, 'r')
    for line in inFd.readlines():
        user_metadata = json.loads(line.strip())
        #print(user_metadata)
        uid = user_metadata['id']
        userMap[uid] = []
        #name    gender    description    videos_count    playlists_count
        #favorites_count    followers_count    following_count    statuses_count    subscribe_count
        #vv_count    is_vip    is_share    is_verified
        #regist_time
        userMap[uid].append(user_metadata['name'])
        userMap[uid].append(user_metadata['gender'])
        userMap[uid].append(user_metadata['description'])
        userMap[uid].append(user_metadata['videos_count'])
        userMap[uid].append(user_metadata['playlists_count'])
        userMap[uid].append(user_metadata['favorites_count'])
        userMap[uid].append(user_metadata['followers_count'])
        userMap[uid].append(user_metadata['following_count'])
        userMap[uid].append(user_metadata['statuses_count'])
        userMap[uid].append(user_metadata['subscribe_count'])
        userMap[uid].append(user_metadata['vv_count'])
        userMap[uid].append(user_metadata['is_vip'])
        userMap[uid].append(user_metadata['is_share'])
        userMap[uid].append(user_metadata['is_verified'])
        userMap[uid].append(user_metadata['regist_time'])
        #break
    return userMap

def getVideoFeatures(videofile):
    videoMap = {}
    inFd = open(videofile, 'r')
    for line in inFd.readlines():
        video_metadata_batch = json.loads(line.strip())['videos']
        for video_metadata in video_metadata_batch:
            #print(video_metadata)
            vid = video_metadata['id']
            videoMap[vid] = []
            #title    description    duration    category    public_type
            #tags    copyright_type    streamtypes
            videoMap[vid].append(video_metadata['user']['id'])
            videoMap[vid].append(video_metadata['title'])
            videoMap[vid].append(video_metadata['description'])
            videoMap[vid].append(video_metadata['duration'])
            videoMap[vid].append(video_metadata['category'])
            videoMap[vid].append(video_metadata['public_type'])
            videoMap[vid].append(video_metadata['tags'])
            videoMap[vid].append(video_metadata['copyright_type'])
            videoMap[vid].append(video_metadata['streamtypes'])
            #break
        #break
    return videoMap

# def getPatternFeatures(patternfile):
#     patternMap = {}
#     inFd = open(patternfile, 'r')
#     for line in inFd.readlines():
#         fields = line.strip().split('\t', -1)
#         # vid, i7pattern
#         patternMap[fields[0]] = fields[1]
#     return patternMap

def extractFeatures(videofile, userfile, labelfile, outfile, details = False):
    userMap = getUserFeatures(userfile)
    videoMap = getVideoFeatures(videofile)
    
    labelFd = open(labelfile, 'r')
    outFd = open(outfile, 'w')
    for line in labelFd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, i1, i2, ..., i30, label
        vid = fields[0]
        label = fields[31]
        if vid in videoMap:
            uid = videoMap[vid][0]
            if uid in userMap:
                vcilist = []
                for i in range(1, 1 + 30):
                    vcilist.append(int(fields[i]))
                # extract features
                features = []
                # 1:title, description, duration, category, public_type, tags, copyright_type, streamtypes
                # title length
                titleLen = 0 if isinstance(videoMap[vid][1], NoneType) else len(videoMap[vid][1])
                features.append(titleLen)
                # ---regular expression---
                cncharPart = re.compile(ur'[\u4e00-\u9fa5]')
                digitPart = re.compile('\d')
                letterPart = re.compile('[A-Za-z_-]')
                spacePart = re.compile(r' ')
                booktitlePart = re.compile(ur'《.*》')
                if 0 == titleLen:
                    # cn char num in title
                    features.append(0)
                    # cn char rage in title
                    features.append(0)
                    # non-cn char num in title
                    features.append(0)
                    # non-cn char rate in title
                    features.append(0)
                    # digit num in title
                    features.append(0)
                    # dig rate in title
                    features.append(0)
                    # letter num in title
                    features.append(0)
                    # letter rate in title
                    features.append(0)
                    # space num in title
                    features.append(0)
                    # space rate in title
                    features.append(0)
                    # booktitle flag in title
                    features.append(0)
                else:
                    cncharLen = len(cncharPart.findall(videoMap[vid][1]))
                    digitLen = len(digitPart.findall(videoMap[vid][1]))
                    letterLen = len(letterPart.findall(videoMap[vid][1]))
                    spaceLen = len(spacePart.findall(videoMap[vid][1]))
                    booktitleFlag = True if 0 < len(booktitlePart.findall(videoMap[vid][1])) else False
                    # cn char num in title
                    features.append(cncharLen)
                    # cn char rage in title
                    features.append(cncharLen * 1. / titleLen)
                    # non-cn char num in title
                    features.append(titleLen - cncharLen)
                    # non-cn char rate in title
                    features.append((titleLen - cncharLen) * 1. / titleLen)
                    # digit num in title
                    features.append(digitLen)
                    # digit rate in title
                    features.append(digitLen * 1. / titleLen)
                    # letter num in title
                    features.append(letterLen)
                    # letter rate in title
                    features.append(letterLen * 1. / titleLen)
                    # space num in title
                    features.append(spaceLen)
                    # space rate in title
                    features.append(spaceLen * 1. / titleLen)
                    # booktitle flag in title
                    features.append(booktitleFlag)
                # description length
                features.append(len(videoMap[vid][2]))
                # duration
                features.append(videoMap[vid][3])
                # category
                features.append(videoMap[vid][4])
                # public_type
                features.append(videoMap[vid][5])
                # tag num
                features.append(len(videoMap[vid][6].split(',')))
                # copyright_type
                features.append(videoMap[vid][7])
                # streamtype num
                features.append(len(videoMap[vid][8]))
                # whether streamtypes contains hd2
                features.append('hd2' in videoMap[vid][8])
                
                #0:name, gender, description, videos_count, playlists_count
                #favorites_count, followers_count, following_count, statuses_count, subscribe_count
                #vv_count, is_vip, is_share, is_verified, regist_time
                # user name length
                userLen = len(userMap[uid][0])
                features.append(userLen)
                userCncharLen = len(cncharPart.findall(userMap[uid][0]))
                userDigitLen = len(digitPart.findall(userMap[uid][0]))
                userLetterLen = len(letterPart.findall(userMap[uid][0]))
                # cn char num in user name
                features.append(userCncharLen)
                # cn char rate in user name
                features.append(userCncharLen * 1. / userLen)
                # non cn char num in user name
                features.append(userLen - userCncharLen)
                # non cn char rate in user name
                features.append((userLen - userCncharLen) * 1. / userLen)
                # digit num in user name
                features.append(userDigitLen)
                # digit rate in user name
                features.append(userDigitLen * 1. / userLen)
                # letter num in user name
                features.append(userLetterLen)
                # letter rate in user name
                features.append(userLetterLen * 1. / userLen)
                # gender
                features.append(userMap[uid][1])
                # length of user description
                features.append(0 if isinstance(userMap[uid][2], NoneType) else len(userMap[uid][2]))
                # videos_count
                features.append(userMap[uid][3])
                # playlists_count
                features.append(userMap[uid][4])
                # favorites_count
                features.append(userMap[uid][5])
                # followers_count
                features.append(userMap[uid][6])
                # following_count
                features.append(userMap[uid][7])
                # statuses_count
                features.append(userMap[uid][8])
                # subscribe_count
                features.append(userMap[uid][9])
                # vv_count
                features.append(userMap[uid][10])
                # is_vip
                features.append(userMap[uid][11])
                # is_share
                features.append(False if 0 == userMap[uid][12] else True)
                # is_verified
                features.append(False if 0 == userMap[uid][13] else True)
                # i1 - i7
                for i in vcilist[0 : 0 + 7]:
                    features.append(i)
                # n7
                s = sum(vcilist[0 : 0 + 7])
                features.append(s)
                # i1 - i7 pct
                for i in vcilist[0 : 0 + 7]:
                    if 0 == s:
                        features.append(i)
                    else:
                        features.append(i * 1. / s)
                
                if True == details:
                    # print features
                    outFd.write(vid + '\t' + str(sum(vcilist)) + '\t' + (str(True) if '1' == label else str(False)) + '\n')
                    for f in videoMap[vid]:
                        outFd.write((f.encode('UTF-8') if isinstance(f, UnicodeType) else str(f)) + '\t')
                    outFd.write('\n')
                    for f in userMap[uid]:
                        outFd.write((f.encode('UTF-8') if isinstance(f, UnicodeType) else str(f)) + '\t')
                    outFd.write('\n')
                    for f in features:
                        outFd.write((f.encode('UTF-8') if isinstance(f, UnicodeType) else str(f)) + '\t')
                    outFd.write('\n\n')                
                else:
                # output
                    outFd.write(vid + '\t' + str(sum(vcilist)) + '\t' + (str(True) if '1' == label else str(False)))
                    for f in features:
                        outFd.write('\t' + (f.encode('unicode-escape') if isinstance(f, UnicodeType) else str(f)))
                    outFd.write('\n')
                
            else:
                continue
        else:
            continue
        
        #break
    labelFd.close()
    outFd.close()

if __name__ == '__main__':
    #workpath = '/Users/ouyangshuxin/Documents/work/Video_Popularity/'
    workpath = 'F:/Video_Popularity/'
    
    # get training/test set with burst flag
#     burst_detector.addBurstFlag2I(workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_training', 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/training/I30_training_bp', 
#                    7, 0.1)
#     burst_detector.addBurstFlag2I(workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_test', 
#                    workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/test/I30_test_bp', 
#                    7, 0.1)

#     extractFeatures(workpath + 'rawdata/150801+151017/VideoMetadata', 
#                     workpath + 'rawdata/150801+151017/UserMetadata', 
#                     workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/training/I30_training_bp', 
#                     workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/training/I30_training_bp_features_details', 
#                     details = True)
#      
#     extractFeatures(workpath + 'rawdata/150801+151017/VideoMetadata', 
#                     workpath + 'rawdata/150801+151017/UserMetadata', 
#                     workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/training/I30_training_bp', 
#                     workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/training/I30_training_bp_features')
#       
#     extractFeatures(workpath + 'rawdata/150801+151017/VideoMetadata', 
#                     workpath + 'rawdata/150801+151017/UserMetadata', 
#                     workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/test/I30_test_bp', 
#                     workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/test/I30_test_bp_features_details', 
#                     details = True)
#      
#     extractFeatures(workpath + 'rawdata/150801+151017/VideoMetadata', 
#                     workpath + 'rawdata/150801+151017/UserMetadata', 
#                     workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/test/I30_test_bp', 
#                     workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/test/I30_test_bp_features')

    burst_detector.addBurstPrediction2I(workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_training', 
                                        workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/randomForest/I30_training_results', 
                                        workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/randomForest/I30_training_bp_predicted', 
                                        7, 0.1)
    
    burst_detector.addBurstPrediction2I(workpath + 'analysis/2_predict_value/PBML/150801+151017/I30_test', 
                                        workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/randomForest/I30_test_results', 
                                        workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/randomForest/I30_test_bp_predicted', 
                                        7, 0.1)
       

#     rv = getVideoFeatures(workpath + 'rawdata/150801+151017/VideoMetadata')
#     print(rv['XMTM2MDk4MTE4OA=='][1])
#     print(type(rv['XMTM2MDk4MTE4OA=='][1]))
#     print(rv['XMTM2MDk4MTE4OA=='][1].encode('unicode-escape'))
#     cncharPart = re.compile(ur'[\u4e00-\u9fa5]')
#     print(len(cncharPart.findall(rv['XMTM2MDk4MTE4OA=='][1])))
#     letterPart = re.compile(r'[a-zA-Z_-]')
#     print(len(letterPart.findall(rv['XMTM2MDk4MTE4OA=='][1])))
#     spacePart = re.compile(r' ')
#     print(len(spacePart.findall(rv['XMTM2MDk4MTE4OA=='][1])))
#     booktitleFlag = re.compile(ur'《.*》')
#     print(True if 0 < len(booktitleFlag.findall(rv['XMTM2MDk4MTE4OA=='][1])) else False)

    print('All Done!')

    pass