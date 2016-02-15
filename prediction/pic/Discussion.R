#workpath = 'F:/Video_Popularity/'
workpath = '/Users/ouyangshuxin/Documents/Video_Popularity/'

indidate = read.table(paste(workpath, 'prediction/pic/iterate_indidate', sep = ''), sep = ',')
pattern = read.table(paste(workpath, 'prediction/pic/iterate_pattern', sep = ''), sep = ',')

indidate_x = seq(5, 25, 2)
pattern_x = seq(1, 7, 1)



pdf(
  paste(workpath, "prediction/pic/discussion.pdf", sep = ''),
  width = 10, height = 4
)

par(mfrow = c(1, 2))

#d,l,u,r
par(mar = c(5, 5, 1, 2) + 0.1)
plot(
  indidate_x, indidate[1,] * 100, type = 'l', axes = FALSE, xaxs = "i", yaxs =
    "i",
  xlim = c(5, 25), ylim = c(1, 8),
  xlab = "Indicator Date", ylab = "MRSE (%)", sub = "(a)",
  lty = 2, lwd = 2, col = "blue"
)
lines(
  indidate_x, indidate[2,] * 100, lty = 2, lwd = 2, col = "green"
)
lines(indidate_x, indidate[3,] * 100, lwd = 2, col = "red")
axis(
  side = 1, at = seq(5, 25, 2), labels = seq(5, 25, 2), tck = 1, lty = 2, col = "grey"
)
axis(
  side = 2, at = seq(0, 8, 1), labels = seq(0, 8, 1), tck = 1, lty = 2, col = "grey"
)
legend(
  "topright", legend = c("Log-Linear", "Multi-Linear", "EPBL_ML"),
  lwd = rep(2, 3), col = c("blue", "green", "red"),
  lty = c(2, 2, 1), bg = "white", cex = 0.8
)
box()

#d,l,u,r
par(mar = c(5, 5, 1, 2) + 0.1)
plot(
  pattern_x, pattern[1,] * 100, type = "b",
  xlim = c(1, 7), ylim = c(5.9, 6.3),
  xlab = "Pattern Count", ylab = "MRSE (%)", sub = "(b)",
  lty = 2, lwd = 2, col = 'blue'
)

dev.off()
