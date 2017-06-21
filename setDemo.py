s = set([1,2,3,4,4])
print(s)
s.add(5)
print(s)
s.remove(1)
print(s)

s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2) #交集
print(s1 | s2) #并集

l = [1,2,3,4]
j = set(l)
print(l)

a = ['c','b','a']
a.sort()
print(a)

a = 'abc'
print(a.replace('a','A'))
print(a)
b = a.replace('a','A')
print(b)
s = set([1,2,3])
print(s)