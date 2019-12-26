# 如何运行程序 #

## 交互提示模式下编写代码 ##

### 交互地运行代码 ###

Windows下cmd输入`python`进入交互环境

	Microsoft Windows [版本 6.1.7601]
	版权所有 (c) 2009 Microsoft Corporation。保留所有权利。
	
	C:\Users\Administrator.USER-20180302VA>python
	Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AM
	D64)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	>>> 2*100
	200
	>>> 2**1000
	10715086071862673209484250490600018105614048117055336074437503883703510511249361
	22493198378815695858127594672917553146825187145285692314043598457757469857480393
	45677748242309854210746050623711418779541821530464749835819412673987675591655439
	46077062914571196477686542167660429831652624386837205668069376L
	>>>

`exit()`退出交互环境

### 为什么使用交互提示模式 ###

在交互提示模式下不能编写大型代码，但可以体验语言和测试编写中的程序文件。

## 系统命令行和文件 ##

### Windows下 ###

	>>> import sys
	>>> sys.platform
	'win32'
	>>>

---

命令行运行python

	python a.py > result.txt

---

Windows这样运行Python脚本，无需键入`python`

	C:\Users\Administrator.USER-20180302VA\Desktop>a.py
	Hello, World
	1267650600228229401496703205376

### Unix可执行脚本 ###

有两个特殊属性

- 它们第一行是特定的。#!后紧接Python解释器的路径
- 它们往往都拥有可执行的权限。'chmod +x a,py'修改文件权限

## 点击文件图标 ##

	# Python 2.6
	raw_input()
	# Python 3
	input()

	input("Please input!")
	next_input = input()

上函数可暂停一下程序，让程序结果呈现出来，而不是一闪而过。

但对异常不行。


## 模块导入和重载 ##

每一个一扩展名py结尾的Python源代码文件都是一个模块。

其他的文件可以通过导入一个模块读取一个模块。

	# 重载模块
	import script
	import script
	# 这样做开销很大

	# py2.6
	reload(script) 
	
	# py3
	from imp import reload # reload()已不是内置
	reload(script)

### 模块的显要特性：属性 ###

	# my.py
	name='lun'

	# object.attribute
	>>> import my
	>>> print(my.name)

---

	#替代方案，这引入函数，对象很有用
	>>> from my import name
	>>> print(name)

---

	# threenames.py

	a='a'
	b='b'
	c='c'
	
	>>> from threenames import a, b, c

---

	# dir()获得变量名的列表
	>>> dir(a)
	['__builtins__', '__doc__', '__file__', '__name__', '__package__']
	>>>


## 使用exec运行模块文件 ##

	>>> exec(open('a.py').read())
	Hello, World
	1267650600228229401496703205376
	>>>

## IDLE用户界面 ##


## 其他启动选项 ##

### 嵌入式调用 ###

C语言环境内运行Python文件

	### C language code (embedding)
	
	#include <Python.h>
	...
	Py_Initialize();                                    // This is C, not Python
	PyRun_SimpleString("x = 'brave ' + 'sir robin'");   // But it runs Python code

### 冻结二进制的可执行性 ###


### 文本编辑器启动的选择 ###


### 其他 ###




## 我应该选用哪种 ##
