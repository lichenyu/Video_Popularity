library(stats4)

workpath = 'F:/Video_Popularity/'

data = read.table(paste(workpath, 'rawdata/150801+151017/N7N30', sep = ''))
n7 = data$V2
n30 = data$V3
# get n7 > 0 for log
idx = which(n7 > 0)
length(n7) - length(idx)
n7_p = n7[idx]
n30_p = n30[idx]


# --------------------------------------------------
# Log-Linear with maximum likelihood estimation
# ln(y) = ln(x) + c
LL <- function(c, sigma) {
  R = log(n30_p) - log(n7_p) - c
  R = suppressWarnings(dnorm(R, 0, sigma, log = TRUE))
  -sum(R)
}
fit = mle(LL, start = list(c = 0.3, sigma = 1))
fit@coef[1]
# 0.3466935
# --------------------------------------------------

# --------------------------------------------------
# Linear with least weighted squares
# y = ax
# c = ln(a), a = e^c
reg = lm(n30 ~ n7 - 1, weights = (1 / n30) ^ 2)
summary(reg)
reg$coefficients
# 1.235237
log(reg$coefficients)
# 0.2112632
# --------------------------------------------------


data = read.table(paste(workpath, 'rawdata/150801+151017/I7N30', sep = ''))
i1 = data$V2
i2 = data$V3
i3 = data$V4
i4 = data$V5
i5 = data$V6
i6 = data$V7
i7 = data$V8
n30 = data$V9


# --------------------------------------------------
# Multi-Linear with weighted LS
# y = a1x1 + ... + a7x7
reg = lm(n30 ~ i1 + i2 + i3 + i4 + i5 + i6 + i7 - 1, weights = (1 / n30)^2)
summary(reg)
reg$coefficients
#1.179124 1.289353 1.241006 1.506698 1.352725 1.731021 2.237415
# --------------------------------------------------


