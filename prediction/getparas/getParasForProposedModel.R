#workpath = 'F:/Video_Popularity/'
workpath = '/Users/ouyangshuxin/Documents/Video_Popularity/'



data = read.table(paste(workpath, 'prediction/i25p4/burst_prediction/I30_training_bp_others', sep = ''))
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
i14 = data$V15
i15 = data$V16
i16 = data$V17
i17 = data$V18
i18 = data$V19
i19 = data$V20
i20 = data$V21
i21 = data$V22
i22 = data$V23
i23 = data$V24
i24 = data$V25
i25 = data$V26
ni = rowSums(data[2:26])
n30 = rowSums(data[2:31])

burst = data$V32
bv = ni * burst
reg = lm(n30 ~ i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11 + i12 + i13 + i14 + i15 + i16 + i17 + i18 + i19 + i20 + i21 + i22 + i23 + i24 + i25 + bv - 1, weights = (1 / n30)^2)
summary(reg)
reg$coefficients
