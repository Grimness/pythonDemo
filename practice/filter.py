def is_palindrome(n):
	return n == int(str(n)[::-1])
output = filter(is_palindrome,range(1,100))
print(list(output))

print('012345678910'[-3:0:-1])