library(rpart)

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



set.seed(10)
tree = rpart(label ~ ., training_d, control = rpart.control(xval = 10, cp = 0.001));
tree_cp = printcp(tree)
#1-SE rule
pruned_cp_row = min((1 : dim(tree_cp)[1])[tree_cp[,"xerror"] < min(tree_cp[, "xerror"] + tree_cp[, "xstd"])])
tree_pruned = prune(tree, cp = tree_cp[pruned_cp_row, "CP"])



# training performance
prediction = predict(tree_pruned, training_f, type = 'class')
ll = c(training_l)
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

out_df <- data.frame(training$vid, ll - 1, pl - 1);
write.table(out_df, 
            file = paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/rpart/I30_training_results', sep = ''), 
            sep = '\t', quote = FALSE, col.names = FALSE, row.names = FALSE)



# test performance
prediction = predict(tree_pruned, test_f, type = 'class')
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
            file = paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection//rpart/I30_test_results', sep = ''), 
            sep = '\t', quote = FALSE, col.names = FALSE, row.names = FALSE)


