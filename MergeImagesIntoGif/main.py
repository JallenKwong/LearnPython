# -*- coding: UTF-8 -*-

# 图片集弄成gif文件
# 作者：白居布衣

import imageio
import os

folderName = "image\\"

if os.path.exists(folderName) is False:
    print "image folder is not existed."
    exit()

imagenamelist = os.listdir(folderName)

if len(imagenamelist) <= 1:
    print "There is not enough images in image folder. At least 2 images"
    exit()

frames = []
duration = 0.15

for imagename in imagenamelist:
    
    frames.append(imageio.imread(folderName + imagename))
# 保存为 gif 
imageio.mimsave("result.gif", frames, 'GIF', duration = duration)

print "Done"
