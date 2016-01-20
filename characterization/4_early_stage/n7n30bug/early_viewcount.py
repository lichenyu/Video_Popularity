# -*- coding: utf-8 -*-

import pattern.pattern_detector as pattern_detector

if __name__ == '__main__':
    workpath = 'F:/Video_Popularity/'
    
    pattern_detector.getI7I30Pct(workpath + 'rawdata/150801+151017/I30', 
                                 workpath + 'characterization/4_early_stage/I30_total_pct')
    pattern_detector.getI7NewPattern(workpath + 'rawdata/150801+151017/I30', 
                                     workpath + 'characterization/4_early_stage/I30_total_I7pattern')
    pattern_detector.countI7Pattern(workpath + 'characterization/4_early_stage/I30_total_I7pattern', 
                                    workpath + 'characterization/4_early_stage/I30_total_I7pattern_count')
    pattern_detector.getPatternRecords(workpath + 'characterization/4_early_stage/I30_total_I7pattern', 
                                       workpath + 'rawdata/150801+151017/I30', 
                                       ['1000000', '1100000', '0000000'])
    
    print('All Done!')