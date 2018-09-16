#encoding=utf-8

#删除Java文件类声明注释

import os,re

def list_all_files(rootdir):
    _files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
           path = os.path.join(rootdir,list[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path) and path.endswith('.java'):
              _files.append(path)
    return _files

def deleteComment(filename):
    print "Handle " + filename
    content = open(filename).read()
    new_content = re.sub(r'/\*\*.*\*/', "", content, count=1, flags=re.S)
    open(filename, 'w').write(new_content)
    print("Done\n")

def main():
    filepaths = list_all_files(".")

    for path in filepaths:
        #print path
        deleteComment(path)

if __name__ == "__main__":
    main()
