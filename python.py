#Types of Operators
#Arithmetic Operators
a = 4
b = 6
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) #a^b

#Relational Operators
a = 20
b = 45

print(a == b)#False
print(a != b)#True
print(a < b)#True
print(a > b)#False
print(a <= b)#True
print(a >= b)#False

#Assignment Operators
num = 20
num = num + 20 #20 + 20 => 40
print(num)
num = 10
num -= 5
print("num :",num)#5
num = 6
num /= 3
print("num :", num)#2.0
num = 25
num %= 6
print("num :", num)#1
num = 5
num **= 5
print("num :", num)#3125

#Logical Operators
#NOT Operators
print(not False)#True
print(not True)#False
a = 30
b = 56
print(not(a < b))#False

#AND Operators
val1 = True
val2 = True
print("AND operator:", val1 and val2) #True

#OR Operators
val1 = True
val2 = False
print("OR operator:", (a == b) or (a > b))#False

#Type Conversion
a = 4
b = 3.3
sum = a + b
print("sum :", sum)

#Type Casting
a = int ("4")
b = 3.3
sum = a + b
print("sum :", sum)

#Input in Python
name = input("My name is:",)
print("Welcome", name)
name = input("My age is:",)
print("Your age is:", name)

name = input("enter name:")
age = int(input("enter age:"))
marks = float(input("enter marks:"))

print("welcome", name)
print("age =", age)
print("marks =",marks)

#Practice Quetions
#1.Write a program to input 2 numbers & print their sum
first = int(input("enter first :"))
second = int(input("enter second :"))
print("sum =", first + second)

#2.Write a program to input side of a square & print its area
side = float(input("enter square side :"))
print("area =", side * side)


