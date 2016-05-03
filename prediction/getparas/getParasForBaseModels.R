#workpath = 'F:/Video_Popularity/'
workpath = '/Users/ouyangshuxin/Documents/Video_Popularity/'

data = read.table(paste(workpath, 'prediction/datasets/I30_training', sep = ''))
i1 = data$V2
i2 = data$V3
i3 = data$V4
i4 = data$V5
i5 = data$V6
i6 = data$V7
i7 = data$V8
n7 = rowSums(data[2:8])
n30 = rowSums(data[2:31])



# --------------------------------------------------
# Log-Linear with maximum likelihood estimation
# ln(y) = ln(x) + c
library(stats4)
# get n7 > 0 for log
idx = which(ni > 0)
length(ni) - length(idx)
ni_p = ni[idx]
n30_p = n30[idx]
LL <- function(c, sigma) {
  R = log(n30_p) - log(ni_p) - c
  R = suppressWarnings(dnorm(R, 0, sigma, log = TRUE))
  -sum(R)
}
fit = mle(LL, start = list(c = 0.3, sigma = 1))
fit@coef[1]
# --------------------------------------------------

# --------------------------------------------------
# Linear with least weighted squares
# y = ax
# c = ln(a), a = e^c
reg = lm(n30 ~ n7 - 1, weights = (1 / n30) ^ 2)
summary(reg)
reg$coefficients
log(reg$coefficients)
# --------------------------------------------------

# --------------------------------------------------
# Multi-Linear with weighted LS
# y = a1x1 + ... + a7x7
reg = lm(n30 ~ i1 + i2 + i3 + i4 + i5 + i6 + i7 - 1)
summary(reg)
reg = lm(n30 ~ i1 + i2 + i3 + i4 + i5 + i6 + i7 - 1, weights = (1 / n30)^2)
summary(reg)
reg$coefficients
# --------------------------------------------------


