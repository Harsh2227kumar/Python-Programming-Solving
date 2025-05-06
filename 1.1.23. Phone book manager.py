def addContact(phoneBook):
	name = input("Name: ")
	phoneNo = input("Phone number: ")
	phoneBook[name] = phoneNo
def removeContact(phoneBook):
	name = input("Name: ")
	if name in phoneBook:
		del phoneBook[name]
	else:
		print("Not found")
def displayContact(phoneBook):
	if phoneBook:
		print(phoneBook)
	else:
		print("{}")
phoneBook = {}
while True:
	print("1. Add Contact")
	print("2. Remove Contact")
	print("3. Display")
	print("4. Quit")
	choice = input("Enter choice (1-4): ")
	if choice == '1':
		addContact(phoneBook)
	elif choice == '2':
		removeContact(phoneBook)
	elif choice == '3':
		displayContact(phoneBook)
	elif choice == '4':
		break
	else:
		print("Invalid")
