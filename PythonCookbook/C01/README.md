# 数据结构和算法 #

## 将序列分解为单独的变量 ##

	>>> p = (4, 5)
	>>> x, y = p
	>>> x
	4
	>>> y
	5
	>>> 

---

	>>> data = ['ACME', 50, 91.1, (2012, 12, 21)]
	>>> name, shares, price, date = data
	>>> name
	'ACME'
	>>> date
	(2012, 12, 21)
	>>> 

---

	>>> name, shares, price, (year, mon, day) = data
	>>> name
	'ACME'
	>>> year
	2012
	>>> mon
	12
	>>> day
	21
	>>> 

若元素的数量不匹配，将得到一个错误提示

	>>> p = (4, 5)
	>>> x, y, z = p
	
	Traceback (most recent call last):
	  File "<pyshell#17>", line 1, in <module>
	    x, y, z = p
	ValueError: need more than 2 values to unpack
	>>>

实际上不仅仅只是元组，列表，只要对象恰好是可迭代，那么就可以执行分解操作，包括字符串、文件等。

	>>> s = 'Hello'
	>>> a, b, c, d, e = s
	>>> a
	'H'
	>>> b
	'e'
	>>> e
	'o'
	>>> 

当做分解操作时，有时想去掉不必要的值，可使用一个用不到的变量名

	>>> data = ['ACME', 50, 91.1, (2012, 12, 21)]
	>>> _, shares, price, _ = data
	>>> shares
	50
	>>> price
	91.1
	>>> 

## 从任意长度的可迭代对象中分解元素 ##

>Python2使用 *表达式 会不支持

使用 *表达式

例如，统计成绩，去掉第一名和最后一名，只对中间剩下的成绩作平均分统计

	def drop_first_last(grades):
		first, *middle, last = grades
		return avg(middle)

---

	>>> record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
	>>> name, email, *phone_numbers = user_record
	>>> name
	'Dave'
	>>> email
	'dave@example.com'
	>>> phone_numbers
	['773-555-1212', '847-555-1212']
	>>>

---

由*修饰的变量也可以位于列表的第一个位置

	*trailing_qtrs, current_qtr = sales_record
	trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
	return avg_comparison(trailing_avg, current_qtr)

---

*式的语法在迭代一个变长的元组序列时尤其有用。

	records = [
		('foo', 1, 2),
		('bar', 'hello'),
		('foo', 3, 4),
	]

	def do_foo(x, y):
		print('foo', x, y)

	def do_bar(s):
		print('bar', s)

	for tag, *args in records:
		if tag == 'foo':
			do_foo(*args)
	elif tag == 'bar':
		do_bar(*args)

在拆分时，*式语法也非常有用

	>>> line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
	>>> uname, *fields, homedir, sh = line.split(':')
	>>> uname
	'nobody'
	>>> homedir
	'/var/empty'
	>>> sh
	'/usr/bin/false'
	>>>

有时候想分解出某些值然后丢弃它们。

	>>> record = ('ACME', 50, 123.45, (12, 18, 2012))
	>>> name, *_, (*_, year) = record
	>>> name
	'ACME'
	>>> year
	2012
	>>>

在列表中

	>>> items = [1, 10, 7, 4, 5, 9]
	>>> head, *tail = items
	>>> head
	1
	>>> tail
	[10, 7, 4, 5, 9]
	>>>

---

在递归式上使用

	>>> def sum(items):
	... head, *tail = items
	... return head + sum(tail) if tail else head
	...
	>>> sum(items)
	36
	>>>

上面的例子没卵用，纯属炫技

## 保存最后N个元素 ##

下面代码对一系列文本行做简单的文本匹配操作，当发现有匹配时就输出当前的匹配行以及最后检查过的N行文本。

	from collections import deque

	def search(lines, pattern, history=5):
	previous_lines = deque(maxlen=history)
		for line in lines:
		if pattern in line:
	#TODO:查找yield的用法
			yield line, previous_lines
		previous_lines.append(line)

	# Example use on a file
	if __name__ == '__main__':
		#TODO:查找with的用法
		with open('somefile.txt') as f:
			for line, prevlines in search(f, 'python', 5):
				for pline in prevlines:
					print(pline, end='')
				print(line, end='')
				print('-'*20)

