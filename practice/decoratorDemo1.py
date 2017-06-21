import functools

def log(func):
	def dec():
		print('begin call %s' % func.__name__)
		result = func()
		print('end call %s' % func.__name__)
		return result
	return dec

@log
def before():
	print('在我之前之后')

before()