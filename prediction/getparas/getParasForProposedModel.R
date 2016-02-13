#workpath = 'F:/Video_Popularity/'
workpath = '/Users/ouyangshuxin/Documents/Video_Popularity/'



data = read.table(paste(workpath, 'prediction/i13p4/burst_prediction/I30_training_bp_1000000000000', sep = ''))
i1 = data$V2
i2 = data$V3
i3 = data$V4
i4 = data$V5
i5 = data$V6
i6 = data$V7
i7 = data$V8
i8 = data$V9
i9 = data$V10
i10 = data$V11
i11 = data$V12
i12 = data$V13
i13 = data$V14
ni = rowSums(data[2:14])
n30 = rowSums(data[2:31])

burst = data$V32
bv = ni * burst
reg = lm(n30 ~ i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11 + i12 + i13 + bv - 1, weights = (1 / n30)^2)
summary(reg)
reg$coefficients
