library(stats4)

data = read.table('C:/Documents and Settings/Administrator/桌面/vc/data/N7N30')

n7 = data$V2
n30 = data$V3
idx = which(n7 > 0)
n7 = n7[idx]
n30 = n30[idx]
rn7 = n7 / n30
rn30 = n30 / n30

# --------------------------------------------------
# Log-Linear with directly LS
# ln(y) = ln(x) + c
reg = lm(log(n30) ~ offset(log(n7)) + 1)
summary(reg)
reg$coefficients
inc = log(n30) - log(n7)
mean(inc)
# 0.7884632 -> just the mean of the intercept
# --------------------------------------------------


# --------------------------------------------------
# Log-Linear with least relative squares
# ln(y) = ln(x) + c
reg = lm(log(rn30) ~ offset(log(rn7)) + 1)
summary(reg)
reg$coefficients
rinc = log(rn30) - log(rn7)
mean(rinc)
# 0.7884632 -> just the mean of the intercept
# --------------------------------------------------


# --------------------------------------------------
# Log-Linear with maximum likelihood estimation
# ln(y) = ln(x) + c
LL <- function(c, sigma) {
  R = log(n30) - log(n7) - c
  R = suppressWarnings(dnorm(R, 0, sigma, log = TRUE))
  -sum(R)
}
fit = mle(LL, start = list(c = 1, sigma = 1))
fit@coef
# 0.7884630

LL <- function(c, mu, sigma) {
  R = log(n30) - log(n7) - c
  R = suppressWarnings(dnorm(R, mu, sigma, log = TRUE))
  -sum(R)
}
fit = mle(LL, start = list(c = 1, mu = 0, sigma = 1))
fit@coef
# 0.8942317
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
# 2.887398
log(reg$coefficients)
# 1.060356
# --------------------------------------------------


# --------------------------------------------------
# Linear with maximum likelihood estimation
# y = ax
LL <- function(a, sigma) {
  R = n30 - a * n7
  R = suppressWarnings(dnorm(R, 0, sigma, log = TRUE))
  -sum(R)
}
fit = mle(LL, start = list(a = 1, sigma = 1))
fit@coef
# 2.87549
log(fit@coef)
# 1.056223

LL <- function(a, mu, sigma) {
  R = n30 - a * n7
  R = suppressWarnings(dnorm(R, mu, sigma, log = TRUE))
  -sum(R)
}
fit = mle(LL, start = list(a = 1, mu = 0, sigma = 1))
fit@coef
# 2.887285
log(fit@coef)
# 1.060317
# --------------------------------------------------


# --------------------------------------------------
# Linear with least relative squares
# y = ax
reg = lm(rn30 ~ rn7 - 1)
summary(reg)
reg$coefficients
# 1.503376
log(reg$coefficients)
# 0.4077131
# --------------------------------------------------


# --------------------------------------------------
# check calculated value ?= least relative squares
sum(rn7) / sum((rn7)^2)
# 1.503376
log(sum(rn7) / sum((rn7)^2))
# 0.4077131
# --------------------------------------------------


# --------------------------------------------------
# Linear with maximum likelihood estimation (relative values)
# y = ax
LL <- function(a, sigma) {
  R = rn30 - a * rn7
  R = suppressWarnings(dnorm(R, 0, sigma, log = TRUE))
  -sum(R)
}
fit = mle(LL, start = list(a = 1, sigma = 1))
fit@coef
# 1.5033763
log(fit@coef)
# 0.4077134
# --------------------------------------------------


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

# heavy tail, tail value count small but effect big
# log transform or directly user relative value
# --------------------------------------------------



plot(log(n7), log(n30), xlim = c(0, 18), ylim = c(0, 18))


plot(n7, n30, xlim = c(0, 15000000), ylim = c(0, 33000000))



