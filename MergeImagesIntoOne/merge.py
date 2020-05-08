from PIL import Image
import os

folderName = ".\\"

imagenamelist = [img for img in os.listdir(folderName) if img.endswith('png')]

print imagenamelist

firstImage = Image.open(folderName + imagenamelist[0])
width, height = firstImage.size

imagelist = []
for imagename in imagenamelist:
    im = Image.open(folderName + imagename)
    imagelist.append(im)

#先计算高度
newImageHeight = len(imagenamelist) * height
newImage = Image.new('RGB', (width, newImageHeight))
count = 0

for im in imagelist:    
    newImage.paste(im.copy(),(0, count))
    count = count + im.size[1]

newImage.save('result\\result.png')

print 'Done!'
