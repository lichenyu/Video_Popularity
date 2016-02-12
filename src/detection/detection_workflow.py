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
    dataset_generator.splitDatesets([workpath + 'rawdata/150801+151017/I30'], 
                                    workpath + 'prediction/datasets/I30_training', 
                                    workpath + 'prediction/datasets/I30_test')

    # detect burst
    burst_detector.detectBurst(workpath + 'prediction/datasets/I30_training', 
                               workpath + 'prediction/i7p4/burst_detection/I30_training_bl', 
                               7, 0.1)
    burst_detector.detectBurst(workpath + 'prediction/datasets/I30_test', 
                               workpath + 'prediction/i7p4/burst_detection/I30_test_bl', 
                               7, 0.1)
       
    # detect pattern
    pattern_detector.getIndiPattern(workpath + 'prediction/datasets//I30_training', 
                                    workpath + 'prediction/i7p4/pattern_detection/I30_training_pattern', 
                                    7)
    pattern_detector.countIndiPattern(workpath + 'prediction/i7p4/pattern_detection/I30_training_pattern', 
                                      workpath + 'prediction/i7p4/pattern_detection/I30_training_pattern_count')
    pattern_detector.getIndiPattern(workpath + 'prediction/datasets/I30_test', 
                                    workpath + 'prediction/i7p4/pattern_detection/I30_test_pattern', 
                                    7)
    pattern_detector.countIndiPattern(workpath + 'prediction/i7p4/pattern_detection/I30_test_pattern', 
                                      workpath + 'prediction/i7p4/pattern_detection/I30_test_pattern_count')

    # extract features
    feature_extractor.extractFeatures(workpath + 'rawdata/150801+151017/VideoMetadata', 
                                      workpath + 'rawdata/150801+151017/UserMetadata', 
                                      workpath + 'prediction/i7p4/burst_detection/I30_training_bl', 
                                      workpath + 'prediction/i7p4/burst_prediction/training_label_features', 
                                      7)
    feature_extractor.extractFeatures(workpath + 'rawdata/150801+151017/VideoMetadata', 
                                      workpath + 'rawdata/150801+151017/UserMetadata', 
                                      workpath + 'prediction/i7p4/burst_detection/I30_test_bl', 
                                      workpath + 'prediction/i7p4/burst_prediction/test_label_features', 
                                      7)
     
    # get (RF) burst prediction results and add them to the I file
    burst_prediction.getPredictionResults(workpath + 'prediction/i7p4/burst_detection/I30_training_bl', 
                                          workpath + 'prediction/i7p4/burst_prediction/training_bprslts', 
                                          workpath + 'prediction/i7p4/burst_prediction/I30_training_bp')
    burst_prediction.getPredictionResults(workpath + 'prediction/i7p4/burst_detection/I30_test_bl', 
                                          workpath + 'prediction/i7p4/burst_prediction/test_bprslts', 
                                          workpath + 'prediction/i7p4/burst_prediction/I30_test_bp')
    # get pattern records of the training set with predictions for para
    pattern_detector.getRecordsByPattern(workpath + 'prediction/i7p4/burst_prediction/I30_training_bp', 
                                         workpath + 'prediction/i7p4/pattern_detection/I30_training_pattern', 
                                         ['1000000', '1100000', '0000000'])
    # get pattern records of the test set with predictions for para
    pattern_detector.getRecordsByPattern(workpath + 'prediction/i7p4/burst_prediction/I30_test_bp', 
                                         workpath + 'prediction/i7p4/pattern_detection/I30_test_pattern', 
                                         ['1000000', '1100000', '0000000'])
     
    # predict popularity
    popularity_prediction.evaluateBaseModels(['1000000', '1100000', '0000000', 'others'], 
                                             workpath + 'prediction/i7p4/burst_prediction/I30_test_bp_', 
                                             workpath + 'prediction/i7p4/popularity_prediction/rse_test_', 
                                             0.3462903, [1.175979, 1.308160, 1.227412, 1.508363, 1.369082, 1.761802, 2.181996])
    print('')
    popularity_prediction.evaluateProposedModels(['1000000', '1100000', '0000000', 'others'], 
                                                 workpath + 'prediction/i7p4/burst_prediction/I30_test_bp_', 
                                                 workpath + 'prediction/i7p4/popularity_prediction/rse_test_', 
                                                 [
                                                  [1.1148868, 1.5946892, 1.2631701, 1.5499933, 1.4332997, 1.7116611, 1.9358164, 0.1368604], 
                                                  [1.1385718, 1.1455380, 1.5605167, 1.8020644, 2.0741012, 1.9513898, 3.7991007, 0.1591615], 
                                                  [1.3113564, 1.4350187, 1.0369490, 1.3713631, 1.2888453, 1.8581218, 3.3020149, 0.1459587], 
                                                  [1.2433989, 1.1757283, 1.1288279, 1.1552937, 1.1294082, 1.2243181, 1.3275145, 0.1216962]
                                                  ])


    print('All Done!')
    
    