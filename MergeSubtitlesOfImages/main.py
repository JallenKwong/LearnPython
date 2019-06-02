# -*- coding: UTF-8 -*-

# 视频截图字幕缩叠
# 作者：白居布衣

from PIL import Image
import os

folderName = "image\\"

if os.path.exists(folderName) is False:
    print "image folder is not existed."
    exit()

imagenamelist = os.listdir(folderName)

if len(imagenamelist) <= 1:
    print "There is not enough images in image folder. At least 2 images"
    exit()

firstImage = Image.open(folderName + imagenamelist[0])
width, height = firstImage.size # 

# 底部字幕的高度 ，所以图片要截取的位置是(0, 400 - 55 + 1,720 , 400)
cropHeight = 100

imagelist = []
imagelist.append(firstImage)
#print firstImage.size

#截取各图
for imagename in imagenamelist:
    if imagenamelist.index(imagename) == 0:
        continue
    im = Image.open(folderName + imagename)
    imagelist.append(im.crop((0, height - cropHeight, width, height)))
        
#开始合并

#先计算高度
newImageHeight = height + (len(imagenamelist) - 1) * cropHeight
newImage = Image.new('RGB', (width, newImageHeight))
count = 0

for im in imagelist:    
    if imagelist.index(im) == 0:
        newImage.paste(im.copy(),(0, 0))
    else:
        newImage.paste(im.copy(),(0, count))
    count = count + im.size[1]

newImage.save('result.jpg')

print 'Done!'
