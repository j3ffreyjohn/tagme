import dataUtil as DU
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

###############
# SET THESE   #
###############
trainFile = '../data/Train/feature_vectors.txt'
trainLabelsFile = '../data/Train/labels.txt'
validationFile = '../data/Validation/feature_vectors.txt'
validationLabelsFile = '../data/Validation/trueLabels.txt'

# Obtain data frame
dataFrames = DU.getData(trainFile,trainLabelsFile,validationFile,validationLabelsFile)
df = dataFrames[0]
data = dataFrames[1]

# Obtain train and test data
train, test = df[df['is_train']==1], df[df['is_train']==0]

# Fit RF Model and obtain predictions
features = df.columns[:-2]
clf = RandomForestClassifier(n_jobs=2)
y, _ = pd.factorize(train['class'])
clf.fit(train[features],y)
preds = clf.predict(test[features]) 

# Output predictions

# Compute Classification Accuracy
