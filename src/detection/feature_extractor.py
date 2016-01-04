# -*- coding: utf-8 -*-
import json

def getUserFeatures(userfile):
    userMap = {}
    inFd = open(userfile, 'r')
    for line in inFd.readlines():
        user_metadata = json.loads(line.strip())
        print(user_metadata)
        userMap[user_metadata['id']] = [user_metadata['following_count'], user_metadata['followers_count'], user_metadata['is_vip']]
        break
    return userMap

if __name__ == '__main__':
    workpath = '/Users/ouyangshuxin/Documents/work/Video_Popularity/'
    
    
    print(getUserFeatures(workpath + 'rawdata/150801+151017/UserMetadata'))
    pass