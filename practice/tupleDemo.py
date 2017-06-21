classmates = ('Michael','Bob','Tracy')
print(classmates[0])
print(classmates[-1])
t = (1,2)
print(t)
t = () #空的tuple
print(t)
t = (1,) #只有一个元素的tuple后面需要加个','号
t = ('a','b',['A','B']) #tuple里包含list  list里的元素可以被改变
t[2][0] = 'c'
t[2][1] = 'd'
print(t)