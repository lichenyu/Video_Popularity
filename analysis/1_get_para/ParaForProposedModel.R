library(stats4)

data = read.table('F:\\Video_Popularity\\src\\burst\\BurstSlow_rate')
n7 = data$V2
n30 = data$V3
rate = data$V4



# --------------------------------------------------
# Linear with least weighted squares
# n30 = a * n7
reg = lm(n30 ~ n7 - 1, weights = (1 / n30) ^ 2)
summary(reg)
reg$coefficients
# ---

idx = which(rate != 0)
rate_p = rate[idx]
n30_p = n30[idx]
n7_p = n7[idx]
rate_n7_p = rate_p * n7_p
reg = lm(n30_p ~ rate_n7_p - 1, weights = (1 / n30_p) ^ 2)
summary(reg)
reg$coefficients
# 0.6653772
# --------------------------------------------------

# n30 - n7 = (a * rate + b) * n7
