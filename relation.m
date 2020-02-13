function JK=relation(XJ,XK,a)

numerator=0;
deminoj=0;
deminok=0;
demino=0;
for i=1:1:a   
    numerator=numerator+(XJ(i,1)-mean(XJ))*(XK(i,1)-mean(XK));
    deminoj=deminoj+(XJ(i,1)-mean(XJ))*(XJ(i,1)-mean(XJ));
    deminok=deminok+(XK(i,1)-mean(XK))*(XK(i,1)-mean(XK));
end
disp(numerator);
demino=deminoj*deminok;
demino=sqrt(demino);
disp(demino);
JK=numerator/demino;
end
