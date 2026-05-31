# TOPIC: FUNCTIONS IN PYTHON(DAY 3)
# def check_even_odd(number):
#     if number % 2 == 0:
#         return f"{number} is an EVEN number"
#     else:
#         return f"{number} is an ODD number"
    
# print("--- Testing My first function ---")
# result1 = check_even_odd(10)
# print(result1)
# result2 = check_even_odd(15)
# print(result2)
# result3 = check_even_odd(1345)
# print(result3)

# def say_hello():
#  print('Good Morning Bhai! kaise ho?')
# say_hello()

# def greet(name):
#     print(f'Hello {name}, Python seekhne me mja aa rha hai!')
# greet('Aman')
# greet('Nick')

# def add_numbers (num1, num2):
#  ans = num1+num2
#  return ans

# my_total = add_numbers(20,50)
# print(f"The total is: {my_total}")

# final_price = my_total - 23
# print(f'The Final price is:  {final_price}')

# def billing_system(*item_prices):
#  total_bill=0
#  for price in item_prices:
#         total_bill = total_bill + price
#  return total_bill

# print('\n--- Testinng *args Functions ---')
# customer1 = billing_system(12,34,56,87)
# print(f'Total bill of Customer1: {customer1}')
# customer2 = billing_system(56,234,345,123,34,12)
# print(f'Total bill of Customer2: {customer2}')

#kwarags
# def save_user_profile(**user_info):
#     print('\n--- New User Profile Saved ---')
#     for key, value in user_info.items():
#       print(f'{key}: {value}')
# save_user_profile(name='Nick', age=21, city='Delhi', Profession='Student')

# SCOPE (LOCAL VS GLOBAL)
# academy_name = 'Python Learning Hub'
# def show_info():
#     student_name = 'Nick'
#     print(f'Inside Function: {student_name} is learning at {academy_name}')
# show_info()
# print(f'Outside Function: Academy name is {academy_name}')

#  LAMBDA FUNCTIONS
# print('\n--- Testing Lambda Function ---')
# def normal_square(x):
#     return x * x
# print(f'Square of 5 using normal function: {normal_square(5)}')
# lambda_square = lambda x : x * x
# print(f'Square of 5 using Lambda Function: {lambda_square(5)}')
# add_numbers = lambda a, b : a + b 
# print(f'Sum of 10 and 20 using Lambda Function: {add_numbers(10,20)}')


# RECURSION (Function Calling Itself)
# def find_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * find_factorial(n-1)
# print('\n--- Testing Recursion ---')
# result = find_factorial(5)
# print(f'Factorial of 5 using Recursion: {result}')

# PASS BY REFERENCE (MUTABLE VS IMMUTABLE)
# print('\n--- Testing pass by Object Reference ---')
# def modify_number(num):
#     num = num + 10 
#     print(f'Inside Function: Modified number is {num}')
# my_number = 40
# modify_number(my_number)
# print(f'Outside Function: Original number {my_number}')
# def modify_list(my_list):
#     my_list.append(99)
# print(f'Inside Function: Modified List is{modify_list}')
# original_list = [2,3,4]
# modify_list(original_list)
# print(f'Outside Function: Original List is {original_list}')
    
# HIGHER-ORDER FUNCTIONS (FUNCTIONS THAT TAKE OTHER FUNCTIONS AS ARGUMENTS)
# print('\n--- Testing Higher-Order Functions ---')
# def shout(text):
#     return text.upper() + '!!!'
# def whisper(text):
#     return text.lower() + '...'
# def GreetMaster(func, name):
#     return func(name)
# print(GreetMaster(shout, 'nick'))
# print(GreetMaster(whisper, 'NICK'))

# MAP AND FILTER WITH LAMBDA
# print('\n--- Testing Map and Filter with lambda ---')
# numbers = [4,5,6,7,8]
# all_squares = list(map(lambda x: x * x, numbers))
# print(f'Squares of numbers using Map and Lambda: {all_squares}')
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(f'Even numbers using Filter and Lambda: {even_numbers}')

# FUNCTION RETURNING ANOTHER FUNCTION
# print('\n--- Testing Function Returning another Function ---')
# def power_factory(power):
#     def calculator(number):
#         return number ** power
#     return calculator
# square_machine = power_factory(3)
# cube_machine = power_factory(5)
# print(f'Square of 4 using Square Machine: {square_machine(4)} ')
# print(f'Cube of 5 using Cube Machine: {cube_machine(5)} ')


# FUNCTION DECORATORS (ADDING EXTRA FUNCTIONALITY TO EXISTING FUNCTIONS)
# print('\n--- Testing Function Decorators ---')
# def my_decorator(func):
#     def wrapper():
#         print('*************************')
#         print('Before calling the function')
#         func()
#         print('After calling the function')
#         print('**************************')
#     return wrapper
# @my_decorator
# def say_hello():
#      print("-> HELLO NICK! I'm real function.")
# say_hello()


def dynamic_decorator(func):
    def wrapper(*args, **kwargs):
        print('----------------------------------')
        print('Decorator: Checking Arguments...')
        result = func(*args, **kwargs)
        print('Decorator: Execution complete!')
        print('-----------------------------------')
        return result
    return wrapper
@dynamic_decorator
def greet_user(name, topic):
    print(f'Hello {name}, welcome to {topic} class!')
greet_user('Nick', 'Python')