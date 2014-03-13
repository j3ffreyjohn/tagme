import dataUtil as DU
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn import svm

###############
# SET THESE   #
###############
#trainFile = '../data/Train/feature_vectors.txt'
trainFile = '../data/Train/fVectors.txt'
trainLabelsFile = '../data/Train/labels.txt'
#validationFile = '../data/Validation/feature_vectors.txt'
validationFile = '../data/Validation/fVectors.txt'
validationLabelsFile = '../data/Validation/trueLabels.txt'
predictionsFile_RF = '../data/RF/labels.txt'
predictionsFile_SVM = '../data/SVM/labels.txt'

# Obtain data frame
dataFrames = DU.getData(trainFile,trainLabelsFile,validationFile,validationLabelsFile)
df = dataFrames[0]
data = dataFrames[1]
target_names = dataFrames[2]
trainData = [el for el in data if el[2]==1]
testData = [el for el in data if el[2]==0]

# Obtain train and test data
train, test = df[df['is_train']==1], df[df['is_train']==0]
testFiles = list(test['fileName'])

print 'Fitting RF model . . .'
# Fit RF Model and obtain predictions
features = df.columns[:-3]
clf = RandomForestClassifier(n_estimators=100,n_jobs=2)
y, _ = pd.factorize(train['class'])
clf.fit(train[features],y)
preds = target_names[clf.predict(test[features])]
pd.crosstab(test['class'], preds, rownames=['actual'], colnames=['preds'])

# Output predictions
predOut = open(predictionsFile_RF,'w')
for i in range(len(testFiles)):
	predOut.write(testFiles[i]+' '+DU.getLabel(preds[i])+'\n')
predOut.close()

# Compute Classification Accuracy
accuracy = DU.getAcc(predictionsFile_RF,validationLabelsFile)
print 'Classification Accuracy (Random Forest) : ', accuracy

print 'Training SVM . . .'
# Train multi-class SVM on the training data
X_train = []
Y_train= []
X_test = []
for el in trainData:
	X_train.append([float(fval) for fval in el[1]])
	Y_train.append(int(el[3]))
for el in testData:
	X_test.append([float(fval) for fval in el[1]])
clf = svm.SVC(kernel='linear')
clf.fit(X_train,Y_train)
preds = clf.predict(X_test)

# Output Predictions
predOut = open(predictionsFile_SVM,'w')
for i in range(len(testData)):
	predOut.write(testData[i][0]+' '+str(preds[i])+'\n')
predOut.close()

# Compute Classification Accuracy
accuracy = DU.getAcc(predictionsFile_SVM,validationLabelsFile)
print 'Classification Accuracy (SVM) : ', accuracy
