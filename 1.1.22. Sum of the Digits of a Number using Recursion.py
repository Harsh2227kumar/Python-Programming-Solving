def Sumof(n):
	if n == 0:
		return 0
	else:
		return n%10 + Sumof(n//10)

# take user input and add the function call
n = int(input())
print(Sumof(n))

