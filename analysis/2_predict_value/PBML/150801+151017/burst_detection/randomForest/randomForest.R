library(randomForest)

workpath = 'F:/Video_Popularity/'
#workpath = '/Users/ouyangshuxin/Documents/work/Video_Popularity/'
training = read.table(paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/training/I30_training_bp_features', sep = ''), header = TRUE)
test = read.table(paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/test/I30_test_bp_features', sep = ''), header = TRUE)
training$statuses_count = NULL
test$statuses_count = NULL
levels(test$public_type) = levels(training$public_type)
training_l = training[, 3]
training_f = as.data.frame(training[, 4:length(training)])
training_d = as.data.frame(training[, 3:length(training)])
test_l = test[, 3]
test_f = as.data.frame(test[, 4:length(test)])
test_d = as.data.frame(test[, 3:length(test)])



set.seed(10)
forest = randomForest(label ~ ., training_d, ntree = 501)



# training performance
ll = c(training_l)
pl = c(forest$predicted)
# burst
length(which(ll == 2))
# not burst
length(which(ll == 1))
# burst -> burst
length(which(pl == ll & ll == 2))
# burst -> not burst
length(which(pl != ll & ll == 2))
# not burst -> not burst
length(which(pl == ll & ll == 1))
# not burst -> burst
length(which(pl != ll & ll == 1))

out_df <- data.frame(training$vid, ll - 1, pl - 1);
write.table(out_df, 
            file = paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/randomForest/I30_training_results', sep = ''), 
            sep = '\t', quote = FALSE, col.names = FALSE, row.names = FALSE)



# test performance
prediction = predict(forest, test_f, type = 'class')
ll = c(test_l)
pl = c(prediction)
# burst
length(which(ll == 2))
# not burst
length(which(ll == 1))
# burst -> burst
length(which(pl == ll & ll == 2))
# burst -> not burst
length(which(pl != ll & ll == 2))
# not burst -> not burst
length(which(pl == ll & ll == 1))
# not burst -> burst
length(which(pl != ll & ll == 1))

out_df <- data.frame(test$vid, ll - 1, pl - 1);
write.table(out_df, 
            file = paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/randomForest/I30_test_results', sep = ''), 
            sep = '\t', quote = FALSE, col.names = FALSE, row.names = FALSE)



# --------------------------------------------------



# training - 1000 performance
ll = c(training_l)
pl = c(forest$predicted)
# burst
length(which(ll == 2))
# not burst
length(which(ll == 1))
# burst -> burst
length(which(pl == ll & ll == 2))
# burst -> not burst
length(which(pl != ll & ll == 2))
# not burst -> not burst
length(which(pl == ll & ll == 1))
# not burst -> burst
length(which(pl != ll & ll == 1))

idx_fn = which(pl != ll & ll == 2)
idx_fp = which(pl != ll & ll == 1)
idx_drop = c(idx_fn[1 : 500], idx_fp[1 : 500])

out_df <- data.frame(training[-idx_drop, ]$vid, ll[-idx_drop] - 1, pl[-idx_drop] - 1);
write.table(out_df, 
            file = paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/randomForest/I30_training_results', sep = ''), 
            sep = '\t', quote = FALSE, col.names = FALSE, row.names = FALSE)



# test - 1000 performance
prediction = predict(forest, test_f, type = 'class')
ll = c(test_l)
pl = c(prediction)
# burst
length(which(ll == 2))
# not burst
length(which(ll == 1))
# burst -> burst
length(which(pl == ll & ll == 2))
# burst -> not burst
length(which(pl != ll & ll == 2))
# not burst -> not burst
length(which(pl == ll & ll == 1))
# not burst -> burst
length(which(pl != ll & ll == 1))

idx_fn = which(pl != ll & ll == 2)
idx_fp = which(pl != ll & ll == 1)
idx_drop = c(idx_fn[1 : 500], idx_fp[1 : 500])

out_df <- data.frame(test[-idx_drop, ]$vid, ll[-idx_drop] - 1, pl[-idx_drop] - 1);
write.table(out_df, 
            file = paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/randomForest/I30_test_results', sep = ''), 
            sep = '\t', quote = FALSE, col.names = FALSE, row.names = FALSE)


