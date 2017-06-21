def now():
	print('2015-3-25')

f = now
f()

name = now.__name__
print(name)
print(f.__name__)

def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper

@log
def now():
	print('2015-3-25')

now()
print('now= %s' % now.__name__)

def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print('2015-3-25')

now()
print(now.__name__)

import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper

@log
def now():
	print('2015-3-25')

now()
print('函数等于: %s' % now.__name__)

import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print('2015-3-25')

now()
print(now.__name__)