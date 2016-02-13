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
#                                workpath + 'prediction/i13p4/burst_detection/I30_training_bl', 
#                                13, 0.1)
#     burst_detector.detectBurst(workpath + 'prediction/datasets/I30_test', 
#                                workpath + 'prediction/i13p4/burst_detection/I30_test_bl', 
#                                13, 0.1)
#             
#     # detect pattern
#     pattern_detector.getIndiPattern(workpath + 'prediction/datasets//I30_training', 
#                                     workpath + 'prediction/i13p4/pattern_detection/I30_training_pattern', 
#                                     13)
#     pattern_detector.countIndiPattern(workpath + 'prediction/i13p4/pattern_detection/I30_training_pattern', 
#                                       workpath + 'prediction/i13p4/pattern_detection/I30_training_pattern_count')
#     pattern_detector.getIndiPattern(workpath + 'prediction/datasets/I30_test', 
#                                     workpath + 'prediction/i13p4/pattern_detection/I30_test_pattern', 
#                                     13)
#     pattern_detector.countIndiPattern(workpath + 'prediction/i13p4/pattern_detection/I30_test_pattern', 
#                                       workpath + 'prediction/i13p4/pattern_detection/I30_test_pattern_count')
#      
#     # extract features
#     feature_extractor.extractFeatures(workpath + 'rawdata/150801+151017/VideoMetadata', 
#                                       workpath + 'rawdata/150801+151017/UserMetadata', 
#                                       workpath + 'prediction/i13p4/burst_detection/I30_training_bl', 
#                                       workpath + 'prediction/i13p4/burst_prediction/training_label_features', 
#                                       13)
#     feature_extractor.extractFeatures(workpath + 'rawdata/150801+151017/VideoMetadata', 
#                                       workpath + 'rawdata/150801+151017/UserMetadata', 
#                                       workpath + 'prediction/i13p4/burst_detection/I30_test_bl', 
#                                       workpath + 'prediction/i13p4/burst_prediction/test_label_features', 
#                                       13)
     
     
     
#     # get (RF) burst prediction results and add them to the I file
#     burst_prediction.getPredictionResults(workpath + 'prediction/i13p4/burst_detection/I30_training_bl', 
#                                           workpath + 'prediction/i13p4/burst_prediction/training_bprslts', 
#                                           workpath + 'prediction/i13p4/burst_prediction/I30_training_bp')
#     burst_prediction.getPredictionResults(workpath + 'prediction/i13p4/burst_detection/I30_test_bl', 
#                                           workpath + 'prediction/i13p4/burst_prediction/test_bprslts', 
#                                           workpath + 'prediction/i13p4/burst_prediction/I30_test_bp')
#     # get pattern records of the training set with predictions for para
#     pattern_detector.getRecordsByPattern(workpath + 'prediction/i13p4/burst_prediction/I30_training_bp', 
#                                          workpath + 'prediction/i13p4/pattern_detection/I30_training_pattern', 
#                                          ['1000000000000', '1100000000000', '1110000000000'])
#     # get pattern records of the test set with predictions for para
#     pattern_detector.getRecordsByPattern(workpath + 'prediction/i13p4/burst_prediction/I30_test_bp', 
#                                          workpath + 'prediction/i13p4/pattern_detection/I30_test_pattern', 
#                                          ['1000000000000', '1100000000000', '1110000000000'])
      
      
      
    # predict popularity
    popularity_prediction.evaluateBaseModels(['1000000000000', '1100000000000', '1110000000000', 'others'], 
                                             workpath + 'prediction/i13p4/burst_prediction/I30_test_bp_', 
                                             workpath + 'prediction/i13p4/popularity_prediction/rse_test_', 
                                             13, 0.2486092, [1.132194, 1.130779, 1.021279, 1.136970, 1.068189, 1.205886, 1.332793, 1.628954, 1.718783, 1.660850, 1.970427, 1.983139, 2.509243])
    print('')
    popularity_prediction.evaluateProposedModels(['1000000000000', '1100000000000', '1110000000000', 'others'], 
                                                 workpath + 'prediction/i13p4/burst_prediction/I30_test_bp_', 
                                                 workpath + 'prediction/i13p4/popularity_prediction/rse_test_', 
                                                 13, 
                                                 [
                                                  [1.081021, 1.288085, 1.093220, 1.073118, 1.159056, 1.330736, 1.348681, 1.678532, 1.652788, 1.710169, 2.016326, 1.716919, 2.187307, 0.170231], 
                                                  [1.0953764, 1.1064463, 0.8101455, 1.1783358, 1.0769573, 1.1226794, 1.4745599, 1.8050701, 2.0201300, 2.4428860, 2.5609528, 2.5713955, 2.7910151, 0.1524071], 
                                                  [1.0653860, 1.0688818, 1.0703397, 0.6625173, 1.0995091, 1.4714298, 1.2140063, 1.8949293, 1.6112827, 2.5648829, 2.6074309, 2.2937185, 4.2016592, 0.1773003], 
                                                  [0.9720664, 1.2046540, 1.1277337, 1.1742274, 1.1341260, 1.2589746, 1.3319762, 1.4975069, 1.5730385, 1.4194923, 1.5797177, 1.7991936, 2.2420617, 0.2082695]
                                                  ])


    print('All Done!')
    
    