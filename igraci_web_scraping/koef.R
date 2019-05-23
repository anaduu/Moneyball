df1 <- read.csv('koef.csv')
v1 <- df1[["overall"]]
v2 <- df1[["koef"]]
lm(v1~v2)
df <- data.frame(v1,v2)
plot(v2~v1,df)
model <- lm(v2~v1,df)
lines(df$v1,predict(model),col='blue')
cor(v1,v2)
