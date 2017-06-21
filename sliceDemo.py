L = ['Michael','Sarah','Tracy','Bob','Jack']

r = []
n  = 3
for i in range(n):
	r.append(L[i])

print(r)

# 切片 0索引开始取数据 知道索引3(结束不包括3)
print(L[0:3])
print(L[1:4])
print(L[-2:-1])
L = list(range(100))
print(L[:10:2])
