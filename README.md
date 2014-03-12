tagme
=====

Multi Class Image Classifier as part of the CSA-Microsoft TagMe competition. 
The aim is to make use of sparse filtering/sparse coding methods for unsupervised feature extraction.

Step 0: Ground Truths
---------------------
Because I don't want to visually inspect perfomance on the validation set later on, I manually labelled the entire validation set for ground truth. 
(2 coffees and half an hour on a Friday afternoon - Hand Labeling 500 images). Have to mention that this made me realize that the validation data is super noisy, with images of low quality, blurred, dim, repeated, and rotated. (Note to self : scale invariant features).

Step 1: Use Given Features
--------------------------
I wanted to use a Random Forest, but it performed very poorly - at least with the provided features. I put the available features through a multi class SVM ( validation set of 1000 images) bumping up the accuracy to 60%. A note about the features: For each image, the features are just the eigen values of the matrix when considering the image in gray scale.


Step 2 : Feature Extraction
---------------------------
Most sparse coding/sparse filtering algorithms work on image patches, so we first obtain image patches from natural images. As a first step, we extract Scale Invariant Feature Transform (SIFT) and Speeded-Up Robust Features(SIRF) from the images using the opencv python interface and write the descriptors to a file to see how that improves the performance of the current vanilla RF classifier. 