deque(maxlen=N)创建了一个固定长度的队列

	>>> q = deque(maxlen=3)
	>>> q.append(1)
	>>> q.append(2)
	>>> q.append(3)
	>>> q
	deque([1, 2, 3], maxlen=3)
	>>> q.append(4)
	>>> q
	deque([2, 3, 4], maxlen=3)
	>>> q.append(5)
	>>> q
	deque([3, 4, 5], maxlen=3)

若不指定队列大小，也就得到无界限队列

	>>> q = deque()
	>>> q.append(1)
	>>> q.append(2)
	>>> q.append(3)
	>>> q
	deque([1, 2, 3])
	>>> q.appendleft(4)
	>>> q
	deque([4, 1, 2, 3])
	>>> q.pop()
	3
	>>> q
	deque([4, 1, 2])
	>>> q.popleft()
	4

从队列两端添加或弹出元素的复杂度都是O(1)。这和列表不同，当从列表的头部插入或移除元素时，列表的复杂度为O(N)。

## 找到最大或最小的N个元素 ##

	import heapq
	nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
	print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
	print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

在更复杂的数据结构操作

	portfolio = [
		{'name': 'IBM', 'shares': 100, 'price': 91.1},
		{'name': 'AAPL', 'shares': 50, 'price': 543.22},
		{'name': 'FB', 'shares': 200, 'price': 21.09},
		{'name': 'HPQ', 'shares': 35, 'price': 31.75},
		{'name': 'YHOO', 'shares': 45, 'price': 16.35},
		{'name': 'ACME', 'shares': 75, 'price': 115.65}
	]

	#TODO:查lambda的用法
	cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
	expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

