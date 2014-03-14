function [ data ] = maxPool( d, pSize, sSize )
%maxPool Max-pooling SIFT Features

assert(mod(sSize,pSize)==0,'Max Pool Failure : Dimensions dont match');

[m,n] = size(d);
data = zeros(m,n/pSize);

numPools = n/pSize;
for i=1:numPools,
    dStart = (i-1)*pSize +1;
    dEnd = dStart + pSize-1;
    cur = d(:,dStart:dEnd);
    new = max(cur,[],2);
    data(:,i) = new;
end
    
end

