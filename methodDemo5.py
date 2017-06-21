 

# 位置参数
def calc(numbers):
	sum = 0
	for n in numbers:
		sum+=n*n
	return sum
print(calc([1,2,3]))
print(calc([1,3,5,7]))

# 可变参数 
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum+=n*n
	return sum
print(calc(1,2,3))
print(calc())

nums = [1,2,3]
print(calc(*nums))


# 关键字参数
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

person('Michael',20)
person('Jack',30,city='Beijing')
person('Jack',30,city='guangzhou',gender='男')

extra = {'city':'Beijing','job':'Engineer'}
person('marry',25,**extra)

# 关键字参数
def person(name,age,**kw):
	if 'city' in kw:
		#有city参数
		pass
	if 'job' in kw:
		#有job参数
		pass
	print('name:',name,'age:',age,'other:',kw)

person('Lucy',23,city='Beijing',addr='Chaoyang',zipcode=12345)

# 命名关键字参数
def person(name,age,*,city,job):
	print('name:',name,'age:',age,city,job)

person('java',12,city='beijing',job='hahah')
# 命名关键字参数
def person(name,age,*kw,city,job):
	print(name,age,kw,city,job)

person('java',21,city='Beijing',job='adfsdfsd')

# 组合参数 顺序 = 位置参数>默认参数>可变参数>关键字参数
def f1(a,b,c=0,*args,**kw):
	print('a:',a,'b:',b,'c:',c,'args:',args,'kw:',kw)

def f2(a,b,c=0,*,d,**kw):
	print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

f1(1,2)
f1(1,2,4)
f1(1,2,c='a')
f1(1,2,3,'a','b','c')
f1(1,2,3,'a','b','c',x=99,city='Beijing')

f2(1,2,d=99,ext=None)

args = (1,2,3,4)
kw = {'d':98,'x':'#'}
f1(*args,**kw) 
args = (1,2,3)
kw = {'d':99,'x':'b'}
f2(*args,**kw)