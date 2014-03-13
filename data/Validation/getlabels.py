# Generate labels file for validation set
import os

trueLabels = open('trueLabels.txt','w')
images = os.listdir('Images')
#images.remove(images[images.index('.DS_Store')])
for img in images:
    #imgSplit = img.split('_')
    fileName = img
    label = '1'
    trueLabels.write(fileName+' '+label+'\n')
print 'Done.'

