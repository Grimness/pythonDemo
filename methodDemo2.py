# -*- coding: utf-8 -*-

# 定义函数  def 函数名(参数1...):
def myAbs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

#调用函数
print(myAbs(-123))

def nop():
	pass

print(nop())