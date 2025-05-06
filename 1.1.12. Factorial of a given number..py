num = int(input("Enter a number : "))
if(num<0):
	print("Enter a positive number")
else:
	fact = 1
	for i in range(1, num+1):
		fact *= i
	print(f"Factorial of given number is : {fact}")