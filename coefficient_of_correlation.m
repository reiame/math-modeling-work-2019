%We designed the following function to calculate the coefficient of correlation

function JK=relation(XJ,XK,a)
numerator=0;
deminoj=0;
deminok=0;
demino=0;
for I = 1:1:a   
    numerator=numerator +(XJ(i,1)-mean(XJ))*(XK(i,1)-mean(XK));
    deminoj=deminoj+(XJ(i,1)-mean(XJ))*(XJ(i,1)-mean(XJ));
    deminok=deminok+(XK(i,1)-mean(XK))*(XK(i,1)-mean(XK));
end
disp(numerator);
demino=deminoj*deminok;
demino=sqrt(demino);
disp(demino);
JK=numerator/demino;
end

AnalyzeOfData=zeros(20,20);
for j=1:1:20
    for k=1:1:20
        AnalyzeOfData(j,k)=abs(relation(VariableSet(:,j),VariableSet(:,k),10));
    end
end

%R-type Cluster Diagram

OneMatrix=ones(20);
Distance=OneMatrix-AnalyzeOfData;
Distance=tril(Distance);
DistanceWITHOUTzero=nonzeros(Distance);
DWZ=DistanceWITHOUTzero';
z=linkage(DWZ,'complete');
y=cluster(z,'maxclust',2);
ind1=find(y==1);ind1=ind1';
ind2=find(y==2);ind2=ind2';
h=dendrogram(z);
set(h,'color','k','linewidth',1.3);
title('R-type cluster diagram of 20 Economic Vitality Factors');
xlabel('Factor Type');ylabel('The Sum of Distance');
ylabel('Distance');
