# -*- coding: utf-8 -*-
import json, re
from types import NoneType

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

def extractFeatures(videofile, userfile, labelfile, outfile):
    print('in')
    userMap = getUserFeatures(userfile)
    videoMap = getVideoFeatures(videofile)
    
    labelFd = open(labelfile, 'r')
    for line in labelFd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, i1, i2, ..., i30, label
        vid = fields[0]
        label = fields[31]
        if vid in videoMap:
            uid = videoMap[vid][0]
            if uid in userMap:
                print(videoMap[vid])
                print(userMap[uid])
                # extract features
                features = []
                # 1:title, description, duration, category, public_type, tags, copyright_type, streamtypes
                # title length
                features.append(len(videoMap[vid][1]))
                # dig num in title
                digitpart = re.compile('\d')
                features.append(len(digitpart.findall(videoMap[vid][1])))
                # dig rate in title
                features.append(len(digitpart.findall(videoMap[vid][1])) * 1. / len(videoMap[vid][1]))
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
                # streamtypes
                features.append(len(videoMap[vid][8]))
                # whether streamtypes contains hd2
                features.append('hd2' in videoMap[vid][8])
                
                #0:name, gender, description, videos_count, playlists_count
                #favorites_count, followers_count, following_count, statuses_count, subscribe_count
                #vv_count, is_vip, is_share, is_verified, regist_time
                # user name length
                features.append(len(userMap[uid][0]))
                # dig num in user name
                features.append(len(digitpart.findall(userMap[uid][0])))
                # dig rate in user name
                features.append(len(digitpart.findall(userMap[uid][0])) * 1. / len(userMap[uid][0]))
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
                
                print(features)
            else:
                continue
        else:
            continue
        
        break
    

if __name__ == '__main__':
    #workpath = '/Users/ouyangshuxin/Documents/work/Video_Popularity/'
    workpath = 'F:/Video_Popularity/'
    

#     umap = getUserFeatures(workpath + 'rawdata/150801+151017/UserMetadata')
#     vmap = getVideoFeatures(workpath + 'rawdata/150801+151017/VideoMetadata')
#     print(umap)
#     print(vmap)
#     u = '785924582'
#     print(0 if isinstance(umap[u][2], NoneType) else len(umap[u][2]))
#     print(umap[u][2])
#     v = 'XMTM2MTM0ODEzMg=='
#     print(vmap[v][1])



    extractFeatures(workpath + 'rawdata/150801+151017/VideoMetadata', 
                    workpath + 'rawdata/150801+151017/UserMetadata', 
                    workpath + 'analysis/2_predict_value/PBML/150801+151017/burst_detection/I30_training', 
                    '')


    pass