function [ ] = sparseSIFT()
%SPARSESIFT : 
%1. Extracts SIFT features for the Train and Validation(/Test) Set. 
%2. Learns a dictionary of code words using sparseFiltering making use of
%the minFunc toolbox.
%3. Finds the weights of the image using the code words for each image in
%the Training and Validation Set, and writes out train file and test file. 


%%%%SET THESE%%%%%%%%%%
trainFolder = '../data/Train/Images/';
%validFolder = '../data/Test/Images/';
validFolder = '../data/Validation/Images/';

%%%%Compute SIFT%%%%%%%
cTrain = SIFT(trainFolder);     % SIFT Dictionary
cValid = SIFT(validFolder);

K_all = [values(cTrain) values(cValid)];
d_all = double([K_all{1:size(K_all,2)}]);

K_train = [values(cTrain)];
d_train = double([K_train{1:size(K_train,2)}]);

%% Remove DC
data = bsxfun(@minus, d_all, mean(d_all));
dataT = bsxfun(@minus, d_train, mean(d_train));

%% Train Layer 1
L1_size = 128;  % Learn a complete representation
L1 = sparseFiltering(L1_size, dataT);   % If time permits, let the optimizer run for more iterations. 

%% Feed-forward Layer 1
data1 = feedForwardSF(L1, data);

%% Remove DC
dataT2 = bsxfun(@minus, data1, mean(data1));

%% Train Layer 2
L2_size = 64;
L2 = sparseFiltering( L2_size,dataT2);

%% Feed-forward Layer 2
data2 = feedForwardSF(L2, data);


% Write out training and test files
writeFiles(data2,trainFolder,validFolder);

end

