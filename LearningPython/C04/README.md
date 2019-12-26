# 介绍Python对象类型 #

Python程序可以分解模块、语句、表达式以及对象：

1. 程序由模块构成；
2. 模块包含语句；
3. 语句包含表达式
4. 表达式建立并处理对象

## 为什么使用内置类型 ##

- 让程序更容易编写
- 它是扩展的组件
- 比定制的数据结构更有效率
- 语言标准的一部分

### Python核心数据类型 ###

对象类型|例子 常量/创建
---|---
数字|1234
字符串|'a'
列表|['a']
字典|{'a':1,'b':2}
元组|(1,2,3)
文件|open("myfile.txt",'w')
集合|set('abc'),{'a','b','c'}
其他类型|类型、None、布尔型
编程单元类型|函数、模块、类<br>（由def/class/import/lambda这样语句和表达式创建）
与实现相关类型|编译的代码堆栈跟踪

Python中没有类型声明，运行的表达式的语法决定了创建和使用的对象的类型。一旦创建一个对象，它就和操作集合绑定了。

Python是**动态类型**（它自动地跟踪你的类型而不是要求声明代码），但是它也是**强类型语言**（你只能对一个对象进行适合该类型的有效操作）

## 数字 ##

	# 基本数学运算
	>>> 123 + 222                     # Integer addition
	345
	>>> 1.5 * 4                       # Floating-point multiplication
	6.0
	>>> 2 ** 100                      # 2 to the power 100
	1267650600228229401496703205376
	
	
	
	>>> len(str(2 ** 1000000))        # How many digits in a really BIG number?
	301030
	
	
	# 浮点数
	>>> 3.1415 * 2                    # repr: as code
	6.2830000000000004
	>>> print(3.1415 * 2)             # str: user-friendly
	6.283
	
	
	# 数学模块
	>>> import math
	>>> math.pi
	3.1415926535897931
	>>> math.sqrt(85)
	9.2195444572928871
	
	
	# 随机模块
	>>> import random
	>>> random.random()
	0.59268735266273953
	>>> random.choice([1, 2, 3, 4])
	1

## 字符串 ##

### 序列的操作 ###


	>>> S = 'Spam'
	>>> len(S)               # Length
	4
	>>> S[0]                 # The first item in S, indexing by zero-based position
	'S'
	>>> S[1]                 # The second item from the left
	'p'
	
---
	
	>>> S[-1]                # The last item from the end in S
	'm'
	>>> S[-2]                # The second to last item from the end
	'a'
	
---
	
	>>> S[-1]                # The last item in S
	'm'
	>>> S[len(S)-1]          # Negative indexing, the hard way
	'm'
	
---

	# 分片
	>>> S                    # A 4-character string
	'Spam'
	>>> S[1:3]               # Slice of S from offsets 1 through 2 (not 3)
	'pa'
	
---
	
	>>> S[1:]                # Everything past the first (1:len(S))
	'pam'
	>>> S                    # S itself hasn't changed
	'Spam'
	>>> S[0:3]               # Everything but the last
	'Spa'
	>>> S[:3]                # Same as S[0:3]
	'Spa'
	>>> S[:-1]               # Everything but the last again, but simpler (0:-1)
	'Spa'
	>>> S[:]                 # All of S as a top-level copy (0:len(S))
	'Spam'
	
	
	
	>>> S
	'Spam'
	>>> S + 'xyz'            # Concatenation # 拼接
	'Spamxyz'
	>>> S                    # S is unchanged
	'Spam'
	>>> S * 8                # Repetition
	'SpamSpamSpamSpamSpamSpamSpamSpam'
	


### 不可变性 ###

	>>> S
	'Spam'
	>>> S[0] = 'z'           # Immutable objects cannot be changed
	...error text omitted...
	TypeError: 'str' object does not support item assignment
	
	>>> S = 'z' + S[1:]      # But we can run expressions to make new objects
	>>> S
	'zpam'

