# Combine features from two files

def merge(file1,file2,outFile):
	f1 = open(file1,'r')
	f2 = open(file2,'r')
	o  = open(outFile,'w')
	f = dict()
	for el in f1:
		elSplit = el.split(' ')
		elSplit[len(elSplit)-1] = elSplit[len(elSplit)-1][:-1]	# remove last \n
		f[elSplit[0]] = elSplit[1:]
	for el in f2:
		elSplit = el.split(' ')
		elSplit[len(elSplit)-1] = elSplit[len(elSplit)-1][:-1]  # remove last \n
		f[elSplit[0]] = f[elSplit[0]] + elSplit[1:]
	for k,v in f.iteritems():
		# k is file name and v is set of features
		o.write(k)
		for el in v:
			o.write(' '+el)
		o.write('\n')

merge('../data/Train/fVectors.txt','../data/Train/feature_vectors.txt','../data/Train/fVectorsC.txt')
merge('../data/Validation/fVectors.txt','../data/Validation/feature_vectors.txt','../data/Validation/fVectorsC.txt')
