def f(x):
	return x * x

r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
s = list(map(str,[1,2,3,4,5,6,7,8,9]))
print(s)
from functools import reduce
def add(x,y):
	return x + y
# reduce 作用两个参数
n = reduce(add,[1,3,5,7,9])
print(n)
print(sum([1,2,3]))
def fn(x,y):
	return x * 10 + y

n = reduce(fn,[1,2,3,4])
print(n)

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

n = reduce(fn,map(char2num,'13579'))
print(n)

def str2int(s):
	def fn(x,y):
		return x * 10 +y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn,map(char2num,s))

print(str2int('123321'))

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
	return reduce(lambda x,y: x * 10 + y,map(char2num,s)


