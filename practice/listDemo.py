classmates = ['Michael','Bob','Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
# print(classmates[3]) 索引是从0开始的
print(classmates[-3]) #也可以从-1开始获取最后一个元素
classmates.append('Adam')
print(classmates)
classmates.insert(1,'Jack')
print(classmates)
print(classmates.pop())
print(classmates)
print(classmates.pop(0))
print(classmates)
classmates[0] = 'Marry'
print(classmates)
L = ['Apple',123,True] #list列表里的元素可以不相同
print(L)
s = ['python','java',['c#','php','javascript'],'html'] #list列表里还可以有列表 list嵌套
print(s)
print(len(s))
print(s[2][1]) #获取list列表里的元素

p = ['abc','defg','hahh']
j = ['123','12',p,'345']
print(j)