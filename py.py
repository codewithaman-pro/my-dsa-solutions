# How to find greatest value
'''
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
if a>b:
    if b>c:
        print(a,"is greatest")
    else:
        print(c,"is greatest")
else:
    if b>c:
        print(b,"is greatest")
    else:
        print(c,"is greatest")
                                '''


# check a laep year or not
'''x=int(input("enter the number:"))
if x%400==0:
    print(x,"is leap year.")
elif x%100==0:
    print(x,"is not leap year.")
elif x%4==0:
    print(x,"is leap year."),
else:
    print(x,"is leap year.")
'''

# make calculator
'''a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
c=input("enter the operator{+,-,*,/,%,//,**}\n")
if c=='+':
    print("sum",a+b)
elif c=='-':
    print("subtract",a-b)
elif c=='*':
    print("multiply",a*b)
elif c=='/':
    print("divide",a/b)
elif c=='%':
    print("remainder",a%b)
elif c=='//':
    print("value",a//b)
elif c=='**':
    ("of square",a**b)
else:
    print("doesn't exist !")'''


# Armstrong
'''
n=int(input("enter the number:"))
sum=0
num=n
while n>0:
    digit = n%10
    sum+=digit**3
    n//=10
    if num==sum:
        print("armstrong")
    else:
        print("not armstrong")'''


# find the palindrome
'''n=int(input("enter n digit number"))
num=n
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
    print("reverse",rev)
    if rev==num:
     print("palindrome")
else:
    print("not palindrome")
'''
    

# find the fibonacci series upto n terms 
'''nterms=int(input("how many terms?"))
n1,n2=0,1
if nterms<=0:
    print("please enter a positive number")
elif nterms==1:
    print(n1)
else:
   print("Fibonacci series")
   print(n1,n2, end=" ")
   for i in range (3,nterms+1):
    nth=n1+n2
    print(nth, end=" ")
    n1=n2
    n2=nth

'''
# Factorial Series
"""
def print_fact(a) :
    fact = 1
    if a < 0 :
        print("Invalid input, Enter a whole number!")
    elif a == 0 :
        print(f"factorial of {a} is {1}")
    else :
        for i in range(1, a+1) :
            fact *= i
    print(f"factorial of {a} is {fact}")


num = int(input("Please enter a positive number : "))
print_fact(num)
"""
# Check Armstrong
'''
def give_length(a) :
    b = str(a)
    return len(b)

def check_arm(a) :
    arm = 0
    org = a
    n = give_length(a)
    if a < 0 :
        return False
    elif a >= 0 :
        while a > 0 :
            rem = a % 10
            arm += rem**n
            a //= 10
    if org == arm :
        return True
    else :
        return False    

def print_armstrong(a, b) :
    count = 0
    for i in range(a, b+1) :
        if check_arm(i) :
            count += 1
            print(i, end=" ")
    print(f"\nTotal no of Armstrong no between {a} to {b} is {count}")

num1 = int(input("Please enter lower boundary : "))
num2 = int(input("Please enter upper boundary : "))
print_armstrong(num1, num2)
'''

# check a number is a prime 
'''
num=int(input("enter the number:"))
flag=False
if num==1:
 print(num,"is not a prime  number")
elif num>1:
 for i in range (2,num):
  if (num%i)==0:
   flag=True
   break
 if flag:
   print(num,"is not a prime number")
 else:
   print(num,"is a prime number")
else:
    print("enter positive number")
    '''


# print the following pattern
'''
rows=int(input("enter the number of rows:"))
for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    print("")
    '''

# concatenation in string
'''
str2="hellow"
str3="aman"
print(str2+" "+str3)
'''


# Using join() method for string concatenation
words=["hello", "aman"]
result=" ".join(words)
print(result)