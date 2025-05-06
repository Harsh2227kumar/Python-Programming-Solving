a = float(input("subject 1: "))
b = float(input("subject 2: "))
c = float(input("subject 3: "))
d = float(input("subject 4: "))
e = float(input("subject 5: "))
avg = (a+b+c+d+e)/5.0
print(f"Average Marks: {avg:.2f}")
if(90.0<=avg<=100.0):
	grade = 'A'
elif(80.0<=avg<=89.0):
	grade = 'B'
elif(70.0<=avg<=79.0):
	grade = 'C'
elif(60.0<=avg<=69.0):
	grade = 'D'
else:
	grade = 'F'
print(f"Grade: {grade}")