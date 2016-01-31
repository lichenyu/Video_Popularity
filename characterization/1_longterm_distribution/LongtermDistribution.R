#workpath = 'F:/Video_Popularity/'
workpath = '/Users/ouyangshuxin/Documents/Video_Popularity/'

data = read.table(paste(workpath, 'rawdata/150801+151017/I30', sep = ''))
#i1 = data$V2
n1 = data$V2
n7 = rowSums(data[2:8])
n30 = rowSums(data[2:31])



# pdf(paste(workpath, "characterization/1_longterm_distribution/longterm_distribution.pdf", sep = ''), 
#     width = 10, height = 4)
# par(mfrow=c(1, 2))
pdf(paste(workpath, "characterization/1_longterm_distribution/longterm_distribution.pdf", sep = ''), 
    width = 9, height = 2.5)
par(mfrow=c(1, 3))



e_1 = ecdf(n1)
e_7 = ecdf(n7)
e_30 = ecdf(n30)
#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
plot(e_1, do.points = FALSE, verticals = TRUE, col.01line = 0, 
     xlim = c(1, 100000), ylim = c(0, 1), axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "(a)", xlab = "View Count", ylab = "ECDF", 
     col = "green", lwd = 1, log = "x"
)
lines(e_7, do.points = FALSE, verticals = TRUE, col.01line = 0, 
      col = "red", lwd = 1)
lines(e_30, do.points = FALSE, verticals = TRUE, col.01line = 0, 
      col = "blue", lwd = 1)
axis(side = 1, at = c(1, 10, 100, 1000, 10000, 100000), 
     labels = expression('10'^0, '10'^1, '10'^2, '10'^3, '10'^4, '10'^5), tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 2, tck = 1, lty = 2, col = 'grey')
legend("bottomright", legend = c("View Count after a Day", 
                                 "View Count after a Week", 
                                 "View Count after a Month"), 
       lwd = rep(1, 3), col = c("green", "red", "blue"), 
       bg="white", cex = 0.8)
box()



library(MASS)
library(fitdistrplus)
library(actuar)

data = read.table(paste(workpath, 'rawdata/150801+151017/I30_151017', sep = ''))
n30_151017 = rowSums(data[2:31])

fp <- fitdist(n30_151017, "pareto")
#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
ppcomp(fp, fitcol = 'red', lwd = 6, 
       addlegend = FALSE, line01lty = 1, 
       main = "", sub = "(b)", 
       xlab = "Theoretical Probabilities", ylab = "Empirical Probabilities")
legend("bottomright", legend = c("Dataset 150801"), 
       pch = 19, col = "red", bg="white", cex = 0.8)
abline(0, 1, lty = 2, lwd = 1)

fp <- fitdist(n30, "pareto")
#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
ppcomp(fp, fitcol = 'red', lwd = 6, 
       addlegend = FALSE, line01lty = 1, 
       main = "", sub = "(c)", 
       xlab = "Theoretical Probabilities", ylab = "Empirical Probabilities")
legend("bottomright", legend = c("Dataset 151017"), 
       pch = 19, col = "red", bg="white", cex = 0.8)
abline(0, 1, lty = 2, lwd = 1)

dev.off()


