library(stats4)

data = read.table('F:\\Video_Popularity\\rawdata\\N7N30')
n7 = data$V2
n30 = data$V3
rn7 = n7 / n30
rn30 = n30 / n30
# get n7 > 0 for log
idx = which(n7 > 0)
length(n7) - length(idx)
n7_p = n7[idx]
n30_p = n30[idx]
rn7_p = n7_p / n30_p
rn30_p = n30_p / n30_p

# --------------------------------------------------
# Log-Linear with directly LS
# ln(y) = ln(x) + c
reg = lm(log(n30_p) ~ offset(log(n7_p)) + 1)
summary(reg)
reg$coefficients
inc = log(n30_p) - log(n7_p)
mean(inc)
# 0.3466905 -> just the mean of the intercept
# --------------------------------------------------


# --------------------------------------------------
# Log-Linear with least relative squares
# ln(y) = ln(x) + c
reg = lm(log(rn30_p) ~ offset(log(rn7_p)) + 1)
summary(reg)
reg$coefficients
rinc = log(rn30_p) - log(rn7_p)
mean(rinc)
# 0.3466905 -> just the mean of the intercept
# --------------------------------------------------


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
# c = ln(a), a = e^c
# --------------------------------------------------


# --------------------------------------------------
# Linear with directly LS
# y = ax
reg = lm(n30 ~ n7 - 1)
summary(reg)
reg$coefficients
# 1.293118
log(reg$coefficients)
# 0.2570567
# --------------------------------------------------


# --------------------------------------------------
# Linear with maximum likelihood estimation
# y = ax
LL <- function(a, sigma) {
  R = n30 - a * n7
  R = suppressWarnings(dnorm(R, 0, sigma, log = TRUE))
  -sum(R)
}
fit = mle(LL, start = list(a = 1.2, sigma = 1))
fit@coef[1]
# 1.294222
log(fit@coef[1])
# 0.2579097
# --------------------------------------------------


# --------------------------------------------------
# Linear with least relative squares
# y = ax
reg = lm(rn30 ~ rn7 - 1)
summary(reg)
reg$coefficients
# 1.235237
log(reg$coefficients)
# 0.2112632
# --------------------------------------------------


# --------------------------------------------------
# check calculated value ?= least relative squares
sum(rn7) / sum((rn7)^2)
# 1.235237
log(sum(rn7) / sum((rn7)^2))
# 0.2112632
# --------------------------------------------------


# --------------------------------------------------
# Linear with maximum likelihood estimation (relative values)
# y = ax
LL <- function(a, sigma) {
  R = rn30 - a * rn7
  R = suppressWarnings(dnorm(R, 0, sigma, log = TRUE))
  -sum(R)
}
fit = mle(LL, start = list(a = 1.2, sigma = 1))
fit@coef[1]
# 1.235237
log(fit@coef[1])
# 0.2112632
# --------------------------------------------------





# --------------------------------------------------
# N7 vs. N30
# --------------------------------------------------
# ln(y) = ln(x) + c
# LS: c = 0.3466905
# MLE: c = 0.3466935
# 
# y = ax
# c = ln(a)
# LS: a = 1.293118, c = 0.2570567
# LRS: a = 1.235237, c = 0.2112632
# --------------------------------------------------



# --------------------------------------------------
# For heavy tail, tail value count small but effect big.
# Log transform or directly user relative value.
# Log transform can deal with heavy tail situation, 
# however it can not ensure perform better
# --------------------------------------------------



# --------------------------------------------------
# N1 vs. N30
# --------------------------------------------------
# ln(y) = ln(x) + c
# LS: c = 0.7884632
# MLE: c = 0.7884630
# 
# y = ax
# c = ln(a)
# LS: a = 2.887398, c = 1.060356
# MLE: a = 2.87549, c = 1.056223
# LRS: a = 1.503376, c = 0.4077131
# MLE-R: a = 1.5033763, c = 0.4077134
# --------------------------------------------------




plot(log(n7), log(n30), xlim = c(0, 18), ylim = c(0, 18))


plot(n7, n30, xlim = c(0, 1000000), ylim = c(0, 1000000))



