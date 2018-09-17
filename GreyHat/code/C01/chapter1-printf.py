#encoding:utf-8

#在ctype的相助，使用动态链接库的导出函数

#在cmd下运行才能输出结果

from ctypes import *

msvcrt = cdll.msvcrt

message = "Hello world!\n"

msvcrt.printf("Testing: %s", message)
