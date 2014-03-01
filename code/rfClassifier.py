import dataUtil as DU

trainFile = '../data/Train/feature_vectors.txt'
trainLabelsFile = '../data/Train/labels.txt'
validationFile = '../data/Validation/feature_vectors.txt'
validationLabelsFile = '../data/Validation/trueLabels.txt'

df = DU.getData(trainFile,trainLabelsFile,validationFile,validationLabelsFile)
