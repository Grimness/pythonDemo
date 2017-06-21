#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] rangge()方法生成一个list列表
print(list(range(1,11)))

# 生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1,11):
	L.append(x * x)
print(L)

# 生成[1x1, 2x2, 3x3, ..., 10x10]
print([x * x for x in range(1,11)])
nums = [x * x for x in range(10,21)]
print(nums)
nums = [x * x for x in range(1,11) if x % 2 ==0]
print(nums) # [4, 16, 36, 64, 100]

chars = [m + n for m in 'ABC' for n in 'XYZ']
print(chars) # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

import os
dirs = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print(dirs)

d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
	print(k,v)
print([k + '=' + v for k,v in d.items()]) # ['y=B', 'x=A', 'z=C']

L = ['HEllo','WORlD','IBM','GOOGle','XIAomi','APPle']
print([s.lower() for s in L]) # lower() 大写转成小写