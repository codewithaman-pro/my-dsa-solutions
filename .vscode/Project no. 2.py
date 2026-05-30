#Write a python program to find the largest of three numbers
num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))
num3 = float(input("enter the third number"))

if(num1>=num2) and (num1>=num3):
    largest = num1
elif(num2>=num1) and (num2>=num3):
    largest = num2
else:
    largest = num3

    print("The largest number is:",largest)


#Write a python program to check whether a number is even or odd
num = int(input("Enter a number"))

if num %2 == 0:
    print(f"{num}is even")
else:
    print(f"{num}is odd")


    num = float(input("Enter a number:"))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#Write a python program to check if a character is a vowel or a consonant
char = input("Enter a single character:")
if len(char) == 1 and char.isalpha():
    char = char.lower()
if char in 'aeiou':
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonent:")


#Write a python program that determine the type of a triangle based on the lengths of sides.
#(all three sides equal = Equilateral, two sides are equal = Isosceles and all sides are diffent = Scalene)
a = float(input("Enter the first side of the triagle:"))
b = float(input("Enter the second side of the triagle:"))
c = float(input("Enter the third side of the triagle:"))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("The triangle is Equilateral.")
    elif a == b or b == c or a == c: 
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalence.")


#Write a Python program to calculate the Body Mass Index (BMI) of a person
height_cm = float(input("Enter your height in centimeters:"))
weight_kg = float(input("Enter your weight in kilograms:"))

height_m = height_cm/100

bmi = weight_kg / (height_m**2)
print(f"\nYour BMI is:{bmi:2f}")

if bmi < 18.5:
    print("Category: Under weight")
elif 18.5<=bmi<=24.9:
    print("Category: Normal weight")
elif 25<=bmi<=29.9:
    print("Category: Over weight")
else:
    print("Category: Obese")
    

#Write a Python program to find the factorial of a given number.
num = int(input("Enter a number:"))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers:")

else:
    for i in range(1, num + 1):
        factorial *=i
        print(f"THe factorial of {num} is {factorial}")


#Write a program to check whether a number is prime or not.
num = int(input("Enter a number:"))

if num <= 1:
    print(num, "is not a prime number")
else:
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num %i == 0:
            is_prime = False
            
            if is_prime:
                print(num, "is a prime number")
            else:
                print(num, "is not a prime number")


#Write a program to print the multiplication table of a given number.
num = int(input("Enter a number:"))
print(f"\nMultiplication Table of{num}:\n")
for i in range(1,11):
    print(f"{num}x{i}={num*i}")

#Write a program to generate the Fibonacci series up to n terms.
n = int(input("Enter the number of terms:"))
a,b = 0,1
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci series up to 1 term:")
    print(a)
else:
    print(f"Fibonacci series up to {n} terms:")
    for i in range(n):
        print(a,end='')
        a,b = b, a + b


#Write a program to find the sum of all digits in a number.
num = int(input("Enter a number:"))
sum_of_digits = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_digits+=digit
    temp = temp//10
    print("The sum of digits in",num,"is",sum_of_digits)


#Write a Python program to simulate the Roller Coaster Game. The program should prompt the user to enter their age and height.

height = int(input("Enter your height in cm: "))


if height < 100:
    print("Sorry, you must be at least 100 cm tall to ride the roller coaster.")
else:
    
    age = int(input("Enter your age in years: "))
    
    
    if age < 12:
        ticket_price = 50  
    elif age <= 18:
        ticket_price = 70  
    elif age <= 60:
        ticket_price = 100  
    else:
        ticket_price = "Not Eligible"
    print(f"You are eligible to ride! Your ticket price is ${ticket_price}.")