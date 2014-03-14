function [ ] = sparseSIFT()
%SPARSESIFT : 
%1. Extracts SIFT features for the Train and Validation(/Test) Set. 
%2. Learns a dictionary of code words using sparseFiltering making use of
%the minFunc toolbox.
%3. Finds the weights of the image using the code words for each image in
%the Training and Validation Set, and writes out train file and test file. 


%%%%SET THESE%%%%%%%%%%
trainFolder = '../data/Train/Images/';
testFolder = '../data/Test/Images/';
validFolder = '../data/Validation/Images/';
poolSize = 8;
siftSize = 576;

%%%%Compute SIFT%%%%%%%
cTrain = SIFT(trainFolder);     % SIFT Dictionary
cValid = SIFT(validFolder);
cTest = SIFT(testFolder);

%K_t_v = [values(cTrain) values(cValid)];
%d_t_v = double([K_t_v{1:size(K_t_v,2)}]);

K_t_t = [values(cTrain) values(cTest)];
d_t_t = double([K_t_t{1:size(K_t_t,2)}]);

K_train = [values(cTrain)];
d_train = double([K_train{1:size(K_train,2)}]);

%% Remove DC
data = bsxfun(@minus, d_t_v, mean(d_t_v));
data_all = bsxfun(@minus, d_t_t, mean(d_t_t));
dataT = bsxfun(@minus, d_train, mean(d_train));

%% Train Layer 1
L1_size = 128;  % Learn overcomplete representation
L1 = sparseFiltering(L1_size, dataT);   % If time permits, let the optimizer run for more iterations. 

%% Feed-forward Layer 1
data1 = feedForwardSF(L1, data);
data11 = feedForwardSF(L1,data_all);

%% Remove DC
%dataT2 = bsxfun(@minus, data1, mean(data1));

%% Train Layer 2
%L2_size = 64;
%L2 = sparseFiltering( L2_size,dataT2);

%% Feed-forward Layer 2
%data2 = feedForwardSF(L2, data);


%% Naive max-pooling of features within a neighborhood
dataP = maxPool(data1,poolSize,siftSize);
dataP_all = maxPool(data11,poolSize,siftSize);

% Write out training and test files
writeFiles(dataP,siftSize,poolSize,trainFolder,validFolder);

end

