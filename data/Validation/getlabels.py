# Generate labels file for validation set
import os

trueLabels = open('trueLabels.txt','w')
images = os.listdir('Images2')
images.remove(images[images.index('.DS_Store')])
for img in images:
    imgSplit = img.split('_')
    fileName = imgSplit[0]+'.jpg'
    label = imgSplit[1][0]
    trueLabels.write(fileName+' '+label+'\n')
print 'Done.'

