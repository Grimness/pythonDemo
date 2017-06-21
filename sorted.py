s = sorted([1,2,-4,0,7])
print(s)
s = sorted([36,5,-12,9,-21],key=abs)
print(s)

s = sorted(['bob','about','Zoo','Credit']) #ASCLL码对比
print(s)
s = sorted(['bob','about','Zoo','Credit'],key=str.lower)
print(s)
#反向排序
s = sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True)
print(s)

