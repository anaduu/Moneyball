df1 <- read.csv('croatia.csv')
v1 <- df[["Overall"]]
df2 <- read.csv('brazil.csv')
v2 <- df[["Overall"]]
t.test(v1,v2,var.equal=T,alternative="less")
