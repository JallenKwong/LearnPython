#encoding=utf-8
import os, sys
 
# 转换函数，默认 待转换前的编码为gb2312，转换后的编码为utf-8
def convert(filename, in_enc="GB2312", out_enc="utf-8"):
        print("convert " + filename)
        content = open(filename).read()
#        print('content',content)
        new_content = content.decode(in_enc,'ignore').encode(out_enc)
        open("utf8-" + filename, 'w').write(new_content)
        print("Done")

def main():
    convert("MyInterceptor.java")

if __name__ == "__main__":
    main()
