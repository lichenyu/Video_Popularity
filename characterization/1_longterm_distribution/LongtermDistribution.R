workpath = 'F:/Video_Popularity/'
#workpath = '/Users/ouyangshuxin/Documents/Video_Popularity/'

data = read.table(paste(workpath, 'rawdata/150801+151017/N30', sep = ''))
n30 = data$V31



pdf(paste(workpath, "characterization/1_longterm_distribution/longterm_distribution.pdf", sep = ''), 
    width = 10, height = 4)
par(mfrow=c(1, 2))



e = ecdf(n30)
#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
plot(e, do.points = FALSE, verticals = TRUE, col.01line = 0, 
     xlim = c(1, 100000), ylim = c(0, 1), axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "(a)", xlab = "View Count", ylab = "ECDF", 
     col = "blue", lwd = 2, log = "x"
)
axis(side = 1, at = c(1, 10, 100, 1000, 10000, 100000), 
     labels = expression('10'^0, '10'^1, '10'^2, '10'^3, '10'^4, '10'^5), tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 2, tck = 1, lty = 2, col = 'grey')
box()



library(MASS)
library(fitdistrplus)
library(actuar)
fp <- fitdist(n30, "pareto")
#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
ppcomp(fp, fitcol = 'red', lwd = 10, 
       addlegend = FALSE, line01lty = 1, 
       main = "", sub = "(b)", 
       xlab = "Theoretical Probabilities", ylab = "Empirical Probabilities")
abline(0, 1, lty = 2, col = 'grey')


dev.off()
