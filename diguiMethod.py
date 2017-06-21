
# 递归函数
def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

print(fact(7))

#===> fact(5)
#===> 5 * fact(4)
#===> 5 * (4 * fact(3))
#===> 5 * (4 * (3 * fact(2)))
#===> 5 * (4 * (3 * (2 * fact(1))))
#===> 5 * (4 * (3 * (2 * 1)))
#===> 5 * (4 * (3 * 2))
#===> 5 * (4 * 6)
#===> 5 * 24
#===> 120

# 尾递归
def fact(n):
	return fact_iter(n,1)

def fact_iter(num,product):
	if num == 1:
		return product
	return fact_iter(num - 1,num * product)
print(fact(5))

# 利用递归函数移动汉诺塔
def move(n,a,b,c):
	if n == 1:
		print('move',a,'-->',c)
		return 
	move(n-1,a,c,b)
	print('move',a,'-->',c)
	move(n-1,b,a,c)
move(3,'A','B','C')
