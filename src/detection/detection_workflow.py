# -*- coding: utf-8 -*-

import s1_dataset_generation as dataset_generator
import s2_burst_detection as burst_detector
import s3_pattern_detection as pattern_detector
import s4_feature_extraction as feature_extractor
import s5_burst_prediction as burst_prediction
import s7_popularity_prediction as popularity_prediction


if __name__ == '__main__':
    workpath = '/Users/ouyangshuxin/Documents/Video_Popularity/'
    #workpath = 'F:/Video_Popularity/'
    
    # split datasets
#     dataset_generator.splitDatesets([workpath + 'rawdata/150801+151017/I30'], 
#                                     workpath + 'prediction/datasets/I30_training', 
#                                     workpath + 'prediction/datasets/I30_test')



#     # detect burst
#     burst_detector.detectBurst(workpath + 'prediction/datasets/I30_training', 
#                                workpath + 'prediction/i9p4/burst_detection/I30_training_bl', 
#                                9, 0.1)
#     burst_detector.detectBurst(workpath + 'prediction/datasets/I30_test', 
#                                workpath + 'prediction/i9p4/burst_detection/I30_test_bl', 
#                                9, 0.1)
#           
#     # detect pattern
#     pattern_detector.getIndiPattern(workpath + 'prediction/datasets//I30_training', 
#                                     workpath + 'prediction/i9p4/pattern_detection/I30_training_pattern', 
#                                     9)
#     pattern_detector.countIndiPattern(workpath + 'prediction/i9p4/pattern_detection/I30_training_pattern', 
#                                       workpath + 'prediction/i9p4/pattern_detection/I30_training_pattern_count')
#     pattern_detector.getIndiPattern(workpath + 'prediction/datasets/I30_test', 
#                                     workpath + 'prediction/i9p4/pattern_detection/I30_test_pattern', 
#                                     9)
#     pattern_detector.countIndiPattern(workpath + 'prediction/i9p4/pattern_detection/I30_test_pattern', 
#                                       workpath + 'prediction/i9p4/pattern_detection/I30_test_pattern_count')
#    
#     # extract features
#     feature_extractor.extractFeatures(workpath + 'rawdata/150801+151017/VideoMetadata', 
#                                       workpath + 'rawdata/150801+151017/UserMetadata', 
#                                       workpath + 'prediction/i9p4/burst_detection/I30_training_bl', 
#                                       workpath + 'prediction/i9p4/burst_prediction/training_label_features', 
#                                       9)
#     feature_extractor.extractFeatures(workpath + 'rawdata/150801+151017/VideoMetadata', 
#                                       workpath + 'rawdata/150801+151017/UserMetadata', 
#                                       workpath + 'prediction/i9p4/burst_detection/I30_test_bl', 
#                                       workpath + 'prediction/i9p4/burst_prediction/test_label_features', 
#                                       9)
     
     
     
#     # get (RF) burst prediction results and add them to the I file
#     burst_prediction.getPredictionResults(workpath + 'prediction/i9p4/burst_detection/I30_training_bl', 
#                                           workpath + 'prediction/i9p4/burst_prediction/training_bprslts', 
#                                           workpath + 'prediction/i9p4/burst_prediction/I30_training_bp')
#     burst_prediction.getPredictionResults(workpath + 'prediction/i9p4/burst_detection/I30_test_bl', 
#                                           workpath + 'prediction/i9p4/burst_prediction/test_bprslts', 
#                                           workpath + 'prediction/i9p4/burst_prediction/I30_test_bp')
#     # get pattern records of the training set with predictions for para
#     pattern_detector.getRecordsByPattern(workpath + 'prediction/i9p4/burst_prediction/I30_training_bp', 
#                                          workpath + 'prediction/i9p4/pattern_detection/I30_training_pattern', 
#                                          ['100000000', '110000000', '000000000'])
#     # get pattern records of the test set with predictions for para
#     pattern_detector.getRecordsByPattern(workpath + 'prediction/i9p4/burst_prediction/I30_test_bp', 
#                                          workpath + 'prediction/i9p4/pattern_detection/I30_test_pattern', 
#                                          ['100000000', '110000000', '000000000'])
      
      
      
#     # predict popularity
#     popularity_prediction.evaluateBaseModels(['100000000', '110000000', '000000000', 'others'], 
#                                              workpath + 'prediction/i9p4/burst_prediction/I30_test_bp_', 
#                                              workpath + 'prediction/i9p4/popularity_prediction/rse_test_', 
#                                              9, 0.3064035, [1.161242, 1.213789, 1.113899, 1.294116, 1.228609, 1.468656, 1.596782, 2.146889, 2.455075])
#     print('')
#     popularity_prediction.evaluateProposedModels(['100000000', '110000000', '000000000', 'others'], 
#                                                  workpath + 'prediction/i9p4/burst_prediction/I30_test_bp_', 
#                                                  workpath + 'prediction/i9p4/popularity_prediction/rse_test_', 
#                                                  9, 
#                                                  [
#                                                   [1.0981059, 1.5911751, 1.1125094, 1.3164351, 1.3433597, 1.5320601, 1.6006977, 2.1938607, 2.1681576, 0.1570093], 
#                                                   [1.1278235, 1.1244228, 1.1940213, 1.3329566, 1.3704086, 1.3904058, 2.2889247, 2.7879782, 3.4788343, 0.1314889], 
#                                                   [1.4573596, 0.9983199, 1.0294220, 1.2220001, 1.1563089, 1.2480434, 1.8122482, 2.5332942, 4.4511361, 0.1892338], 
#                                                   [1.1543809, 1.2228305, 1.1256822, 1.1224990, 1.1324919, 1.2249547, 1.2122635, 1.3744851, 1.5509282, 0.1737234]
#                                                   ])


    print('All Done!')
    
    