列表堆化，底层使用堆的数据结构

	>>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
	>>> import heapq
	>>> heap = list(nums)
	>>> heapq.heapify(heap)
	>>> heap
	[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
	>>>

	>>> heapq.heappop(heap)
	-4
	>>> heapq.heappop(heap)
	1
	>>> heapq.heappop(heap)
	2

## 实现优先级队列 ##

[MyPriorityQueue.py](MyPriorityQueue.py)

包装heapq来实现一个简单优先级队列

	import heapq
	
	class PriorityQueue:
	
		def __init__(self):
			self._queue = []
			self._index = 0
		
		def push(self, item, priority):
			heapq.heappush(self._queue, (-priority, self._index, item))
			self._index += 1
		
		def pop(self):
			return heapq.heappop(self._queue)[-1]

使用例子

	class Item:
		def __init__(self, name):
			self.name = name
		def __repr__(self):
			return 'Item({!r})'.format(self.name)

	q = PriorityQueue()
	q.push(Item('foo'), 1)
	q.push(Item('bar'), 5)
	q.push(Item('spam'), 4)
	q.push(Item('grok'), 1)

---

	>>> q.pop()
	Item('bar')
	>>> q.pop()
	Item('spam')
	>>> q.pop()
	Item('foo')
	>>> q.pop()
	Item('grok')
	>>> 

第一次pop()操作返回的元素具有最高的优先级。

两个优先级相同的元素返回的顺序同它们插入到队列时的顺序相同。

---

其实Item实例是没法进行次序比较

	>>> a = Item('foo')
	>>> b = Item('bar')
	>>> a < b # Python2得 False，未抛异常
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: unorderable types: Item() < Item()
	>>>

使用元组可以行比较，除了相等情况

	>>> a = (1, Item('foo'))
	>>> b = (5, Item('bar'))
	>>> a < b # Python2得 True
	True
	>>> c = (1, Item('grok'))
	>>> a < c # Python2得 False，未抛异常
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: unorderable types: Item() < Item()
	>>>

通过引入额外的索引值，避免上面的情况出现

	>>> a = (1, 0, Item('foo'))
	>>> b = (5, 1, Item('bar'))
	>>> c = (1, 2, Item('grok'))
	>>> a < b
	True
	>>> a < c
	>True
	>>>

## 在字典中将键映射到多个值上 ##

	d = {
	'a' : [1, 2, 3],#列表
		'b' : [4, 5]
	}

	e = {
		'a' : {1, 2, 3},#集合，会消除重复元素
		'b' : {4, 5}
	}

---

	from collections import defaultdict

	d = defaultdict(list)
	d['a'].append(1)
	d['a'].append(2)
	d['b'].append(4)

	...
	d = defaultdict(set)
	d['a'].add(1)
	d['a'].add(2)
	d['b'].add(4)
	...

---

普通的字典则用`setdefault()`方法来取代。

	d = {} # A regular dictionary
	d.setdefault('a', []).append(1)
	d.setdefault('a', []).append(2)
	d.setdefault('b', []).append(4)
	...

---

initialization of the first value can be messy if you try to do it yourself.

	d = {}
	for key, value in pairs:
		if key not in d:
			d[key] = []
			d[key].append(value)

---

Using a `defaultdict()` simply leads to much cleaner code:

	d = defaultdict(list)
		for key, value in pairs:
			d[key].append(value)

## 让字典保持有序 ##

	from collections import OrderedDict

	d = OrderedDict()
	d['foo'] = 1
	d['bar'] = 2
	d['spam'] = 3
	d['grok'] = 4

	# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
	for key in d:
		print(key, d[key])

OrderedDict转换成JSON格式

	>>> import json
	>>> json.dumps(d)
	'{"foo": 1, "bar": 2, "spam": 3, "grok": 4}'
	>>>

OrderedDict内部维护了一个双向链表，注意性能上的问题。

## 与字典有关的计算问题 ##

比如求最小值，最大值，排序

	prices = {
		'ACME': 45.23,
		'AAPL': 612.78,
		'IBM': 205.55,
		'HPQ': 37.20,
		'FB': 10.75
	}

利用`zip()`把字典的键和值反转过来。

	min_price = min(zip(prices.values(), prices.keys()))
	# min_price is (10.75, 'FB')

	max_price = max(zip(prices.values(), prices.keys()))
	# max_price is (612.78, 'AAPL')

	prices_sorted = sorted(zip(prices.values(), prices.keys()))
	# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
	# (45.23, 'ACME'), (205.55, 'IBM'),
	# (612.78, 'AAPL')]

注意，`zip()`创建了一个迭代器，它的内容**只能被消费一次**。

	prices_and_names = zip(prices.values(), prices.keys())
	print(min(prices_and_names)) # OK
	print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

---

使用字典的普通方法进行数据操作。它们只会处理键，而不是值

	min(prices) # Returns 'AAPL'
	max(prices) # Returns 'IBM'

利用`values()`

	min(prices.values()) # Returns 10.75
	max(prices.values()) # Returns 612.78

但是我们还是要知道相关联的键。

	min(prices, key=lambda k: prices[k]) # Returns 'FB'
	max(prices, key=lambda k: prices[k]) # Returns 'AAPL'

要知道最小值，还要额外执行一次查找：

	min_value = prices[min(prices, key=lambda k: prices[k])]

看来使用`zip()`来解决这问题

注意，计算min()和max()时，如果碰巧value的值相同，则将返回拥有最小或最大key值的那个条目。

	>>> prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
	>>> min(zip(prices.values(), prices.keys()))
	(45.23, 'AAA')
	>>> max(zip(prices.values(), prices.keys()))
	(45.23, 'ZZZ')
	>>>

## 在两个字典中寻找相同点 ##

让字典进行集合操作。

>PS. Python2不能使用

	a = {
		'x' : 1,
		'y' : 2,
		'z' : 3
	}

	b = {
		'w' : 10,
		'x' : 11,
		'y' : 2
	}

	# Python2不能使用

	# Find keys in common
	a.keys() & b.keys() # { 'x', 'y' }
	# Find keys in a that are not in b
	a.keys() - b.keys() # { 'z' }
	# Find (key,value) pairs in common
	a.items() & b.items() # { ('y', 2) }

假设想创建一个新的字典，其中去掉某些键。

使用**字典推导式**来创建新字典。

	# Make a new dictionary with certain keys removed
	c = {key:a[key] for key in a.keys() - {'z', 'w'}}
	# c is {'x': 1, 'y': 2}

## 从序列中移除重复项且保持元素间顺序不变 ##

如果序列中的值是可哈希（hashable），那么这个问题可通过使用集合和生成器来解决

	def dedupe(items):
		seen = set()
		for item in items:
			if item not in seen:
				yield item
				seen.add(item)

使用该函数的例子

	>>> a = [1, 5, 2, 1, 9, 1, 5, 10]
	>>> list(dedupe(a))
	[1, 5, 2, 9, 10]
	>>>

---

若想在**不可哈希**的对象序列中去除重复项

	def dedupe(items, key=None):
		seen = set()
		for item in items:
			val = item if key is None else key(item)
			if val not in seen:
				yield item
				seen.add(val)

---

	>>> a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
	>>> list(dedupe(a, key=lambda d: (d['x'],d['y'])))
	[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
	>>> list(dedupe(a, key=lambda d: d['x']))
	[{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
	>>>

---

去除重复项的简单方法

	>>> a
	[1, 5, 2, 1, 9, 1, 5, 10]
	>>> set(a)
	{1, 2, 10, 5, 9}
	>>>

但这样不能保证元素间的顺序不变。

若想读一个文件，去除其中重复文本行，可以这样处理：

	with open(somefile,'r') as f:
		for line in dedupe(f):
			...

## 对切片命名 ##

	###### 0123456789012345678901234567890123456789012345678901234567890'
	record = '....................100 .......513.25 ..........'
	cost = int(record[20:32]) * float(record[40:48])


	SHARES = slice(20,32)
	PRICE = slice(40,48)
	cost = int(record[SHARES]) * float(record[PRICE])

---

`slice()`创建一个切片对象

	>>> items = [0, 1, 2, 3, 4, 5, 6]
	>>> a = slice(2, 4)
	>>> items[2:4]
	[2, 3]
	>>> items[a]
	[2, 3]
	>>> items[a] = [10,11]
	>>> items
	[0, 1, 10, 11, 4, 5, 6]
	>>> del items[a]
	>>> items
	[0, 1, 4, 5, 6]

---

	>>> a = slice(10, 50, 2)
	>>> a.start
	10
	>>> a.stop
	50
	>>> a.step
	2
	>>>

---

可以通过使用indices(size)方法将切片映射到特定大小的序列上。

	>>> s = 'HelloWorld'
	>>> a.indices(len(s))
	(5, 10, 2)
	>>> for i in range(*a.indices(len(s))):
	... print(s[i])
	...
	W
	r
	d
	>>>

## 找出序列中出现次数最多的元素 ##

使用collections模块终的Counter类。

	words = [
		'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
		'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
		'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
		'my', 'eyes', "you're", 'under'
	]

	from collections import Counter
	word_counts = Counter(words)
	top_three = word_counts.most_common(3)
	print(top_three)
	# Outputs [('eyes', 8), ('the', 5), ('look', 4)]

可以给Counter对象提供任何可哈希的对象序列作为输入。在底层实现中，Counter是一个字典，在元素和它们出现的次数间做了映射。

	>>> word_counts['not']
	1
	>>> word_counts['eyes']
	8
	>>>

可以手动增加计数，只需简单地自增即可

	>>> morewords = ['why','are','you','not','looking','in','my','eyes']
	>>> for word in morewords:
	... word_counts[word] += 1
	...
	>>> word_counts['eyes']
	9
	>>>

或者

	>>> word_counts.update(morewords)
	>>>

---

Counter可以使用各种数学运算操作结合起来使用。

	>>> a = Counter(words)
	>>> b = Counter(morewords)
	>>> a
	Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2,
	"you're": 1, "don't": 1, 'under': 1, 'not': 1})
	>>> b
	Counter({'eyes': 1, 'looking': 1, 'are': 1, 'in': 1, 'not': 1, 'you': 1,
	'my': 1, 'why': 1})

	>>> # Combine counts
	>>> c = a + b
	>>> c
	Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2,
	'around': 2, "you're": 1, "don't": 1, 'in': 1, 'why': 1,
	'looking': 1, 'are': 1, 'under': 1, 'you': 1})

	>>> # Subtract counts
	>>> d = a - b
	>>> d
	Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2,
	"you're": 1, "don't": 1, 'under': 1})
	>>>

## 通过公共键对字典列表排序 ##
