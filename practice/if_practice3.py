hight = 1.75
weght = 80.5
bmi = weght / hight ** 2
print(bmi)
if bmi < 18.5:
	print('过轻')
elif (bmi > 18.5) and (bmi < 25):
	print('正常')
elif (bmi > 25) and (bmi < 28):
	print('过重')
elif (bmi > 28) and (bmi < 32):
	print('肥胖')
else:
	print('严重肥胖')

a = 15
if a > 20:
	print('20')
elif 20 > a > 10:
	print(a)