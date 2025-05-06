import math
import cmath

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = b**2 - 4*a*c

if(d>0):
	root1 = (-b + math.sqrt(d))/(2*a)
	root2 = (-b - math.sqrt(d))/(2*a)
	print(f"The roots are: {root1:.2f} and {root2:.2f}")
elif d==0:
	root = -b/(2*a)
	print(f"The root is: {root:.2f}")
else:
	real_part = -abs(b / (2 * a))  
	imag_part = (cmath.sqrt(abs(d)) / (2 * a)).real 
	print(f"The roots are: {real_part:.2f}{imag_part:+.2f}j and {real_part:.2f}{-imag_part:+.2f}j")

