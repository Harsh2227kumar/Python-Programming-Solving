def isPalindrom(str):
	cleanedStr = str.replace(" ", "").lower()

	if cleanedStr == cleanedStr[::-1]:
		print("palindrome")
	else:
		print("not a palindrome")
	
str = input()
isPalindrom(str)