### 类型特定的方法 ###

	>>> S.find('pa')            # Find the offset of a substring
	1
	>>> S
	'Spam'
	>>> S.replace('pa', 'XYZ')  # Replace occurrences of a substring with another
	'SXYZm'
	>>> S
	'Spam'
	
	
	
	>>> line = 'aaa,bbb,ccccc,dd'
	>>> line.split(',')            # Split on a delimiter into a list of substrings
	['aaa', 'bbb', 'ccccc', 'dd']
	
	>>> S = 'spam'
	>>> S.upper()                  # Upper- and lowercase conversions
	'SPAM'
	>>> S.isalpha()                # Content tests: isalpha, isdigit, etc.
	True
	
	>>> line = 'aaa,bbb,ccccc,dd\n'
	>>> line = line.rstrip()       # Remove whitespace characters on the right side
	>>> line
	'aaa,bbb,ccccc,dd'
	
	
	# 格式化方法
	>>> '%s, eggs, and %s' % ('spam', 'SPAM!')        # Formatting expression (all)
	'spam, eggs, and SPAM!'
	
	>>> '{0}, eggs, and {1}'.format('spam', 'SPAM!')  # Formatting method (2.6, 3.0)
	'spam, eggs, and SPAM!'


### 寻找帮助 ###


	>>> dir(S)
	['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__
	format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__get
	slice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mo
	d__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
	 '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook
	__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center',
	 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index
	', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper',
	'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', '
	rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', '
	strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

---

	>>> help(S.replace)
	Help on built-in function replace:
	
	replace(...)
	    S.replace(old, new[, count]) -> string
	
	    Return a copy of string S with all occurrences of substring
	    old replaced by new.  If the optional argument count is
	    given, only the first count occurrences are replaced.
	
	>>>

### 编写字符串的其他方法 ###

	>>> S = 'A\nB\tC'            # \n is end-of-line, \t is tab
	>>> len(S)                   # Each stands for just one character
	5
	>>> ord('\n')                # \n is a byte with the binary value 10 in ASCII
	10
	>>> S = 'A\0B\0C'            # \0, a binary zero byte, does not terminate string
	>>> len(S)
	5

---
	# 多行字符串
	>>> msg = """ aaaaaaaaaaaaa
	bbb'''bbbbbbbbbb""bbbbbbb'bbbb
	cccccccccccccc"""
	>>> msg
	'\naaaaaaaaaaaaa\nbbb\'\'\'bbbbbbbbbb""bbbbbbb\'bbbb\ncccccccccccccc'

### 模式匹配 ###

	>>> import re
	>>> match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
	>>> match.group(1)
	'Python '
	
	>>> match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
	>>> match.groups()
	('usr', 'home', 'lumberjack')


## 列表 ##

### 序列操作 ###

	# 可以任意类型
	>>> L = [123, 'spam', 1.23]       # A list of three different-type objects
	>>> len(L)                        # Number of items in the list
	3
	
	>>> L[0]                          # Indexing by position
	123
	>>> L[:-1]                        # Slicing a list returns a new list
	[123, 'spam']
	>>> L + [4, 5, 6]                 # Concatenation makes a new list too
	[123, 'spam', 1.23, 4, 5, 6]
	>>> L                             # We're not changing the original list
	[123, 'spam', 1.23]

### 类型特定的操作 ###

	>>> L.append('NI')                # Growing: add object at end of list
	>>> L
	[123, 'spam', 1.23, 'NI']
	>>> L.pop(2)                      # Shrinking: delete an item in the middle
	1.23
	>>> L                             # "del L[2]" deletes from a list too
	[123, 'spam', 'NI']
	
---
	
	>>> M = ['bb', 'aa', 'cc']
	>>> M.sort()
	>>> M
	['aa', 'bb', 'cc']
	>>> M.reverse()
	>>> M
	['cc', 'bb', 'aa']

### 边界检查 ###

	>>> L
	[123, 'spam', 'NI']

	# 不允许引用不存在的元素
	>>> L[99]
	...error text omitted...
	IndexError: list index out of range
	
	>>> L[99] = 1
	...error text omitted...
	IndexError: list assignment index out of range

### 嵌套 ###

	>>> M = [[1, 2, 3],          # A 3 × 3 matrix, as nested lists
	         [4, 5, 6],          # Code can span lines if bracketed
	         [7, 8, 9]]
	>>> M
	[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	
	
	
	>>> M[1]                     # Get row 2
	[4, 5, 6]
	>>> M[1][2]                  # Get row 2, then get item 3 within the row
	6

### 列表解析 ###

列表解析表达式list comprehension expression

	>>> col2 = [row[1] for row in M]     # Collect the items in column 2
	>>> col2
	[2, 5, 8]
	>>> M                                # The matrix is unchanged
	[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	
---
	
	>>> [row[1] + 1 for row in M]        # Add 1 to each item in column 2
	[3, 6, 9]
	
	# 这里if起到过滤的作用
	>>> [row[1] for row in M if row[1] % 2 == 0]      # Filter out odd items
	[2, 8]
	
---
	
	>>> diag = [M[i][i] for i in [0, 1, 2]]     # Collect a diagonal from matrix
	>>> diag
	[1, 5, 9]
	>>> doubles = [c * 2 for c in 'spam']       # Repeat characters in a string
	>>> doubles
	['ss', 'pp', 'aa', 'mm']

---

	# Python生成器
	>>> G = (sum(row) for row in M)             # Create a generator of row sums
	>>> next(G)
	6
	>>> next(G)                                 # Run the iteration protocol
	15

---

	>>> list(map(sum, M))                       # Map sum over items in M
	[6, 15, 24]

---

	# 解析语法用来创建集合和字典
	>>> {sum(row) for row in M}                 # Create a set of row sums
	{24, 6, 15}
	>>> {i : sum(M[i]) for i in range(3)}       # Creates key/value table of row sums
	{0: 6, 1: 15, 2: 24}
	
	>>> [ord(x) for x in 'spaam']               # List of character ordinals
	[115, 112, 97, 97, 109]
	>>> {ord(x) for x in 'spaam'}               # Sets remove duplicates
	{112, 97, 115, 109}
	>>> {x: ord(x) for x in 'spaam'}            # Dictionary keys are unique
	{'a': 97, 'p': 112, 's': 115, 'm': 109}


## 字典 ##

### 映射操作 ###

	#相当于Java的HashMap

	>>> D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
	
	>>> D['food']                  # Fetch value of key 'food'
	'Spam'
	>>> D['quantity'] += 1         # Add 1 to 'quantity' value
	>>> D
	{'food': 'Spam', 'color': 'pink', 'quantity': 5}


	>>> D = {}
	>>> D['name'] = 'Bob'          # Create keys by assignment
	>>> D['job'] = 'dev'
	>>> D['age'] = 40
	>>> D
	{'age': 40, 'job': 'dev', 'name': 'Bob'}
	>>> print(D['name'])
	Bob

### 重返嵌套 ###

	>>> rec = {'name': {'first': 'Bob', 'last': 'Smith'},
	           'job':  ['dev', 'mgr'],
	           'age':  40.5}

	>>> rec['name']                     # 'name' is a nested dictionary
	{'last': 'Smith', 'first': 'Bob'}
	>>> rec['name']['last']             # Index the nested dictionary
	'Smith'
	>>> rec['job']                      # 'job' is a nested list
	['dev', 'mgr']
	>>> rec['job'][-1]                  # Index the nested list
	'mgr'
	>>> rec['job'].append('janitor')    # Expand Bob's job description in-place
	>>> rec
	{'age': 40.5, 'job': ['dev', 'mgr', 'janitor'], 'name': {'last': 'Smith',
	'first': 'Bob'}}

### 对键排序 ###

	>>> D = {'a': 1, 'b': 2, 'c': 3}
	>>> D
	{'a': 1, 'c': 3, 'b': 2}
	
	
	
	>>> Ks = list(D.keys())            # Unordered keys list
	>>> Ks                             # A list in 2.6, "view" in 3.0: use list()
	['a', 'c', 'b']
	>>> Ks.sort()                      # Sorted keys list
	>>> Ks
	['a', 'b', 'c']
	>>> for key in Ks:                 # Iterate though sorted keys
	        print(key, '=>', D[key])   # <== press Enter twice here
	
	a => 1
	b => 2
	c => 3

---

	# 使用内置函数sorted()
	>>> D
	{'a': 1, 'c': 3, 'b': 2}
	>>> for key in sorted(D):
	        print(key, '=>', D[key])
	
	a => 1
	b => 2
	c => 3
	
---

	# while for 循环作用
	>>> for c in 'spam':
	        print(c.upper())
	
	S
	P
	A
	M
	

	>>> x = 4
	>>> while x > 0:
	        print('spam!' * x)
	        x -= 1
	
	spam!spam!spam!spam!
	spam!spam!spam!
	spam!spam!
	spam!

### 迭代和优化 ###


## 元组 ##


## 文件 ##


## 其他核心类型 ##


## 小结 ##
