print(abs(-12))
print(abs)
x = abs(-12)
print(x)
f = abs
print(f(-15))

def add(a,b,f):
	return f(a) + f(b)
# 高阶函数是把函数作为参数传入另一个函数中
print(add(-1,4,f))
print(add(-1,4,abs))