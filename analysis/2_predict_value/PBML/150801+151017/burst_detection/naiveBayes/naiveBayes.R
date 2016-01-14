library(e1071)

#workpath = 'F:/Video_Popularity/'
workpath = '/Users/ouyangshuxin/Documents/work/Video_Popularity/'

training = read.table(paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/training/I30_training_bp_features', sep = ''), header = TRUE)
training_df = as.data.frame(training[, 3:length(training)])

model = naiveBayes(label ~ ., data = training_df)



test = read.table(paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/test/I30_test_bp_features', sep = ''), header = TRUE)
levels(test$public_type) = levels(training$public_type)

prediction <- predict(model, test)

ll = c(test$label)
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
