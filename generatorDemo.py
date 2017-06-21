L = [x * x for x in range(10)] # range(10) 生成0 -10 的list列表
print(L)

g = (x * x for x in range(10)) # 生成generator对象
print(g)
print(next(g)) # generator对象需要使用next()方法遍历
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# 遍历generator
for n in g:
	print(n)

def fib(max):
	n,a,b = 0,0,1
	while n < max:
		print(b)
		a,b = b,a+b
		n = n +1
	return 'done'
fib(6)

# yield 使用关键字就能变成generator
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b # 把结果变成generator
		a,b = b,a+b
		n = n +1
	return 'done'
print(fib(6))

def odd():
	print('step1')
	yield 1
	print('step2')
	yield 2
	print('step3')
	yield 3

print(next(odd()))
