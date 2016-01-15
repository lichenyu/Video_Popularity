library(class)

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



title_booktitle_flag = training_f$title_booktitle_flag
title_booktitle_flag = model.matrix(~title_booktitle_flag-1)
training_f$title_booktitle_flag = NULL
category = training_f$category
category = model.matrix(~category-1)
training_f$category = NULL
public_type = training_f$public_type
public_type = model.matrix(~public_type-1)
training_f$public_type = NULL
copyright_type = training_f$copyright_type
copyright_type = model.matrix(~copyright_type-1)
training_f$copyright_type = NULL
streamtypes_hd2 = training_f$streamtypes_hd2
streamtypes_hd2 = model.matrix(~streamtypes_hd2-1)
training_f$streamtypes_hd2 = NULL
gender = training_f$gender
gender = model.matrix(~gender-1)
training_f$gender = NULL
is_vip = training_f$is_vip
is_vip = model.matrix(~is_vip-1)
training_f$is_vip = NULL
is_share = training_f$is_share
is_share = model.matrix(~is_share-1)
training_f$is_share = NULL
is_verified = training_f$is_verified
is_verified = model.matrix(~is_verified-1)
training_f$is_verified = NULL
training_f = cbind(training_f, title_booktitle_flag, category, public_type, copyright_type, 
                    streamtypes_hd2, gender, is_vip, is_share, is_verified)

title_booktitle_flag = test_f$title_booktitle_flag
title_booktitle_flag = model.matrix(~title_booktitle_flag-1)
test_f$title_booktitle_flag = NULL
category = test_f$category
category = model.matrix(~category-1)
test_f$category = NULL
public_type = test_f$public_type
public_type = model.matrix(~public_type-1)
test_f$public_type = NULL
copyright_type = test_f$copyright_type
copyright_type = model.matrix(~copyright_type-1)
test_f$copyright_type = NULL
streamtypes_hd2 = test_f$streamtypes_hd2
streamtypes_hd2 = model.matrix(~streamtypes_hd2-1)
test_f$streamtypes_hd2 = NULL
gender = test_f$gender
gender = model.matrix(~gender-1)
test_f$gender = NULL
is_vip = test_f$is_vip
is_vip = model.matrix(~is_vip-1)
test_f$is_vip = NULL
is_share = test_f$is_share
is_share = model.matrix(~is_share-1)
test_f$is_share = NULL
is_verified = test_f$is_verified
is_verified = model.matrix(~is_verified-1)
test_f$is_verified = NULL
test_f = cbind(test_f, title_booktitle_flag, category, public_type, copyright_type, 
                   streamtypes_hd2, gender, is_vip, is_share, is_verified)



set.seed(10)
prediction = knn(training_f, test_f, training_l, k = 9)

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


table(ll, pl)

accuracy = rep(0, 10)
k = 1:10
for(x in k){
  set.seed(10)
  prediction <- knn(training_f, test_f, training_l, k = x)
  accuracy[x] <- mean(prediction == test_l)
}

plot(k, accuracy, type = 'b')
