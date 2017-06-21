from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('sdf',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))
for x in [1,2,3,4,5]:
	print(x)

print('=========================================================')
it = iter([1,2,3,4,5])
while True:
	try:
		 # 获得下一个值:
		x = next(it)
		print(x)
	except StopIteration:
		 # 遇到StopIteration就退出循环
		 break
