import fibonacci_module

def main():
	try:
		n = int(input("Enter the max value: "))
		if n > 0:
			fibonacci_series = fibonacci_module.generate_fibonacci_sequence(n)
			print(f"Fibonacci series upto {n} :",)
			print(*fibonacci_series, end=" ")
		else:
			print("Please enter a positive integer")
	except ValueError:
		print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
	main()