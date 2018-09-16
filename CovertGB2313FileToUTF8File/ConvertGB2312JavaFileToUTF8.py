#encoding=utf-8

import os

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

def convert(filename, in_enc="GB2312", out_enc="utf-8"):
        print("Converting " + filename)
        content = open(filename).read()
        #print('content',content)
        new_content = content.decode(in_enc,'ignore').encode(out_enc)
        open(filename, 'w').write(new_content)
        print("Done\n")

def main():
    filepaths = list_all_files(".")

    for path in filepaths:
        #print path
        convert(path)

if __name__ == "__main__":
    main()


