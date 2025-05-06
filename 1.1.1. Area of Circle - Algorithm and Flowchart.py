radius = float(input("Enter the radius : "))

if(radius < 0 or radius>100):
	print("Enter a positive value upto 100")
else:
	pi = 3.14
	area = pi*radius*radius
	print(f"Area of circle = {area:.6f}\n")
