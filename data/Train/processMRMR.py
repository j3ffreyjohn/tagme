# Code to Parse output of MRMR and create train and test variables with those subsets

score_threshold = 0

maxF = 0
feat = []
mrmr = open('mr.out','r')		# Expects no header
k=1
for l in mrmr:
	mSplit = l.split(' ');
	score = float(mSplit[6][:-1])
	if score < score_threshold:
		maxF = k
		break
	feat.append(int(mSplit[2]));
	k += 1
if maxF==0:
	maxF = 500

# read train and test files
train = open('fVectors.txt','r')
test = open('../Validation/fVectors.txt','r')
train_trim = open('FV_train.txt','w')
test_trim = open('FV_test.txt','w')

# Write out train
for l in train:
	lSplit = l.split(' ');
	max_len = len(lSplit)-1;
	lSplit[max_len] = lSplit[max_len][:-1]
	train_trim.write(lSplit[0])  # write file name
	for i in range(1,max_len+1):
		if i in feat:
			train_trim.write(','+lSplit[i])
	train_trim.write('\n')

# Write out test
for l in test:
        lSplit = l.split(' ');
        max_len = len(lSplit)-1;
        lSplit[max_len] = lSplit[max_len][:-1]
        test_trim.write(lSplit[0])  # write file name
        for i in range(1,max_len+1):
                if i in feat:
                        test_trim.write(','+lSplit[i])
        test_trim.write('\n')

mrmr.close()
train.close()
test.close()
train_trim.close()
test_trim.close()
	
	
	
