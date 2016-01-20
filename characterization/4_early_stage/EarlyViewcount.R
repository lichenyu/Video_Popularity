workpath = 'F:/Video_Popularity/'
#workpath = '/Users/ouyangshuxin/Documents/Video_Popularity/'

data = read.table(paste(workpath, 'rawdata/150801+151017/I30', sep = ''))
n7 = rowSums(data[2:8])
n30 = rowSums(data[2:31])

data_demo = read.table(paste(workpath, 'characterization/4_early_stage/data', sep = ''))

data_burst_after7 = read.table(paste(workpath, 'characterization/4_early_stage/I30_burst_after7', sep = ''))
n7_burst_after7 = rowSums(data_burst_after7[2:8])
n30_burst_after7 = rowSums(data_burst_after7[2:31])

data_pattern0 = read.table(paste(workpath, 'characterization/4_early_stage/I30_pattern0', sep = ''))
n7_pattern0 = rowSums(data_pattern0[2:8])
n30_pattern0 = rowSums(data_pattern0[2:31])

data_others = read.table(paste(workpath, 'characterization/4_early_stage/I30_others', sep = ''))
n7_others = rowSums(data_others[2:8])
n30_others = rowSums(data_others[2:31])



pdf(paste(workpath, "characterization/4_early_stage/n7n30.pdf", sep = ''), 
    width = 10, height = 4)

par(mfrow=c(1, 2))

#d,l,u,r
par(mar=c(5, 5, 1, 2) + 0.1)
plot(n7, n30, type = "p", pch = 20, cex = 0.4, 
     xlim = c(0, 10000), ylim = c(0, 10000), 
     xlab = "View Count on the 7th Day", ylab = "View Count on the 30th Day", sub = "(a)", 
     col = "grey")

#d,l,u,r
par(mar=c(5, 5, 1, 2) + 0.1)
plot(seq(0, 30), data_demo[1, ], type = "l", 
     xlim = c(0, 30), ylim = c(0, 450), 
     xlab = "Days Since Uploaded", ylab = "View Count", main = "", sub = "(b)", 
     col = "blue", lwd = 2, lty = 1)
lines(seq(0, 30), data_demo[2, ], type = "l", col = "red", lwd = 2, lty = 2)
lines(seq(0, 30), data_demo[3, ], type = "l", col = "green", lwd = 2, lty = 6)
lines(c(7, 7), c(-10, 600), col = "grey", lty = 2)
legend("topleft", legend = c("Video1", "Video2", "Video3"), 
       lty = c(1, 2, 6), lwd = rep(2, 3), col = c("blue", "red", "green"), 
       bg="white", cex = 0.8)

dev.off()




pdf(paste(workpath, "characterization/4_early_stage/n7n30_2.pdf", sep = ''), 
    width = 9, height = 2.5)

par(mfrow=c(1, 3))

#d,l,u,r
par(mar=c(5, 5, 1, 2) + 0.1)
plot(n7_pattern0, n30_pattern0, type = "p", pch = 20, cex = 0.4, 
     xlim = c(0, 10000), ylim = c(0, 10000), 
     xlab = "View Count on the 7th Day", ylab = "View Count on the 30th Day", sub = "(a)", 
     col = "grey")
abline(0, 1)

#d,l,u,r
par(mar=c(5, 5, 1, 2) + 0.1)
plot(n7_others, n30_others, type = "p", pch = 20, cex = 0.4, 
     xlim = c(0, 10000), ylim = c(0, 10000), 
     xlab = "View Count on the 7th Day", ylab = "View Count on the 30th Day", sub = "(b)", 
     col = "grey")
abline(0, 1)


#d,l,u,r
par(mar=c(5, 5, 1, 2) + 0.1)
plot(n7_burst_after7, n30_burst_after7, type = "p", pch = 20, cex = 0.4, 
     xlim = c(0, 10000), ylim = c(0, 10000), 
     xlab = "View Count on the 7th Day", ylab = "View Count on the 30th Day", sub = "(c)", 
     col = "grey")
abline(0, 1)



dev.off()
