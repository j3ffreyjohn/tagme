# Fit RandomForest Classifer fo tagMe

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from collections import defaultdict

def getData(trainFile,trainLabelsFile,validationFile,validationLabelsFile):
	# Load all data into dictionary
	trainData = open(trainFile,'r')
	trainLabels = open(trainLabelsFile, 'r')
	validationData = open(validationFile,'r')
	validationLabels = open(validationLabelsFile,'r')

	dataD = defaultdict()
	for el in trainData:
		vals = el.split(' ')
		dataD[vals[0]] = [vals[0],vals[1:-1],1]
	for el in trainLabels:
		vals = el.split(' ')
		current = dataD[vals[0]]
		current.append(vals[1][0])
		dataD[vals[0]] = current
	for el in validationData:
		vals = el.split(' ')
		dataD[vals[0]] = [vals[0],vals[1:-1],0]
	for el in validationLabels:
		vals = el.split(' ')
		current = dataD[vals[0]]
		current.append(vals[1][0])
		dataD[vals[0]] = current

	data = dataD.values()
	dataNP = np.concatenate([[b[1]] for b in data])
	df = pd.DataFrame(dataNP)
	df['is_train'] = [b[2] for b in data]
	df['class'] = [b[3] for b in data]
	df.head()

	trainData.close()
	trainLabels.close()
	validationData.close()
	validationLabels.close()
	return df
