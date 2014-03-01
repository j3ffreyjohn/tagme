tagme
=====

Multi Class Image Classifier as part of the CSA-Microsoft TagMe competition. 
The aim is to make use of sparse filtering/sparse coding methods for unsupervised feature extraction.

Step 0: Ground Truths
=====================
Because I don't want to visually inspect perfomance on the validation set later on, I manually labelled the entire validation set for ground truth. 
(2 coffees and half an hour on a Friday afternoon - Hand Labeling 500 images). Have to mention that this made me realize that the validation data is super noisy, with images of low quality, blurred, dim, repeated, and rotated. (Note to self : scale invariant features).

Step 1: Use Given Features
==========================
The first method is make use of the best out-of-box classifier I know of, Random Forests, using the <a href="http://blog.yhathq.com/posts/random-forests-in-python.html">RandomForestClassifier</a> in sklearn. 
 
