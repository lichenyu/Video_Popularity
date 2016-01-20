workpath = 'F:/Video_Popularity/'
#workpath = '/Users/ouyangshuxin/Documents/Video_Popularity/'

data = read.table(paste(workpath, 'characterization/3_evolution_pattern/data', sep = ''))



pdf(paste(workpath, "characterization/3_evolution_pattern/patterns.pdf", sep = ''), 
    width = 7.5, height = 5)

par(mfrow=c(2, 3))

#d,l,u,r
par(mar=c(5, 5, 2, 2) + 0.1)
plot(seq(0, 30), data[1, ] / data[1, 31], type = "l", 
     xlim = c(0, 30), ylim = c(0, 1), 
     xlab = "Days Since Uploaded", ylab = "Normalized View Count", main = "Type 1", 
     col = "blue", lwd = 3)

#d,l,u,r
par(mar=c(5, 5, 2, 2) + 0.1)
plot(seq(0, 30), data[2, ] / data[2, 31], type = "l", 
     xlim = c(0, 30), ylim = c(0, 1), 
     xlab = "Days Since Uploaded", ylab = "Normalized View Count", main = "Type 2", 
     col = "blue", lwd = 3)

#d,l,u,r
par(mar=c(5, 5, 2, 2) + 0.1)
plot(seq(0, 30), data[3, ] / data[3, 31], type = "l", 
     xlim = c(0, 30), ylim = c(0, 1), 
     xlab = "Days Since Uploaded", ylab = "Normalized View Count", main = "Type 3", 
     col = "blue", lwd = 3)

#d,l,u,r
par(mar=c(5, 5, 2, 2) + 0.1)
plot(seq(0, 30), data[4, ] / data[4, 31], type = "l", 
     xlim = c(0, 30), ylim = c(0, 1), 
     xlab = "Days Since Uploaded", ylab = "Normalized View Count", main = "Type 4", 
     col = "blue", lwd = 3)

#d,l,u,r
par(mar=c(5, 5, 2, 2) + 0.1)
plot(seq(0, 30), data[5, ] / data[5, 31], type = "l", 
     xlim = c(0, 30), ylim = c(0, 1), 
     xlab = "Days Since Uploaded", ylab = "Normalized View Count", main = "Type 5", 
     col = "blue", lwd = 3)

#d,l,u,r
par(mar=c(5, 5, 2, 2) + 0.1)
plot(seq(0, 30), data[6, ] / data[6, 31], type = "l", 
     xlim = c(0, 30), ylim = c(0, 1), 
     xlab = "Days Since Uploaded", ylab = "Normalized View Count", main = "Type 6", 
     col = "blue", lwd = 3)

dev.off()
