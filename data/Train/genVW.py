# Generate VW format training and test data

train = open('FV_train.txt','r')
test = open('FV_test.txt','r')
train_vw = open('train.vw','w')
test_vw = open('test.vw','w')
l = open('labels.txt')

labels = {}

# Get labels
for el in l:
	elSplit = el.split(' ');
	labels[elSplit[0]] = elSplit[1][:-1]

# Write out train_vw
for el in train:
	elSplit = el.split(',')
	label = labels[elSplit[0]]
	max_F = len(elSplit)-1	# num features
	elSplit[max_F] = elSplit[max_F][:-1]	# clean the last feature
	train_vw.write(label+' |')  # write the label
	for i in range(1,max_F):
		train_vw.write('f'+str(i)+':'+elSplit[i]+' ')
	train_vw.write('\n')

# Write out test_vw
for el in test:
        elSplit = el.split(',')
        max_F = len(elSplit)-1  # num features
        elSplit[max_F] = elSplit[max_F][:-1]    # clean the last feature
        for i in range(1,max_F):
                test_vw.write('f'+str(i)+':'+elSplit[i]+' ')
        test_vw.write('\n')

train.close()
test.close()
train_vw.close()
test_vw.close()
l.close()
	
	




