# -*- coding: utf-8 -*

#批量创建笔记文件夹，一文件夹包含image/, README.md

import os

nums = 40

for i in range(nums):
    foldername = "C%s"%(("0" if i + 1 < 10 else "") + str(i + 1))
    print "[%s.](%s)\n"%(str(i+1), foldername)
    if not os.path.exists(foldername):
        print "Creating " + foldername
        os.mkdir(foldername)
        os.makedirs("%s/%s"%(foldername,"image"))
        open("%s/%s"%(foldername,"README.md"), 'w').close()

