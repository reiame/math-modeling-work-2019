> a=rnorm(1000,mean=0,sd=1) #生成1000个随机变量，服从N(0，1)
> amean=mean(a) #求出a（即上述样本）的期望
> avar=var(a) #求出上述样本的方差
> hist(a,col="lightblue") #画出样本分布的直方图
> x=rpois(100,2) #生成100个随机变量，服从P(2)
> xmean=mean(x)
> xvar=var(x)
> hist(x,col="red")
> for(n in 1:1000){
+ y[n]=mean(rpois(100,lambda=2))
+ } #生成1000组上述样本
> sy <- (y-2)/sqrt(2) #标准化
> symean=mean(sy) #标准化后的syi的均值
> syvar=var(sy) #方差
> hist(sy,color="red")
> x2=runif(1000,min=5,max=10) #1000个样本，服从U(5,10)
> mean(x2)

> y2 <- 4*x2-6
> mean(y2)

> x2var=var(x2)
> y2var=var(y2)
> covx2y2=mean((x2-mean(x2))*(y2-mean(y2))) #X,Y的协方差
> covx2y2

> corrx2y2=covx2y2/(sqrt(x2var)*sqrt(y2var)) #X,Y的相关系数
> corrx2y2

> corr_test <- function(n){
+ y_n=x2*exp(2*x2^(n-1))
+ covx2y_n=mean((x2-mean(x2))*(y_n-mean(y_n)))
+ corrx2y_n=covx2y_n/(sqrt(x2var)*sqrt(var(y_n)))
+ corrx2y_n
+ }
> corr_test(1)

> corr_test(2)

> corr_test(3)


