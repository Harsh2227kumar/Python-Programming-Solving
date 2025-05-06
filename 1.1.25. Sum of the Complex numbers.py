class Complex ():
	def initComplex(self,num):
		print(f"complex number {num}")
		print("Real Part:",end=" ")
		self.real=int(input())
		print("Imaginary Part:",end=" ")
		self.imag=int(input())
	def display(self):
		print(f"{self.real}+{self.imag}i")
	def sum(self,c1,c2):
		self.real = c1.real + c2.real
		self.imag = c1.imag + c2.imag


c1 = Complex()
c2 = Complex()
c3 = Complex()

c1.initComplex(1)
c1.display()
c2.initComplex(2)
c2.display()
print("Sum:",end=" ")

c3.sum(c1,c2)
c3.display()
