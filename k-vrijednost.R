df1 <- read.csv('mojcsv.csv')
v1 <- df1[["broj"]]
v2 <- df1[["postotak"]]
lm(v1~v2)
df <- data.frame(v1,v2)
plot(v2~v1,df)
model <- lm(v2~v1,df)
lines(df$v1,predict(model),col='blue')
cor(v1,v2)
hist(v2)

