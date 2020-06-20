function Network = SW_network_update(Network,length,l_side,n_side)
y=n_side/l_side;
for i=1:length
    for j=1:i
        r=rand(1);
        %disp(r);
        if (r>1) && (Network(i,j)==1)
            Network(i,j)=0;
            Network(j,i)=0;
        end
    end
end