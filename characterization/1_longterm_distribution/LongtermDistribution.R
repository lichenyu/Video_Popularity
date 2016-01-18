workpath = 'F:/Video_Popularity/'
#workpath = '/Users/ouyangshuxin/Documents/work/Video_Popularity/'

data = read.table(paste(workpath, 'rawdata/150801+151017/N30', sep = ''))
n30 = data$V31

e = ecdf(n30)

pdf("C:\\Documents and Settings\\Administrator\\桌面\\vc_day30.pdf", width = 5, height = 7)
par(mfrow=c(2,1))

#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
plot(e, do.points = FALSE, verticals = TRUE, col.01line = 0, 
     xlim = c(1, 10000), ylim = c(0, 1), axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "(a)", xlab = "View Count", ylab = "ECDF", 
     col = "blue", lwd = 2, log = "x"
)
axis(side = 1, at = c(1, 10, 100, 1000, 10000), labels = c(1, 10, 100, 1000, 10000), tck = 1, lty = 2)
axis(side = 2, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 2, tck = 1, lty = 2)
box()



library(MASS)
library(fitdistrplus)
library(actuar)
n30_100000 = n30[n30 <= 100000]
fp <- fitdist(n30, "pareto")
plot(fp)
#ppcomp(fp, line01lty = 1)
#summary(fp)

ppcomp(fp, fitpch = 10)

#d,l,u,r
par(mar=c(6, 4, 1, 2) + 0.1)
ppcomp(fp, 
       fitpch = c(2), fitcol = 'red', 
       addlegend = FALSE, line01lty = 1, 
       main = "", sub = "(b)", 
       xlab = "Theoretical Probabilities", ylab = "Empirical Probabilities")
abline(0, 1)

dev.off()
