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



accuracy = rep(0, 36)
g = 10^(-3 : 2)
c = 10^(0 : 5)
g_idx = 1 : 6
c_idx = 1 : 6
for(i in c_idx){
  for(j in g_idx){
    print(i)
    print(c[i])
    print(j)
    print(g[j])
    print((i - 1) * 6 + j)
    set.seed(10)
    svm = svm(label ~ ., data = training_d, gamma = g[j], cost = c[i])
    prediction = predict(svm, test_f)
    ll = c(test_l)
    pl = c(prediction)
    accuracy[(i - 1) * 6 + j] = length(which(pl == ll & ll == 2)) + length(which(pl == ll & ll == 1))
    print(accuracy[(i - 1) * 6 + j])
  }
}



# set.seed(10)
# tuned = tune(svm, label ~ ., data = training_d, 
#              ranges = list(gamma = 10^(-6 : -1), cost = 10^(0 : 5)), 
#              tunecontrol = tune.control(cross = 3))
# summary(tuned)
# tuned$best.model

set.seed(10)
svm = svm(label ~ ., data = training_d, gamma = 0.1, cost = 1, cross = 3)
summary(svm)

prediction = predict(svm, test_f)

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
