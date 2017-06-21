# -*- coding: utf-8 -*-

def pwoer(x):
	return x * x

#print(pwoer(15))


def pwoer(x,n):
	s = 1
	if x==0:
		return'0的次方没有意义'
	while n > 0:
		n-=1
		s*=x
	return s

#print(pwoer(0,3)) 

def pwoer(x,n=2): #默认参数n=2
	s = 1
	while n > 0:
		n-=1
		s*=x
	return s

print(pwoer(5,1))

def enroll(name,gender):
	print('name:',name)
	print('gender:',gender)

def enroll(name,gender,age=6,city='Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)

enroll('jack','男')

enroll('lucy','女',18,'广西')

enroll('marry','女',city='我家门口')

def add_end(L=[]):
	L.append('END')
	return L
print(add_end([1,2,3]))
print(add_end(['a','b','c']))
print(add_end())
print(add_end())
print(add_end(L=[1,2]))
print(add_end())