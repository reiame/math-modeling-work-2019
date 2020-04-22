> a=rnorm(1000,mean=0,sd=1) #����1000���������������N(0��1)
> amean=mean(a) #���a��������������������
> avar=var(a) #������������ķ���
> hist(a,col="lightblue") #���������ֲ���ֱ��ͼ
> x=rpois(100,2) #����100���������������P(2)
> xmean=mean(x)
> xvar=var(x)
> hist(x,col="red")
> for(n in 1:1000){
+ y[n]=mean(rpois(100,lambda=2))
+ } #����1000����������
> sy <- (y-2)/sqrt(2) #��׼��
> symean=mean(sy) #��׼�����syi�ľ�ֵ
> syvar=var(sy) #����
> hist(sy,color="red")
> x2=runif(1000,min=5,max=10) #1000������������U(5,10)
> mean(x2)

> y2 <- 4*x2-6
> mean(y2)

> x2var=var(x2)
> y2var=var(y2)
> covx2y2=mean((x2-mean(x2))*(y2-mean(y2))) #X,Y��Э����
> covx2y2

> corrx2y2=covx2y2/(sqrt(x2var)*sqrt(y2var)) #X,Y�����ϵ��
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

