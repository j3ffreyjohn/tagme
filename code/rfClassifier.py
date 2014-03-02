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
predictionsFile = '../data/preds.txt'

# Obtain data frame
dataFrames = DU.getData(trainFile,trainLabelsFile,validationFile,validationLabelsFile)
df = dataFrames[0]
data = dataFrames[1]
target_names = dataFrames[2]
trainData = [el for el in data if el[2]==1]
testData = [el for el in data if el[2]==0]

# Obtain train and test data
train, test = df[df['is_train']==1], df[df['is_train']==0]

# Fit RF Model and obtain predictions
features = df.columns[:-2]
clf = RandomForestClassifier(n_jobs=2)
y, _ = pd.factorize(train['class'])
clf.fit(train[features],y)
preds = target_names[clf.predict(test[features])]
pd.crosstab(test['class'], preds, rownames=['actual'], colnames=['preds'])

# Output predictions
predOut = open(predictionsFile,'w')
for i in range(len(test)):
	predOut.write(testData[i][0]+' '+DU.getLabel(preds[i])+'\n')
predOut.close()

# Compute Classification Accuracy
total=0
correct = 0
for i in range(len(preds)):
	if DU.getLabel(preds[i])==testData[i][3]:
		correct +=1
	total +=1

print 'Classification Accuracy : ', (correct*100.0)/total
	
