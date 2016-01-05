# -*- coding: utf-8 -*-
import json

def getUserFeatures(userfile):
    userMap = {}
    inFd = open(userfile, 'r')
    for line in inFd.readlines():
        user_metadata = json.loads(line.strip())
        print(user_metadata)
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
        #userMap[uid].append(user_metadata['regist_time'])
        break
    return userMap

def getVideoFeatures(videofile):
    videoMap = {}
    inFd = open(videofile, 'r')
    for line in inFd.readlines():
        video_metadata_batch = json.loads(line.strip())['videos']
        for video_metadata in video_metadata_batch:
            print(video_metadata)
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
            break
        break
    return videoMap

def extractFeatures(videofile, userfile, classfile, outfile):
    userMap = getUserFeatures(userfile)
    videoMap = getVideoFeatures(videofile)

if __name__ == '__main__':
    #workpath = '/Users/ouyangshuxin/Documents/work/Video_Popularity/'
    workpath = 'F:/Video_Popularity/'
    
    
    print(getUserFeatures(workpath + 'rawdata/150801+151017/UserMetadata'))
    print(getVideoFeatures(workpath + 'rawdata/150801+151017/VideoMetadata'))
    pass