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
#                                workpath + 'prediction/i25p4/burst_detection/I30_training_bl', 
#                                25, 0.1)
#     burst_detector.detectBurst(workpath + 'prediction/datasets/I30_test', 
#                                workpath + 'prediction/i25p4/burst_detection/I30_test_bl', 
#                                25, 0.1)
#                   
#     # detect pattern
#     pattern_detector.getIndiPattern(workpath + 'prediction/datasets//I30_training', 
#                                     workpath + 'prediction/i25p4/pattern_detection/I30_training_pattern', 
#                                     25)
#     pattern_detector.countIndiPattern(workpath + 'prediction/i25p4/pattern_detection/I30_training_pattern', 
#                                       workpath + 'prediction/i25p4/pattern_detection/I30_training_pattern_count')
#     pattern_detector.getIndiPattern(workpath + 'prediction/datasets/I30_test', 
#                                     workpath + 'prediction/i25p4/pattern_detection/I30_test_pattern', 
#                                     25)
#     pattern_detector.countIndiPattern(workpath + 'prediction/i25p4/pattern_detection/I30_test_pattern', 
#                                       workpath + 'prediction/i25p4/pattern_detection/I30_test_pattern_count')
#            
#     # extract features
#     feature_extractor.extractFeatures(workpath + 'rawdata/150801+151017/VideoMetadata', 
#                                       workpath + 'rawdata/150801+151017/UserMetadata', 
#                                       workpath + 'prediction/i25p4/burst_detection/I30_training_bl', 
#                                       workpath + 'prediction/i25p4/burst_prediction/training_label_features', 
#                                       25)
#     feature_extractor.extractFeatures(workpath + 'rawdata/150801+151017/VideoMetadata', 
#                                       workpath + 'rawdata/150801+151017/UserMetadata', 
#                                       workpath + 'prediction/i25p4/burst_detection/I30_test_bl', 
#                                       workpath + 'prediction/i25p4/burst_prediction/test_label_features', 
#                                       25)
     
     
     
#     # get (RF) burst prediction results and add them to the I file
#     burst_prediction.getPredictionResults(workpath + 'prediction/i25p4/burst_detection/I30_training_bl', 
#                                           workpath + 'prediction/i25p4/burst_prediction/training_bprslts', 
#                                           workpath + 'prediction/i25p4/burst_prediction/I30_training_bp')
#     burst_prediction.getPredictionResults(workpath + 'prediction/i25p4/burst_detection/I30_test_bl', 
#                                           workpath + 'prediction/i25p4/burst_prediction/test_bprslts', 
#                                           workpath + 'prediction/i25p4/burst_prediction/I30_test_bp')
#     # get pattern records of the training set with predictions for para
#     pattern_detector.getRecordsByPattern(workpath + 'prediction/i25p4/burst_prediction/I30_training_bp', 
#                                          workpath + 'prediction/i25p4/pattern_detection/I30_training_pattern', 
#                                          ['1000000000000000000000000', '1100000000000000000000000', '1110000000000000000000000'])
#     # get pattern records of the test set with predictions for para
#     pattern_detector.getRecordsByPattern(workpath + 'prediction/i25p4/burst_prediction/I30_test_bp', 
#                                          workpath + 'prediction/i25p4/pattern_detection/I30_test_pattern', 
#                                          ['1000000000000000000000000', '1100000000000000000000000', '1110000000000000000000000'])
      
      
      
#     # predict popularity
#     popularity_prediction.evaluateBaseModels(['1000000000000000000000000', '1100000000000000000000000', '1110000000000000000000000', 'others'], 
#                                              workpath + 'prediction/i25p4/burst_prediction/I30_test_bp_', 
#                                              workpath + 'prediction/i25p4/popularity_prediction/rse_test_', 
#                                              25, 0.0984914, [1.0900092, 0.9881023, 0.9394291, 0.9767307, 0.9340327, 0.9752981, 0.9959329, 1.0169636, 0.9773896, 0.9863678, 1.1242456, 1.0928225, 1.0367258, 1.0320493, 1.2381523, 1.0640083, 1.0879510, 1.1154080, 1.2448542, 1.1769642, 1.2033240, 1.2029030, 1.2948082, 1.3760237, 1.3891083])
#     print('')
#     popularity_prediction.evaluateProposedModels(['1000000000000000000000000', '1100000000000000000000000', '1110000000000000000000000', 'others'], 
#                                                  workpath + 'prediction/i25p4/burst_prediction/I30_test_bp_', 
#                                                  workpath + 'prediction/i25p4/popularity_prediction/rse_test_', 
#                                                  25, 
#                                                  [
#                                                   [1.0590981, 0.3339345, 0.9102734, 0.9928815, 0.8876235, 0.8344424, 0.9559665, 0.9662559, 0.9632932, 0.9925725, 1.1939797, 1.1608431, 1.1065368, 1.0159638, 1.4091633, 1.0103059, 1.1730932, 1.0241010, 1.3406542, 1.1209629, 1.3443546, 1.2534968, 1.4684744, 1.3870564, 1.8647395, 0.3285392], 
#                                                   [1.0702425, 1.0549513, 0.4306568, 0.7595529, 0.6674779, 0.8025147, 0.9481986, 1.0774647, 1.0478711, 0.9883542, 1.0587527, 1.2201268, 1.0535981, 1.0341260, 1.2541239, 1.2186622, 1.0159214, 1.0147117, 1.2414040, 1.0306626, 1.2087485, 1.6553059, 1.5231930, 1.3980681, 1.4620430, 0.1850115], 
#                                                   [1.0216349, 1.0290820, 1.0187330, 0.7446599, 0.9335382, 1.0091486, 0.8915960, 1.1024424, 0.9953286, 1.0487402, 1.0063735, 1.2520269, 1.3373092, 1.0218593, 0.9581160, 1.2332978, 1.1687206, 0.9731336, 1.3292224, 1.1413230, 1.2046914, 1.4575109, 1.2974986, 1.6759684, 1.8850911, 0.2051498], 
#                                                   [1.0165313, 1.0179538, 1.0041964, 1.0316487, 1.0019626, 1.0358565, 1.0414406, 1.0602777, 1.0290318, 1.0287165, 1.1381200, 1.1185796, 1.0769111, 1.0606155, 1.1601269, 1.0905153, 1.1575532, 1.1577957, 1.2370098, 1.2185871, 1.2061714, 1.1938113, 1.2742644, 1.2775034, 1.3161615, 0.2529395]
#                                                   ])


    print('All Done!')
    
    