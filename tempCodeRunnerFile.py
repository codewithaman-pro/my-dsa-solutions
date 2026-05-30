'''
for i in range(1,11):
    print("2 *",i,"=",i*2)

print()

for a in range (10,0,-1):
    
    print("2 *",a,"=",a*2)


    # While loop 
  i = 1
while i<=10:
    print("Aman Sharma")
    i=i+1
    print(i)

a=11
while a>=1:
        print("How")
        a=a-1

        print(a)

# Indexing Stirng and Slicing
a = " Today , I am learning Python"
print(a[-28])
print(a[0:23])
print(a[0::2])
print(a[-1::15]) 
print(a[-1::8])
print(a[-1::-1])
print(a[-1:-29:-3])
'''

# String Iteration
"""a=" I want to improve my Python Language"
'''a=a[-1::-1]''' # for reverse
b=len(a)
print(b)
for i in range (b):
    print(i)

    print()

    print(a[i])

print()


for c in range(b-1,-1,-1):
        print(a[c])
     
# Without using Range and length
a = "Today , I have completed while loop"
for i in a:
    print(i)
"""
# python string function lower(),upper(), title(),capitalize()
a = "Aman Sharma B.Tech 2nd Year 4 Semester"
print(a.lower())
print(a.upper())
print(a.title())
print(a.capitalize())
print(a.find("r",9))# It gives index number of the string
print(a.find("z")) # if z is no available in string then 
                    #it gives negative value (-1).
print(a.index("r",27)) # it also gives indexing value
s="check"
print(s.isalpha()) # it gives True or False value
# when all string are alphabet then it gives True. only have to be in string 
f="fast" # false because there is string , we have to take only integer value.
g="12345"
print(f.isdigit())
print(g.isdigit()) # when all string are numbers then gives True. only have to be in integer
b="amansharma1234"
print(b.isalnum())
c="words 12233" 
print(c.isalnum()) # false because there is one space in this string

# chr(),ord() Function-> it gives ASCII value of integer&string.
# chr() function-> if we take integer then returns string.               
# ord() function-> if we take string then returns integer.
# we have to take only one string
d= 67
print(chr(d)) 
e='a'
f='G'
print(ord(e))
print(ord(f))       

# format() method-> inserts values into string placeholders defined by curly braces{}.
a = "My name is {} {}".format("Aman", "Sharma")
print(a)
b = "I am from {0} \npost: \n{1} \ndistrict: \n{2} \n{3}".format("Matihaniya Khurd","Pakadi Bujurg","Kushinagar","Uttar Pradesh")
print(b)
c = "I have completed B.Sc.{} from UNPG College Padrauna Kushinagar \nUttar Pradesh".format("in Mathematics")
print(c)
d = "Now, I am pursuing {} in {} from {} {} {}".format("B.Tech.","Data Science","VGI Dadri", "Greater Noida","\nUttar Pradesh")
print(d)
e = "I am {} {} {} ".format("20","Years","Old")
print(e)
f = "From {a} to {b}".format(a=15,b=26)
print(f)
g = "From {b:^15} to {a:^15}".format(a=15,b=26) # ^ = for center ----4----
print(g)
# which is inserting number 15 then, that is characters size
h = "From {a:<15} to {b:<15}".format(a=23,b=34) # < = for left 4--------
i = "From {a:>15} to {b:>15}".format(a=45,b=56) # > = for right --------4
print(h)
print(i)


# List -> mutable,changable,used in square braces []  
