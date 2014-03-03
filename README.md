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
The first method is make use of the best out-of-box classifier I know of, Random Forests, using the <a href="http://blog.yhathq.com/posts/random-forests-in-python.html">RandomForestClassifier</a> in sklearn. With the provided features, with 10 or 100 trees, the classification accuracy hovered around 20% for 5-classes. Clearly, we need more discriminative features here. The confusion matrix obtained:

actual/preds | Buildings | Cars | Faces | Flowers | Shoes
------------- |---|---|---|---|---
Buildings | **23** | 9 | 41 | 12 | 15
Cars | 75  |**9** | 14 | 0 | 2
Faces | 2 | 15 | **3** | 74 | 6
Flowers | 7 | 70 | 7 | **7** | 9
Shoes | 2 | 9 | 3 | 19 | **67**

``Update`` : The contest team reports that that obtained 70% accuracy with these features using a multi-class SVM. Either there's a bug in my RF code or SVM is doing way better. Will need to implement muti class SVM also for sanity check.

``Update`` : Multi Class SVM gives 64% accuracy on the noisy validation set.  

Step 2 : Feature Extraction
---------------------------
Most sparse coding/sparse filtering algorithms work on image patches, so we first obtain image patches from natural images. As a first step, we extract Scale Invariant Feature Transform (SIFT) and Speeded-Up Robust Features(SIRF) from the images using the opencv python interface and write the descriptors to a file to see how that improves the performance of the current vanilla RF classifier. 
