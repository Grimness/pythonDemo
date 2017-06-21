import functools

def log(text=None):
	def dec(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			if text==None:
				print('Call %s():' % func.__name__)
			else:
				print('%s %s():' %(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return dec

@log()
def now():
	print('2015-3-25')
@log('你好吗?')
def say():
	print('光棍节')

now()
print(now.__name__)
say()
print(say.__name__)