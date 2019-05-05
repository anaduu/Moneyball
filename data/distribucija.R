df1 <- read.csv('croatia.csv')
v1 <- df1[["Overall"]]
df2 <- read.csv('brazil.csv')
v2 <- df2[["Overall"]]
t.test(v1,v2,var.equal=T,alternative="less")
