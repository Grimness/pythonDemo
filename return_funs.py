def calc_sum(*args):
	ax = 0 
	for n in args:
		ax = ax + n
	return ax

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

f = lazy_sum(1,2,3,4,5)
print(f)

# 函数没有被执行,循环中的值不会被使用
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)
	return fs
f1,f2,f3 = count()
print(f1())

def count():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i)) #f(i) 立刻执行,因此i的当前值被传入f()
	return fs

f1,f2,f3 = count()
print(f1())