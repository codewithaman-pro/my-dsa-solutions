# Set -> A Set is an unorderd collection of unique and immutable elements in Python.
# It is defined by enclosing elements inside curly braces {} or by using the set() constructor.

# How to create a set
# Method A: Using Curly braces {}
# my_set = {10, 20, 30, 40, 20, 30}
# print(my_set)

# # Method B: Using set() Constructor
# names_list = ['Amit', 'Rahul', 'Amit', 'Priya']
# unique_names = set(names_list)
# print(unique_names)

# Adding & Removing Elements
# .add() Method -> This method is used to add a single element to the set. If the element is already present,
# it has no effect.
# names = {'Amit' , 'Rahul'}
# names.add('Priya')
# print(names)
# names.add('Amit') # Duplicate not allowed
# print(names)
  
# .update() Method -> This method is used to add multiple elements at onces. 
# You can pass a list, tuple, or another set as an argument.
# my_set = {10, 20}
# my_set.update([30, 40, 50], (60, 70))
# print(my_set)  

# Remove Element
# .remove() Method -> Removes the specified element from the set. If the element does not exist,
# it raises a KeyError.
# numbers = {1, 2, 3, 4}
# numbers.remove(2)
# print(numbers)

# .discard() Method -> Removes the specified element from the set.
# If the element does not exist, it does NOTHING and does not raise any error.
# numbers = {1, 3, 4 ,5}
# numbers.discard(4)
# print(numbers)

# .pop() -> Removes and returns an arbitary element from the set.
# Since sets are unorderd, you can't predict which element will be removed.
# items = {'Apple', 'Banana', 'Cherry', 'Orange'}
# deleted_item = items.pop()
# print('Removed Item:', deleted_item)
# print('Updated Item:', items)

# .clear() -> Removes all elements from the set, leaving it completely empty.
# data = {10, 20, 30, 40}
# data.clear()
# print(data)

# Basic Mathematical Operaitons (Union & Intersection)
# 1. Union -> The Union of two sets returns a new set containing all unique elements from both sets. 
# It can be performed using the .union() method or the pipe operator | .
# python_students = {'Amit', 'Rahul', 'Priya'}
# web_students = {'Rahul', 'Karan', 'Sneha'}
# # Method 1. Use function union()
# all_students = python_students.union(web_students)
# print('Union Function:', all_students)
# # Method 2. Use pipe Operator (|) 
# all_students_1 = python_students | web_students
# print('Union Operator:', all_students_1) 

# Intersection -> The intersection of two sets returns a new set containing only the elements that 
# are common to both sets. It can be performed using the .intersection() method or the ampersand operator & .
# python_students = {'Amit', 'Rahul', 'Karan', 'Pappu'}
# web_students = {'Rahul', 'Amit', 'Sneha', 'Ritesh'}
# # Use function .intersection()
# common_students = python_students.intersection(web_students)
# print('Intersection Function:', common_students)
# # Use operator ampersand &
# common_students_1 = python_students & web_students
# print('Intersection Operator:', common_students_1)

# Advanced Mathemetical Operations (Difference & Symmetric Difference)
# 1. Difference -> The difference between two sets (A-B) returns a new set containing elements 
# that are present in set A but NOT present in set B. It can be performed using the .difference() method or the minus operator (-).
# python_students = {'Amit', 'Rahul', 'Ankit'}
# web_students = {'Rahul', 'Karan', 'Sneha'}
# only_python = python_students.difference(web_students)
# print('Defference Function:', only_python)
# # Use operator (-)
# only_web = web_students - python_students
# print('Difference Operator:', only_web)

# Union Update Operator (|=) -> It updates the set on the left with the union of itself and the set on the right.
# set_a = {1,2}
# set_b = {3,4}
# set_a |= set_b
# print('Union Update:', set_a)

# Intersection Update operator (&=) -> It updates the set on the left with the intersection of itself and the set on the right.
# set_x = {1,2,3}
# set_y = {3,4,5}
# set_x &= set_y
# print('Intersection Update:', set_x)

# Symmetric Difference Update Operator (^=) -> It updates the set on the left with the symmetric difference of itself and the set on the right.
# set_a = {1,2,3}
# set_b = {3,4,5}
# set_a ^= set_b
# print('Symmetric Update Operator:', set_a)

# Strict Subset Operator (Comparison Operator) -> A Strict subset (<) means set A is a subset of B, but set A is not equal to set B.
# set B must have at least one extra element.
# a = {1,2,3,}
# b = {1,2,3,4}
# c = {1,2}
# print('Strict Subset:', a<b)
# print('Strict Subset:', a<c)
# print('Normal Subset:', a<=c)

