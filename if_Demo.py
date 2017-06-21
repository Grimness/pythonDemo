age = 2
if age >= 18:
	print('已经成年')
	print('今年%d岁' % age)
elif age >= 6:
	print('今年%d岁' % age)
	print("青少年")
else:
	print('今年%d岁' % age)
	print('儿童')


if 1:
	print('True')
else:
	print('False')

year = input('出生年份:') #input()输入的是str类型  不能和整数比较
birth = int(year) #把str 通过int()转换成整数类型
if birth < 2000:
	print('00前')
else:
	print('00后')