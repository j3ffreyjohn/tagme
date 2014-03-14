function [ ] = writeFiles( data,siftSize,poolSize,trainFolder,validFolder )
%writeFiles write out the training and test file

num_des = siftSize/poolSize;

trainFile = fopen('../data/Train/fVectors.txt','wt');
%validFile = fopen('../data/Validation/fVectors.txt','wt');
validFile = fopen('../data/Test/fVectors.txt','wt');

trainList = dir(trainFolder);
validList = dir(validFolder);

numTrain = size(trainList,1)-2;
numValid = size(validList,1)-2;

trainData = data(:,1:num_des*numTrain);
validData = data(:,num_des*numTrain+1:end);

assert(size(validData,2)/num_des==numValid,'Wrong data dimensions');

for i=3:size(trainList,1),
    dStart = (i-3)*num_des+1;
    dEnd = dStart + num_des - 1;
    curData = trainData(:,[dStart:dEnd]);
    curData = curData(:);  % get all data in one row
    fprintf(trainFile,'%s ',trainList(i).name);    
    fprintf(trainFile,'%s ',curData);
    fprintf(trainFile,'\n');
end

fclose(trainFile);

for i=3:size(validList,1),
    dStart = (i-3)*num_des + 1;
    dEnd = dStart + num_des - 1;
    curData = validData(:,dStart:dEnd);
    curData = curData(:);  % get all data in one row
    fprintf(validFile,'%s ',validList(i).name);    
    fprintf(validFile,'%s ',curData);
    fprintf(validFile,'\n');    
end

fclose(validFile);


end

