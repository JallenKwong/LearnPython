# -*- coding: utf-8 -*

#提取格式为'UCS-2 LE'的字幕文件中的英文台词


import codecs

filename = "Friends.S06E06.eng"


textFile = codecs.open(filename + ".ass","r","utf-16-le")
resultFile = codecs.open(filename + ".txt", "w", "utf-8")


for line in textFile.readlines():

    if "4c&H000000&}" in line:
        resultFile.write(line.split("4c&H000000&}")[1])

resultFile.close()
