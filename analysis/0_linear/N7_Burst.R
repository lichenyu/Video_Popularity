workpath = 'F:/Video_Popularity/'


data = read.table(paste(workpath, 'analysis/2_predict_value/PBML+BP/150801+151017/I30_BP_value', sep = ''))
n7 = rowSums(data[2:8])
burst = data$V32

plot(n7, burst, xlim = c(0, 10000), ylim = c(0, 10000))
reg = lm(burst ~ n7 - 1)
summary(reg)
abline(0, reg$coefficients[1], col = 'red')
reg = lm(burst ~ n7)
summary(reg)
abline(reg$coefficients[1], reg$coefficients[2], col = 'red')


idx_p = which(n7 > 0)
log_n7 = log10(n7[idx_p])
log_burst = log10(burst[idx_p])

plot(log_n7, log_burst)
reg2 = lm(log_burst ~ log_n7)
summary(reg2)
abline(reg2$coefficients[1], reg2$coefficients[2], col = 'red')

idx_2 = which(n7 < 100)
n7_2 = n7[idx_2]
burst_2 = burst[idx_2]
plot(n7_2, burst_2, xlim = c(0, 100), ylim = c(0, 1000))
reg = lm(burst_2 ~ n7_2 - 1)
summary(reg)
abline(0, reg$coefficients[1], col = 'red')
