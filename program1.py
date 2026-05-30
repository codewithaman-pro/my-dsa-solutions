# printing output (print() function, f-strings, format method)
#using print() function
print("Hello World")
print("10, 20, 30")
print("python", "is", "fun", sep="-")

#using format() method
Name = "nick"
age = 22
print("My name is {} and I am {} years old.".format(Name, age))

#using f-strings
Name = "nick"
age = 22
print(f"My name is {Name} and I am {age} years old.")
# Printing with spacial characters
print("Hello\nWorld") # new line
print("Hello\tWorld") # tab space
print("Hello\\World") # backslash