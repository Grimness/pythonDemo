#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module'
__author__ = '李大帅'

import sys

def test():
	args = sys.argv
	if len(args)==1:
		print('Hello,world')
	elif len(args)==2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')

if __name__ == '__main__':
	test()


def _private_1(name):
	return 'Hello, %s' % name

def _private_2(name):
	return 'Hi %s' % name

def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)

print(greeting('j'))

from PIL import Image

im = Image.open('test.png')
print(im.format,im.size,im.mode) 
PNG (400,300) RGB
im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')