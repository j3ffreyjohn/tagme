function [ c ] = SIFT(folder)
%SIFT Compute SIFT for all images in a folder

imgList = dir(folder);

% Sift Parameters
binSize = 8;
magnif = 3;
stepSize = 4;

c = containers.Map;

tic
% Go through every image
display('Computing SIFT . . .');
for i=3:size(imgList,1),
    I = imread(sprintf('%s/%s',folder,imgList(i).name));    % read image
    I = single(vl_imdown(rgb2gray(I)));    % convert to gray scale
    Is = vl_imsmooth(I, sqrt((binSize/magnif)^2 - .25)) ;
    [~,d] = vl_dsift(Is, 'size', binSize, 'step',stepSize);    % compute SIFT features
    c(imgList(i).name) = d;    % add descriptors to dictinary
end
toc


end

