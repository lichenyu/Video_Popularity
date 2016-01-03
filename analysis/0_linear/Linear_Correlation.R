workpath = 'F:/Video_Popularity/'


# get n7 > 0 for log
#idx = which(n7 > 0)
#length(n7) - length(idx)
#n7_p = n7[idx]
#n30_p = n30[idx]

data = read.table(paste(workpath, 'rawdata/150801+151017/N30', sep = ''))
n7 = data$V2
n30 = data$V3
plot(n7, n30, pch = 20, xlim = c(0, 10000), ylim = c(0, 10000))

data = read.table(paste(workpath, 'src/burst/150801+151017/N30_1000000', sep = ''))
n7 = data$V2
n30 = data$V3
lines(n7, n30, type = 'p', pch = 20, col = 'blue')

data = read.table(paste(workpath, 'src/burst/150801+151017/N30_0000000', sep = ''))
n7 = data$V2
n30 = data$V3
lines(n7, n30, type = 'p', pch = 20, col = 'red')

data = read.table(paste(workpath, 'src/burst/150801+151017/N30_1100000', sep = ''))
n7 = data$V2
n30 = data$V3
lines(n7, n30, type = 'p', pch = 20, col = 'green')

data = read.table(paste(workpath, 'src/burst/150801+151017/N30_0100000', sep = ''))
n7 = data$V2
n30 = data$V3
lines(n7, n30, type = 'p', pch = 20, col = 'orange')

data = read.table(paste(workpath, 'src/burst/150801+151017/N30_1001000', sep = ''))
n7 = data$V2
n30 = data$V3
lines(n7, n30, type = 'p', pch = 1, col = 'purple')

data = read.table(paste(workpath, 'src/burst/150801+151017/N30_0001000', sep = ''))
n7 = data$V2
n30 = data$V3
lines(n7, n30, type = 'p', pch = 1, col = 'pink')
