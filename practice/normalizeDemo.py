from functools import reduce
def prod(s):
	return s[0].upper() + s[1:].lower()
print(list(map(prod,['aDmin','jAcK','liSa'])))

# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(l):
	def sun(x,y):
		return x * y
	return reduce(sun,l)

print(prod([1,2,3,4]))

def char2num(s):
	return {'.':.,'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2float()	