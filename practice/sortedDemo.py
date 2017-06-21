L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(L[0])
def buy_name(t):
	return t[0]
L = sorted(L,key=buy_name)
print(L)
def buy_score(s):
	return s[1]
L = sorted(L,key=buy_score,reverse=True)
print(L)