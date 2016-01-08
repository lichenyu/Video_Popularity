workpath = 'F:/Video_Popularity/'
#workpath = '/Users/ouyangshuxin/Documents/work/Video_Popularity/'


#--------------------------------------------------
# PBML (+ indicator*a*n7)
data = read.table(paste(workpath, 'analysis/2_predict_value/PBML/150801+151017/burst_detection/rpart/I30_training_bp_predicted_others', sep = ''))
i1 = data$V2
i2 = data$V3
i3 = data$V4
i4 = data$V5
i5 = data$V6
i6 = data$V7
i7 = data$V8
n7 = rowSums(data[2:8])
n30 = rowSums(data[2:31])


reg = lm(n30 ~ i1 + i2 + i3 + i4 + i5 + i6 + i7 - 1, weights = (1 / n30)^2)
summary(reg)
reg$coefficients



burst = data$V32
bv = n7 * burst
reg = lm(n30 ~ i1 + i2 + i3 + i4 + i5 + i6 + i7 + bv - 1, weights = (1 / n30)^2)
summary(reg)
reg$coefficients
#--------------------------------------------------



#--------------------------------------------------
# PBML + indicator*(a*n7 + b)
data = read.table(paste(workpath, 'analysis/2_predict_value/PBML+BP/150801+151017/I30_others_training', sep = ''))
i1 = data$V2
i2 = data$V3
i3 = data$V4
i4 = data$V5
i5 = data$V6
i6 = data$V7
i7 = data$V8
indicator = data$V32
n7 = rowSums(data[2:8])
n30 = rowSums(data[2:31])


reg = lm(n30 ~ i1 + i2 + i3 + i4 + i5 + i6 + i7 - 1, weights = (1 / n30)^2)
summary(reg)
reg$coefficients

bv1 = n7 * indicator
bv2 = indicator
reg = lm(n30 ~ i1 + i2 + i3 + i4 + i5 + i6 + i7 + bv1 + bv2 - 1, weights = (1 / n30)^2)
summary(reg)
reg$coefficients
#--------------------------------------------------



#--------------------------------------------------
# PBML + indicator*(a1*i1 + ... + a7*i7)
data = read.table(paste(workpath, 'analysis/2_predict_value/PBML+BP/150801+151017/I30_0000000_training', sep = ''))
i1 = data$V2
i2 = data$V3
i3 = data$V4
i4 = data$V5
i5 = data$V6
i6 = data$V7
i7 = data$V8
indicator = data$V32
n7 = rowSums(data[2:8])
n30 = rowSums(data[2:31])


reg = lm(n30 ~ i1 + i2 + i3 + i4 + i5 + i6 + i7 - 1, weights = (1 / n30)^2)
summary(reg)
reg$coefficients

bv1 = i1 * indicator
bv2 = i2 * indicator
bv3 = i3 * indicator
bv4 = i4 * indicator
bv5 = i5 * indicator
bv6 = i6 * indicator
bv7 = i7 * indicator
reg = lm(n30 ~ i1 + i2 + i3 + i4 + i5 + i6 + i7 + bv1 + bv2 + bv3 + bv4 + bv5 + bv6 + bv7 - 1, weights = (1 / n30)^2)
summary(reg)
reg$coefficients
#--------------------------------------------------