library(e1071)

#workpath = 'F:/Video_Popularity/'
workpath = '/Users/ouyangshuxin/Documents/work/Video_Popularity/'
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



naivebayes = naiveBayes(label ~ ., data = training_d)

prediction <- predict(naivebayes, test_f)

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
