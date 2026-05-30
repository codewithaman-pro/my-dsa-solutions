print("Jai Shree Ram")
print(23>6)
a=12
b=12
print('a',b)
print(id(a),id(b))
# string concatenation
a="aman"
b="sharma"
print(a+" "+b)
c=45
print(c+45) # this will work as both are integers
#print(a+c) # this will give error as we cant contatanate string and integer

# 1.Arithmetic Operarators
#Operators: +, -, *, /, %, //,  **
a1=10
b1=5
print("Addition:",a1+b1) # 10+5=15
print("Subtraction:",a1-b1) # 10-5=5
print("Multiplication:",a1*b1) # 10*5=50
print("Division:",a1/b1) # 10/5=2.0
print("Modulus:",a1%b1) # 10%5=0
print("Floor Division:",a1//b1) # 10//5=2
print("Exponentiation:",a1**b1) # 10**5=100000
# 2.Assignment Operators
# Operators: =, +=, -=, *=, /=, %=, //=, **=
a2=20
print("Initial value of a2:",a2) # 20
a2+=6
print("After a2+=6:",a2) # 20+6=26
a2-=5
print("After a2-=5:",a2) # 26-5=21
a2*=7
print("After a2*=7:",a2) # 21*=7=147
a2/=5
print("After a2/=5:",a2) # 147/5=29.4
a2%=6
print("After a2%=6:",a2) # 29.4%6=5.4
a3=54
a3//=8
print("After 54//=8:",a3) # 54//=8=6
a3**=5
print("After a3**=5:",a3) # 6**5=7776

# 3.Comparison Operators
# Operators: == (Equal), != (Not Equal), > (Greater Than), < (Less Than), >= (Greater Than or Equal to), <= (Less Than or Equal to)
x=14
y=23
print("x==y:",x==y) #False
print("x!=y:",x!=y) #True
print("x>y:",x>y) #False
print("x<y:",x<y) #True
print("x>=y:",x>=y) #False
print("x<=y:",x<=y) #True

# 4.Logical Operators
# Operators: AND, OR, NOT
p=4<5
q=5<5
print("p and q:",p and q) #False
print("p or q:",p or q) #True
print("not p:",not p) #False
print("not q:",not q) #True

# 5.Membership Operators
# Operators: in, not in
str1="Hello friends, My name is aman sharma" 
print("Is aman in str1?:","aman" in str1) # True
print("Is john in str1?:","john" in str1) # False
print("IS my in str1?:","my" in str1) # False
print("Is john not in str1?:","john" not in str1) # True
print("Is aman not in str1?:","aman" not in str1) #False

# 6.Identity Operators
#Operators: is, is not
m=45
n=34
print("m is n:",m is n) #False
print("n is m:",n is m) #False
print("m is not n:",m is not n) #True
print("n is not m:",n is not m) #True

# 7.Bitwise Operators
# Operators: & (AND), | (OR), ^ (XOR), ~ (Bitwise NOT), << (Left Shift), >> (Right Shift), >>> (Unsigned Right Shift)
a1=10
b1=8
print("a1 & b1:", a1 & b1,"\n", bin(a1),"\n",bin(b1)) # 10=1010, 8=1000 => 1000=8
print("a1 | b1:", a1 | b1,"\n", bin(a1),"\n",bin(b1)) # 10=1010, 8=1000 => 1010=10
print("a1 ^ b1:", a1 ^ b1,"\n", bin(a1),"\n",bin(b1)) # 10=1010, 8=1000 => 0010=2
print("~a1:", ~a1,) # ~10=1010 => 0101=-11
print("~b1:", ~b1,) # ~8=1000 => 0111=-9
print("a1 << 2:", a1 << 2) # 10=1010 => 101000=40
print("b1 >> 2:", b1 >> 2) # 8=1000 => 0010=2





# Data Types in Python
# Sequence Types: list, tuple, range, string
# Mutable data types: list, dictionary, set, bytearray
# Immutable data types: int, float, complex, string, tuple, frozenset, bytes 
# Numeric Types: int, float, complex
b=10
c=10.5
d=3+4j
print("Integer value:",b,type(b))
print("Float value:",c,type(c))
print("Complex value:",d,type(d))


# Sequence Types: string, list, tuple, range
# String Type [ This is immutable] and [you can only write in single, double or triple quotes]
s='this is a string'
s= "this is a string"
s= """this is a string"""
s= '''this is a string'''
print('Single quote:',s,type(s))
print("Double quote:",s,type(s))
print("""Triple quote:""",s,type(s))
print('''Triple quote:''',s,type(s))


# List Type [This is mutable] [List can change, delete and update values]
l=[1,4.5,'alex',3+5j]
l[3]=9
l[2]='aman'
l[0]=2
l[1]=7
print("list:",l,type(1))


# Tuple Type [This is immutable] [Tuple cannot change, delete and update values]
t=(3,5.4,'team',4+8j)
print("tuple:",t,type(t))
### t(0)=9  this will give error as tuple is immutable

# Range Type [This is immutable] [Range cannot change, delete and update values]
r=range(2,9) 
### r(0)=4 # this will give error as range is immutable
print("range:",r,type(r))


# Dictionary Type [This is mutable] [Dictionary can change, delete and update values]
d={'name':'aman','age':22,'course':'Btech'}
d['age']=23
d["course"]='mtech'
d["name"]='nick'
print("dictionary:",d,type(d))
print(d['name'], d['age'],d['course'])


# Set Type [This is immutable] [Set cannot change, delete, and update]
s={3,5,5,6}
print(s,type(s))



# Getting User Input & Type Casting
'''
a=input("Enter the value1:")
b=input("Enter the value2:")
print(a+b)

c=int(input("Enter the value3:"))
d=int(input("Enter the value4:"))
print(c+d)

e=float(input("Enter the value5:"))
f=float(input("Enter the value6:"))
print(e+f)

g=eval(input("Enter the number:"))
h=eval(input("Enter the number:"))
print(g+h)
'''

# Python COnditional Statements
# if statement, if else statement, if elif statement
'''
x=int(input("Enter the value1:"))
if x%2==0:
    print(x,"Even number")
else:
    print(x,"Odd number")

per=int(input("Enter the number:"))
if per>=50:
    print("First division")
elif per>=48:
    print("Second division")
elif per>=35:
    print("Third division")
else:
    print("Fail")
'''


# How to build simple Calculator in Python

print('''
      + ADD
      - SABTRACT
      * MULTIPLY
      / DIVIDE''')
while True:
    NUM=float(input("Enter the value1:"))
    NUM1=float(input("Enter the value2:"))
    opr=input("Enter the opr...:")
    if opr=="+":
        print(NUM+NUM1)
    elif opr=="-":
     print(NUM-NUM1)
    elif opr=="*":
        print(NUM*NUM1)
    elif opr=="/":
        print(NUM/NUM1)
    elif opr=="%":
        print(NUM%NUM1)
    elif opr=="^":
        print(NUM^NUM1)
    elif opr=="**":
        print(NUM**NUM1)
    else:
        print("Invalid Operation")

    print("\n---Option---")
    print("1.Continue")
    print("2.Clear")
    print("3.Exit")
    ch=input("Choose:")
    if ch == "1":
        continue
    elif ch == "2":    
        print("\nScreen Cleared!\n")
        continue
    elif ch == "3":
        print("Calculator Closed.")
        break
    else:
        print("Invalid Choise. Try Again!")

        continue


        