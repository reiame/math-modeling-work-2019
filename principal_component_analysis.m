%Principal Component Analysis

problem3zscore=zscore(problem3);
r=corrcoef(problem3zscore);
[x,y,z]=pcacov(r)
f=repmat(sign(sum(x)),size(x,1),1);
x=x.*f
df=problem3zscore*x(:,[1:num]);
num=4;
df=problem3zscore*x(:,[1:num]);
tf=df*z(1:num)/100;
[stf,ind]=sort(tf,'descend');
stf=stf',ind=ind'
