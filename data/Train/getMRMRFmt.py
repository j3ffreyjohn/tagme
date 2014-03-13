
f = open('fVectors.txt','r')
l = open('labels.txt','r') 
o = open('d.csv','w')

labels = {}

# Get labels
for el in l:
	elSplit = el.split(' ')
	labels[elSplit[0]] = elSplit[1]

numFeatures = 9984
o.write('class')
for i in range(1,numFeatures+1):
	fName = ',f'+str(i)
	o.write(fName)
o.write('\n')

for el in f:
	elSplit = el.split(' ')
	label = labels[elSplit[0]][:-1]
	o.write(label)
	for i in range(1,numFeatures+1):
		o.write(','+str(elSplit[i]))
	o.write('\n') # last line
	
f.close()
l.close()
o.close()




