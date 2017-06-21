names = ['Michael','Bob','Tracy']
scores = [95,75,85]
d = {'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])
d['Adam'] = 87
print(d['Adam'])
print(d)
print('Jack' in d)
print(d.get('Jack'))
print(d.get('Jack',0)) #get() 方法查找dict中是否存在对应的元素
d.pop('Bob') #pop()方法是删除对应的元素
print(d)
