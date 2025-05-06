digit1 = int(input("digit1 (0-9): "))
digit2 = int(input("digit2 (0-9): "))
digit3 = int(input("digit3 (0-9): "))

if(0<=digit1<=9 and 0<=digit2<=9 and 0<=digit3<=9):
	digits = [digit1, digit2, digit3]

	perms = [
		[digit1, digit2, digit3],
		[digit1, digit3, digit2],
		[digit2, digit1, digit3],
		[digit2, digit3, digit1],
		[digit3, digit1, digit2],
		[digit3, digit2, digit1]
	]

	unique_perms = []
	for perm in perms:
		if perm not in unique_perms:
			unique_perms.append(perm)
			print(''.join(map(str, perm)))
else:
	print("Invalid")