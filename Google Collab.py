import math

# 1. Area of Circle
def area_of_circle(radius):
    return math.pi * radius ** 2

print("Area of Circle:", area_of_circle(5))


# 2. Area of Square
def area_of_square(side):
    return side ** 2

print("Area of Square:", area_of_square(4))


# 3. Area of Rectangle
def area_of_rectangle(length, width):
    return length * width

print("Area of Rectangle:", area_of_rectangle(5, 3))


# 4. Area of Triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

print("Area of Triangle:", area_of_triangle(6, 4))


# 5. Basic Arithmetic - Addition
def basic_addition(x, y):
    return x + y

print("3 + 10 =", basic_addition(3, 10))


# 6. Variable Assignment and Display
def display_variables():
    a, b, c = 10, 20, 30
    print("a =", a, "b =", b, "c =", c)
    return a, b, c

a, b, c = display_variables()


# 7. Conditional Statements
def compare_variables(a, b, c):
    if a > b and a > c:
        return "a is the largest"
    elif b > c:
        return "b is the largest"
    else:
        return "c is the largest"

print(compare_variables(a, b, c))


# 8. Integer Division and Modulo
def division_and_modulo(x, y):
    return x // y, x % y

div_result, mod_result = division_and_modulo(17, 5)
print("Integer Division:", div_result)
print("Modulo:", mod_result)


# 9. Digit Extraction (assuming 4-digit number)
def extract_digits(number):
    thousands = number // 1000
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    units = number % 10
    return thousands, hundreds, tens, units

print("Digits of 1234:", extract_digits(1234))


# 10. Digit Extraction using while loop
def digit_extraction():
    num = int(input("Enter a number to extract its digits: "))
    print("Digits in the number (from right to left):")
    while num > 0:
        digit = num % 10
        print(digit)
        num //= 10

digit_extraction()


# 11. Celsius to Fahrenheit Conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("30°C in Fahrenheit:", celsius_to_fahrenheit(30))


# 12. Fahrenheit to Celsius Conversion
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
print("86°F in Celsius:", fahrenheit_to_celsius(86))




"""
**********************************************************************************************************************************************************************************************************************************************************************
"""



# 1. Area with Input (Square and Rectangle)
def area_with_input():
    side = float(input("Enter side of square: "))
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    print("Area of Square:", side ** 2)
    print("Area of Rectangle:", length * width)

area_with_input()


# 2. Even or Odd
def even_or_odd():
    num = int(input("\nEnter a number to check even or odd: "))
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

even_or_odd()


# 3. Leap Year Check
def is_leap_year():
    year = int(input("\nEnter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a Leap Year")
    else:
        print(year, "is Not a Leap Year")

is_leap_year()


# 4. Grading System
def grading_system():
    marks = int(input("\nEnter your marks (0-100): "))
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print("Your Grade is:", grade)

grading_system()


# 5. Largest of Two Numbers
def largest_of_two():
    a = float(input("\nEnter first number: "))
    b = float(input("Enter second number: "))
    print("Largest number is:", max(a, b))

largest_of_two()


# 6. Sum of Two Numbers
def sum_of_two():
    x = float(input("\nEnter first number: "))
    y = float(input("Enter second number: "))
    print("Sum =", x + y)

sum_of_two()


# 7. 4-Digit Addition (Sum of digits without loop)
def sum_of_digits():
    num = int(input("\nEnter a 4-digit number: "))
    if 1000 <= num <= 9999:
        a = num // 1000
        b = (num % 1000) // 100
        c = (num % 100) // 10
        d = num % 10
        print("Sum of digits:", a + b + c + d)
    else:
        print("Not a valid 4-digit number")

sum_of_digits()


# 8. Percentage and Grade for 5 Subjects
def percentage_and_grade():
    print("\nEnter marks for 5 subjects:")
    s1 = float(input("Subject 1: "))
    s2 = float(input("Subject 2: "))
    s3 = float(input("Subject 3: "))
    s4 = float(input("Subject 4: "))
    s5 = float(input("Subject 5: "))
    
    total = s1 + s2 + s3 + s4 + s5
    percentage = total / 5

    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)

percentage_and_grade()




"""
**********************************************************************************************************************************************************************************************************************************************************************
"""




# 1. Basic For Loop
def basic_for_loop():
    print("Numbers from 1 to 10:")
    for i in range(1, 11):
        print(i, end=' ')
    print()

basic_for_loop()


# 2. Factorial Calculation using a For Loop
def factorial_calculation():
    num = int(input("\nEnter a number to calculate its factorial: "))
    if num < 0:
        print("Factorial not defined for negative numbers.")
        return
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)

factorial_calculation()




"""
**********************************************************************************************************************************************************************************************************************************************************************
"""



# 1. Prime Number Check
def is_prime():
    num = int(input("Enter a number to check if it's prime: "))
    if num <= 1:
        print(num, "is not prime.")
        return
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is not prime.")
            return
    print(num, "is a prime number.")

is_prime()


# 2. Palindrome Check (Slicing - for string)
def palindrome_check_slicing():
    word = input("\nEnter a word or phrase to check if it's a palindrome: ").replace(" ", "").lower()
    if word == word[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")

palindrome_check_slicing()


# 3. Palindrome Check (Integer Operations)
def number_palindrome_check():
    num = int(input("\nEnter a number to check if it's a palindrome: "))
    original = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    if original == reversed_num:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")

number_palindrome_check()


# 4. String Reversal (User-Defined Function)
def reverse_string_user_func():
    def reverse_string(s):
        result = ""
        for char in s:
            result = char + result
        return result
    
    text = input("\nEnter a string to reverse: ")
    print("Reversed string:", reverse_string(text))

reverse_string_user_func()


# 5. String Reversal (Slicing)
def reverse_string_slicing():
    text = input("\nEnter a string to reverse using slicing: ")
    print("Reversed string:", text[::-1])

reverse_string_slicing()


# 6. Palindrome Numbers in Range
def palindrome_in_range():
    start = int(input("\nEnter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    print("Palindrome numbers in range:")
    for num in range(start, end + 1):
        if str(num) == str(num)[::-1]:
            print(num, end=' ')
    print()

palindrome_in_range()