# Strict Superset / Proper Superset (>) -> Set a is a strict superset of set B(written as A > B) if and only if 
# set A contains all elements of set B, and set A has at least one extra element that is not in set B.
# In other words, set A and set B can't be equal.
# set_A = {1,2,3}
# set_B = {1,2}
# print('Case (>):', set_A > set_B)

# when both sets are equal.
# set_A = {1,2}
# set_B = {1,2}
# print('Case 2:', set_A > set_B)
# print('Normal Superset (>=):', set_A >= set_B)

# set_A = {1,2,3}
# set_B = {4,5}
# print('Case 3:', set_A > set_B )

# Set Comprehension -> A short and elegant way to create set dynamically using a for loop inside curly braces.
# squares_set = {x**2 for x in [1,2,2,3,4,5]} #  duplicate doesn't allowed.
# print('Set Comprehension:', squares_set)
# # Set comprehension with if condition (Advanced Filtering)
# number_list = {1,2,3,4,5,6,4,2}
# even_squares = {x * x for x in number_list if x % 2 == 0}
# print('Square number of Even:', even_squares)
# Comparison & Relaitonship Methods

# Dunder Methods -> Dunder Methods (short for 'Double Underscore') are special hidden methods in Python
# that start and end with __. When you use operators like in ,|, &, or len(), Python internally maps them to these
# dunder methods. Calling these methods directly gives the exact same result.
# Method A: -> __contains__ :-> Triggered when you check if an element exists using the in keyword.
my_friends = {'Amit', 'Rahul', 'Ankit'}
print('Rahul' in my_friends)
print(my_friends.__contains__('Rahul'))

# 1. issubset() -> The issubset() method returns True if all elements of the set A are present in set B.
# Otherwise, it returns False. You can also use the <= operator.
# big_cities = {'Delhi', 'Mumbai', 'Kolkata', 'Chennai'}
# small_cities = {'Delhi', 'Mumbai'}
# print(small_cities.issubset(big_cities))
# print(small_cities <= big_cities)
# print(big_cities.issubset(small_cities))

# issuperset() -> issuperset() method returns True if set A contains all elements of set B.
# Otherwise, it returns False. You can also use the >= operator.
# big_cities = {'Delhi', 'Mumbai','Kolkata', 'Chennai'}
# small_cities = {'Delhi', 'Mumbai'}
# print(big_cities.issuperset(small_cities))
# print(big_cities >= small_cities)

# isdisjoint() -> The isdisjoint() method returns True if two sets have a null intersection,
# meaning they have no common elements. if there is even one common element, it returns False.
# set_x = {1,2,3}
# set_y = {4,5,6}
# set_z = {3,7,8}
# print(set_x.isdisjoint(set_y))
# print(set_x.isdisjoint(set_z)) 

# Global Functions, Loops & frozen Set
# 1. Frozen Set -> A frozenset is an immutable version of a Python set object.
# Once created, elements can not be added or removes from it.
# Because it is immutable, a frozenset is hashable and can be used as a key in a dictionary or as 
# an element in another set.
# normal_set = {1,2,3}
# frozen_data = frozenset(normal_set)
# print(type(frozen_data))
# frozen_data.add(4)

# Global Utility Functions
# Function (A): len() -> It counts and returns the total number of elements in the set.
# my_data = {10,20,30,40,20,30,}
# total_items = len(my_data)
# print('Total number of elements in the set:', total_items)

# Function (B): max() -> It scans the set and returns the element with the maximum value.
# scores = {45,56,345,32,58}
# highest_score = max(scores)
# print('Big Value is:', highest_score)

# Function (C): min() -> It scans the set and returns the element with the minimum value.
# scores = {23,45,67,89,90}
# smallest_score = min(scores)
# print('Small Value:', smallest_score)


# Function any() -> It returns True if at least one element in the set is a truthy value
# (non-zero, non-empty, or True). If the set empty, it returns False.
# test_set = {0, False, 5, 10}
# result = any(test_set)
# print(result)

# Function all() -> It returns True only if all elements in the set are truthy values
# (no zeros, no False). Even a single falsy value will make it false. 
# marks_set = {10, 20, 0, 40}
# final_check  = all(marks_set)
# print(final_check)

# Iterating Over a Set -> Since sets don't have index numbers, we can't use while loop with index counters.
# we must use a for loop to access elements.
# programming_language = {'Python', 'Java', 'C', 'C++', 'JavaScript'}
# for language in programming_language:
#     print('Language Name:', language)

# While loop can't work directly in the set but we can work indirectly.
my_set = {'Python', 'Java', 'C++'}
set_iterator = iter(my_set)
print('--- Output from while loop ---')
while True:
    try:
        item = next(set_iterator)
        print(item)
    except StopIteration:
        break
