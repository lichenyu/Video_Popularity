workpath = 'F:/Video_Popularity/'

data = read.table(paste(workpath, 'src/pattern/150801+151017/I30_others_training', sep = ''))
i1 = data$V2
i2 = data$V3
i3 = data$V4
i4 = data$V5
i5 = data$V6
i6 = data$V7
i7 = data$V8
d = as.data.frame(data)
n30 = rowSums(data[2:31])


reg = lm(n30 ~ i1 + i2 + i3 + i4 + i5 + i6 + i7 - 1, weights = (1 / n30)^2)
summary(reg)
reg$coefficients
