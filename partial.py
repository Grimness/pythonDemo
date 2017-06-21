print(int('1234'))

print(int('1234',base=8))
print(int('1234',base=10))
print(int('1234',base=16))
print(int('11110',base=2))

def int2(x,base=2):
	return int(x,base)

print(int2('110'))

import functools

# 偏函数定义
int2 = functools.partial(int,base=2)
print(int2('110'))

print(int2('110',base=10))