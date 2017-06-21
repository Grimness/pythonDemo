from collections import Iterable

d = {'a':1,'b':2,'c':3}
for key in d:
	print(key)

for value in d.values():
	print(value)

for ch in 'ABCDEFG':
	print(ch)

print(isinstance('abc',Iterable))
print(isinstance([1,2,3,4],Iterable))
print(isinstance(12345,Iterable))

# enumerate() 方法可以让遍历对象生成角标
for i,value in enumerate(['A','B','C']):
	print(i,value)

for x,y in [(1,1),(2,4),(3,9)]:
	print(x,y)