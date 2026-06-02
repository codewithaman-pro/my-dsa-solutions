# Tuple -> An Ordered collection of items which is immutable (cant't be changed after creation) and allows duplicate elements.
# Tuple is defined by using parenthesis () and itmes are separated by commas.

# TUPLE PACKING (without using parenthesis)
# skills = 'Python', 'DSA', 'ML'
# print(skills)
# print(type(skills))

# tuple() -> It is a built-in function that can be used to create a tuple from an iterable (like list, string etc.)
# my_list = [1, 2, 3]
# my_tuple = tuple(my_list)
# print(my_tuple)

#Tuple Unpacking -> It is a process of assigning the elements of a tuple to indivisual variables.
# Normal Unpacking
# user = ('Amit', 30, 'India')
# name, age, country = user
# print('Name:', name)
# print('Age:', age)
# print('Country:', country)

# Pro Unpacking -> It is used when we want to unpack a tuple 
# but we don't know the number of elements in the tuple or we want to ignore some elements.
# scores = (90, 85, 70, 65, 80)
# topper, runner_up, *others = scores
# print('Topper:', topper)
# print('Runner Up:',runner_up)
# print('Others:', others)

# Mutability of Nested Elementss 
# magical_tuple = ('Amit', 'Python', [10, 20])
# magical_tuple[1] = 'JAVA' -> TypeError
# magical_tuple[2].append(30) # This is allowed because the list inside the tuple is mutable.
# print(magical_tuple)

# Method 1: .count(value) -> It is used to count the number of occurrences of a value in a tuple.
# signals = ('Red', 'Green', 'Red', 'Yellow', 'Red', 'Green')
# red_count = signals.count('Red')
# print('Red light',red_count ,'baar aayi hai')

# Method 2: index(value, [start, [stop]]) -> This method tells you at which index (position) the item you specified is located first.
# alphabets = ('A', 'B', 'C', 'D', 'B')
# position = alphabets.index('B')
# print('the position of B:',position)

# Hidden rule (.index(value, start))
alphabets = ('A', 'B', 'C', 'B', 'D')
new_position = alphabets.index('B',2)
print('The position of second B:', new_position)