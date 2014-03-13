function [ ] = writeFiles( data,trainFolder,validFolder )
%writeFiles write out the training and test file

trainFile = fopen('../data/Train/fVectors.txt','wt');
validFile = fopen('../data/Validation/fVectors.txt','wt');

trainList = dir(trainFolder);
validList = dir(validFolder);

numTrain = size(trainList,1)-2;
numValid = size(validList,1)-2;

trainData = data(:,1:900*numTrain);
validData = data(:,900*numTrain+1:end);

assert(size(validData,2)/900==numValid,'Wrong data dimensions');

for i=3:size(trainList,1),
    dStart = (i-3)*900+1;
    dEnd = dStart + 899;
    curData = trainData(:,[dStart,dEnd]);
    curData = curData(:);  % get all data in one row
    fprintf(trainFile,'%s ',trainList(i).name);    
    fprintf(trainFile,'%s ',curData);
    fprintf(trainFile,'\n');
end

fclose(trainFile);

for i=3:size(validList,1),
    dStart = (i-3)*900 + 1;
    dEnd = dStart + 899;
    curData = validData(:,dStart:dEnd);
    curData = curData(:)';  % get all data in one row
    fprintf(validFile,'%s ',validList(i).name);    
    fprintf(validFile,'%s ',curData);
    fprintf(validFile,'\n');    
end

fclose(validFile);


end

