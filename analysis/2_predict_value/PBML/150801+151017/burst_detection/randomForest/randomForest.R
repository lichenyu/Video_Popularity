library(randomForest)

workpath = 'F:/Video_Popularity/'

training = read.table(paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/training/I30_training_bp_features', sep = ''), header = TRUE)
training_df = as.data.frame(training[, 3:length(training)])
set.seed(10)
myForestrf = randomForest(label ~ ., training_df)
#print(myForestrf)
#importance(myForestrf)
#plot(myForestrf)





# training performance
ll = c(training$label)
pl = c(myForestrf$predicted)
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
test = read.table(paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/test/I30_test_bp_features', sep = ''), header = TRUE)
levels(test$public_type) = levels(training$public_type)
predict = predict(myForestrf, test, type = 'class')
ll = c(test$label)
pl = c(predict)
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


