def is_odd(n):
	return n % 2 == 1
l = list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10,11,15]))
print(l)

def not_empty(s):
	return s and s.strip()
l = list(filter(not_empty,['A','B',None,'C',' ']))
print(l)

def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter() #初始化iter
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n),it) # 构造新序列

for n in primes():
	if n < 1000:
		print(n)
	else:
		break
