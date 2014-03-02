# Data Utility Class

import pandas as pd
import numpy as np
from collections import defaultdict

# Return class name for label
def getClass(label):
	dict = {'1': 'Buildings', '2': 'Cars', '3': 'Faces', '4': 'Flowers', '5':'Shoes'}
	return dict[label]

# Return label for class name
def getLabel(className):
	dict = {'Buildings':'1','Cars':'2','Faces':'3','Flowers':'4','Shoes':'5'}
	return dict[className]

# Parse all data and return as pandas data frames
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
	target = np.array([int(b[3])-1 for b in data])
	target_names = np.array(['Buildings','Cars','Faces','Flowers','Shoes'])
	df['class'] = pd.Categorical(target,target_names)
	df.head()

	trainData.close()
	trainLabels.close()
	validationData.close()
	validationLabels.close()
	return [df,data,target_names]
