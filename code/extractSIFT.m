function [] = extractSIFT( imgDir, outFile )
%EXTRACTSIFT Extract SIFT features from images in imgDir, and write out
%features to outFile. 


cd('../lib/vlfeat-0.9.18/toolbox/');       % Add VLFEAT Lib
vl_setup
cd('../../sparseFiltering');  % Add sparse filtering code base
startup
cd('../../code');     

imgList = dir(imgDir);  % get list of images
numImages = size(imgList,1);    % get num images

% Sift Parameters
binSize = 20;
magnif = 3;
stepSize = 2;

c = containers.Map;     % SIFT Dictionary
tic
% Go through every training image
display('Computing SIFT . . .');
for i=3:numImages,
    I = imread(sprintf('%s/%s',imgDir,imgList(i).name));    % read image
    I = single(vl_imdown(rgb2gray(I)));    % convert to gray scale
    Is = vl_imsmooth(I, sqrt((binSize/magnif)^2 - .25)) ;
    [~,d] = vl_dsift(Is, 'size', binSize, 'step',stepSize);    % compute SIFT features
    c(imgList(i).name) = d;    % add descriptors to dictinary
end
toc

K = values(c);

% pass this through the sparse Filtering code to learn dictionary bases
data = double([K{1:size(K,2)}]);    % 128 X patches

%% Remove DC
data = bsxfun(@minus, data, mean(data));

%% Train Layer 1
L1_size = 128;  % Increase this for more features
L1 = sparseFiltering(L1_size, data);

% Show Layer 1 Bases
displayData(L1);
pause;

%% Feed-forward Layer 1
data1 = feedForwardSF(L1, data);
data1 = bsxfun(@minus, data1, mean(data1));

%% Train Layer 2
%L2_size = 128;
%L2 = sparseFiltering(L2_size, data1);

%% Visualize Layer 2
%figure;

% Number of L2 units to visualize
num_viz = 10; 

% Visualize different units
offset = 1;

% Plot the units
for i = 1:num_viz
    j = offset+i;
    
    % Find the sign of the unit with the maximum absolute values
    [a, b] = max(abs(L2(j, :)));
    sgn    = sign(L2(j, b)); 
    
    % Sort and plot units in those direction
    [a, b] = sort(sgn*(L2(j, :)), 'descend');
    
    % Plot
    subplot(1, num_viz, i, 'align'); 
    displayData(L1(b(1:10), :), [] , 1);
end

%display('Running K-Means . . .');
%numClusters = 200;
%[centers,assignments] = vl_ikmeans(uint8([K{1:size(K,2)}]),numClusters,'method','elkan');    % Run k-means clustering 

% Assign descriptor centers
%features = zeros(numImages-2,numClusters);      % SIFT histogram bins
%for i=3:numImages,
    
    
    
%end

end

