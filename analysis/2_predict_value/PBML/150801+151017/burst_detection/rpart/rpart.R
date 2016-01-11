library(rpart)
library(rpart.plot)

workpath = 'F:/Video_Popularity/'

training = read.table(paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/training/I30_training_bp_features', sep = ''), header = TRUE)
training_df = as.data.frame(training[, 3:length(training)])
set.seed(10)
mytree = rpart(label ~ ., training_df, control = rpart.control(xval = 10, cp = 0.001));

tree_cp = printcp(mytree)
#1-SE rule
prune_cp_row = min((1 : dim(tree_cp)[1])[tree_cp[,"xerror"] < min(tree_cp[, "xerror"] + tree_cp[, "xstd"])])
mytree_prune = prune(mytree, cp = tree_cp[prune_cp_row, "CP"])

printcp(mytree_prune)
print(mytree_prune$variable.importance);
plot(mytree_prune);
#text(mytree_prune, use.n=T);
#prp(mytree_prune, faclen = 0, cex = 0.8, extra = 1)



# training performance
predict = predict(mytree_prune, training, type = 'class')
ll = c(training$label)
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

out_df <- data.frame(training$vid, ll - 1, pl - 1);
write.table(out_df, 
            file = paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/rpart/I30_training_results', sep = ''), 
            sep = '\t', quote = FALSE, col.names = FALSE, row.names = FALSE)



# test performance
test = read.table(paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/test/I30_test_bp_features', sep = ''), header = TRUE)
predict = predict(mytree_prune, test, type = 'class')
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
            file = paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection//rpart/I30_test_results', sep = ''), 
            sep = '\t', quote = FALSE, col.names = FALSE, row.names = FALSE)










