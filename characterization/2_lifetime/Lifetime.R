workpath = 'F:/Video_Popularity/'
#workpath = '/Users/ouyangshuxin/Documents/Video_Popularity/'

data = read.table(paste(workpath, 'characterization/2_lifetime/lifetime', sep = ''))

vc = data$V2
lifetime = data$V3
active_idx = which(30 <= vc)
lifetime_active = lifetime[active_idx]
lifetime_inactive = lifetime[-active_idx]

pdf(paste(workpath, "characterization/2_lifetime/lifetime.pdf", sep = ''), 
    width = 5, height = 4)



e = ecdf(lifetime)
e_active = ecdf(lifetime_active)
e_inactive = ecdf(lifetime_inactive)
#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
plot(e_inactive, do.points = FALSE, verticals = TRUE, col.01line = 0, 
     xlim = c(0, 30), ylim = c(0, 1), axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "", xlab = "Lifetime (days)", ylab = "ECDF", 
     col = "red", lwd = 2, lty = 6
)
lines(e_active, do.points = FALSE, verticals = TRUE, col.01line = 0, 
      col = "green", lwd = 2, lty = 2)
lines(e, do.points = FALSE, verticals = TRUE, col.01line = 0, 
      col = "blue", lwd = 2, lty = 1)
axis(side = 1, at = seq(0, 30, 1), labels = rep("", 31), tck = 1, lty = 2, col = 'grey')
axis(side = 1, at = seq(0, 30, 5), labels = seq(0, 30, 5))
axis(side = 2, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 2, tck = 1, lty = 2, col = 'grey')
legend("bottomright", legend = c("All Videos", "Active Videos", "Inactive Videos"), 
       lty = c(1, 2, 6), lwd = rep(2, 3), col = c("blue", "green", "red"), 
       bg="white", cex = 0.8)
box()



dev.off()
