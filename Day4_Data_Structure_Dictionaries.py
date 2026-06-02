# Dictionary -> A coolection of key-value pairs which is unordered, mutable (can be changed after creation)
#  and does not allow duplicate keys. Dictionary is defined by using curly brackets {} and key-value pairs are separated by commas.
# user_data = {
#     'name' : 'Amit',
#     'age' : 23,
#     'is_verified' : True,
#     'skills' : ['Python', 'SQL']
# }
# print(user_data)
# print(type(user_data))

# Accessing value in a dictionary -> We can access the value in a dictionary by using the key inside square brackets [] 
# or by using the get() method.

# print(user_data['name'])  # Accessing value by key
# print(user_data.get('age')) # Accessing value by get() method
# print(user_data.get('is_verified')) # Accessing value by get() method
# print(user_data.get('skills')) # Accessing value by get() method

# Modification & Adding new kay-value pair in a dictionary -> We can modify the value of an existing key 
# or add a new key-value pair in a dictionary by using the assignment operator =.
# profile = {'username': 'rahul_99', 'score': 150}
# profile['score'] = 200
# profile['level'] = 5
# print(profile)

# Deleting a key-value pair from a dictionary -> We can delete a key-value pair from a dictionary by using the del kayword 
# or the pop() method.

# car = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# pop() method -> It removes the specified key and return the corresponding value.
# removed_year = car.pop('year')
# print('Removed Year:', removed_year)
# print('Updated Car Dictionary:', car)

# del keyword -> It removes the specified key-value pair from the dictionary.
# del car['model']
# print('Updated Car Dictionary after deletion:', car)  

# Pro-Level Functions ( keys(), values(), items() ) ->
# These functions are used to retreive the keys, values and key-value pairs from a dictionary.
# student = {'name': 'Priya', 'course': 'Java', 'marks': 90}
# # keys() -> It returns a view object that displays a list of all the keys in the dictionary.
# print(student.keys())
# # values() -> It returns a view object that displays a list of all the values in the dictionary.
# print(student.values())
# # items() -> It returns a view object that diaplays a list of all the key-value pairs in the dictionary as tuples.
# print(student.items())

# Looping through a dictonary -> we can Loop through a dictionary using a for Loop to access its keys, values 
# or key-value pairs.
# for k, v in student.items():
#     print(f'Key was: {k} and value was: {v}')

3 # Task:1
# superhero = {
#     'name': 'Tony Stark',
#     'hero_name': 'Iron Man',
#     'power': 85
# }
# superhero['power'] = 100
# superhero['status'] = 'Active'
# print(superhero)

# for key, value in superhero.items():
#     print(key, '-->', value)

# .popitem() Method -> It removes and returns the last key-value pair from the dictionary as a tuple.
# user = {'name': 'Amit', 'role': 'Admin', 'status': 'Online'}
# last_deleted = user.popitem()
# print('Last Deleted Item:', last_deleted)
# print('Updated User Dictonary:', user)

# # .update() Method -> It is used to update the dictionary with the kay-value pairs from another dictionary 
# # or with key-value pairs provided as keyword arguments.
# dict1 = {'brand': 'Apple', 'model': 'iPhone 15'}
# dict2 = {'color': 'Black', 'storage': '128GB'}
# dict1.update(dict2)
# print('Updated Dict 1:', dict1)

# .setdefault() Method -> This is truly brilliant and hidden method. It says: 'If that key already exists in the dictonary
# fecth its value for me. And the key does not exist , create a new key and insert the default value I have provided.'
# country_code = {'India': '+91', 'USA': '+1'}
# print(country_code.setdefault('India', '+00'))
# print(country_code.setdefault('Japan', '+81'))
# print(country_code)

# Dictionary Comprehension -> Make dictionary in only one line using dictionary comprehension.
# numbers = [1, 2, 3, 4, 5]
# square_dict = {x: x*x for x in numbers}
# print(square_dict)

# .fromkey() Method -> Creating keys for everyone in one go if you need to create a dictonary containing a large number of keys , 
# but want to assign the exact same initial value (default value) to all of them, we use the .fromkeys() method.
# friends = ['Amit', 'Rahul', 'Priya']
# default_status = 'Offline'
# status_dict = dict.fromkeys(friends, default_status)
# print(status_dict)

# Dictionary Copying (.copy())
# original = {'A': 1, 'B': 2}
# backup = original.copy()
# backup['C'] = 3
# print('Origianl:', original)
# print('Backup:', backup)

# Nested Dictionaries
# users = {
#     'user1': {
#         'name': 'Amit',
#         'role': 'admin'
#         },
#         'user2': {
#             'name': 'Rahul',
#             'role': 'User'
#         }

#     }
# print(users['user2']['role'])

# in Operator -> A key - checking tool
# Often , before retrieving data, we need to verify whether a specific key exists within a dictionary.
# the 'in' keyword is used for this purpose.
# It returns a value of either True or False.
# user_status = {'Amit': 'Online', 'rahul': 'Offline'}
# print('Priya' in user_status)
# print('Amit' in user_status)

# clear() Method -> If you want the dictionary to remain in memory , 
# but wish to deleteall the data within it at once (meaning the dictionary becomes completely empty),
# we use .clear() method
# session_data = {'token': 'abc123', 'user_id': 99}
# session_data.clear()
# print(session_data)

# Dictionary Merge(|) and Update (|=) Operator 
# dict_a = {'apple': 1, 'banana': 2}
# dict_b = {'cherry': 3, 'banana': 5}
# # Merge Operator (|) -> This combines both to create an entirely new dictionary.
# my_dict = dict_a | dict_b
# print('New Dict:', my_dict) #In the dictionary written later (dict_b) , the value for 'banana' was overwritten.

# # Update Operator (|=) -> It merges the new data directly into the existing data.
# dict_a |= dict_b
# print('Updated Dict:', dict_a)

# len() Function -> It tells what is the size of dictionary.
# stock = {'items': 50, 'price': 1200, 'discount': 10, 'rating': 4.5}
# total_keys = len(stock)
# print('The total items in the dictionary:', total_keys)

# reversed() Function -> Looping through a dictionary in reverse.
# People often assume that a dictionary can't be looped through in reverse;
# however, if you need  to read the dictionary's element from the end towards the beginning , the reversed() function comes in handy.
# steps = {'step1': 'Login', 'step2': 'Cart', 'step3': 'Payment'}
# for key in reversed(steps):
#     print(key, '->', steps[key])

# type() Function -> It checks that Is it dictionary or not ?
# info = {'id': 101, 'status': 'Success'}
# print(type(info))

# del -> Using the del Keyword to Wipe the entire Memory. We previously learned about del info['key']
# which removes a specific key-value pair. However, 
# if you wish to completely eliminate the entire dictionary container from memory parmanently
#(meaning the variable itself is deleted ) - you can apply the del command to the entire dictionary object.
# temp_data = {'session_id': 'abc123'}
# del temp_data
# print(temp_data) # NameError because now it is not in the compuetr memory

# Identity Operator (is and is not) -> It checks memory address.
# dict_x = {'A': 1}
# dict_y = {'A': 1}
# dict_z = dict_x 
# print(dict_x == dict_y)
# print(dict_x is dict_y)
# print(dict_x is dict_z)

# dict() Function -> make dictionaries using Constructor dict()
# d1 = dict(name='Amit', age=34)
# print(d1)

# pairs = [('apple', 10), ('banana',20)]
# d2 = dict(pairs)
# print(d2)

# Comparison Operator (== and !=)
# dict_a = {'A': 1, 'B':2}
# dict_b = {'B': 2, 'A': 1}
# print(dict_a == dict_b)
# print(dict_a != dict_b)

# Built-in Functions -> max(), min(), any(), all() 
# max() -> It returns the largest key in the dictionary.
# min() -> It returns the smallest key of a dictionary.
# my_dict = {1: 'One', 2: 'Two', 3: 'Three'}
# print(max(my_dict))
# print(min(my_dict))

# all() -> all to all keys are correct.
# This function will return True only if all of the dictionary's keys are True 
# (meaning that no key should be 0, False, None, or an empty string).
# if even a single key is zero or false , it will return False.
# dict1 = {1: 'Apple', 2: 'Banana', 3: 'Cherry'}
# print(all(dict1))

# dict2 = {0: 'Zero Value', 1: 'One Value'}
# print(all(dict2))

# any() -> if even a single key is True , that Works!
# this one is a bit laid-back. It essentially says, I don't care about all the keys;
# if I find even a single key in the entire dictionary that evaluates to True
# i'll happily return True. It will only return False of every single key is either 0 or False.
# dict3 = {0: 'Khali', 1: 'Bhara hua'}
# print(any(dict3))
# dict4 = {0: 'A', False: 'B'}
# print(any(dict4))

# KeyError Exception -> KeyError Exception when you are working with dictionaries and attempt to access a key that does not exist, 
# the error that Python raises is called a KeyError. To avoid this, we use the get() method or the 'in' keyword 
# techniques we have already learned.
# data = {'id': 1}
# print(data['name']) # KeyError

# Dunder Methods: __contains__ and __len__ -> Python's engine executes our keywords in the background as built-in functions.
# when you write 'key in dict' Python internally executes 'dict.__contains__(key)',
# when you write 'len(dict)', Python internally executes 'dict.__len__()'.
# info = {'a': 1, 'b':2}
# print(info.__contains__('a'))
# print(info.__len__())

# Shallow Copy vs Deep Copy -> We have learned about .copy(), which creates a distinct dictionary. 
# however, if a list is nested inside that dictionary(creating a nested dictionary),
# .copy() is unable to create a separate memory address for that inner list. 
# To handle this , Python provides a specific keyword/Module known as 'copy.deepcopy()'.
# import copy 
# original = {'user': 'Amit', 'skill': ['Python', 'SQL']}
# perfect_backup = copy.deepcopy(original)
# perfect_backup['skill'].append('DS')
# print('Original:', original['skill'])
# print('Perfect Backup:', perfect_backup['skill'])

# Sorting a Dictionary -> you previously learned that you can directly sort a list using the 'sort()' method;
# however, sort() does not work directly on dictionaries.
# scores = {'Rahul': 90, 'Amit': 95, 'Priya': 80}
# for key in sorted(scores):
#     print(key, '->', scores[key])

# Double Dictionary Unpacking (** operator)  -> Just as we unpack normal variables, in modern Python,
# the entire data from two dictionaries can be unpacked into a third dictionary in a single line
# without using the .update() method. This is achieved using the (**) double asterisk operator.
# user_info = {'name': 'Amit', 'age': 34}
# user_skills = {'lang': 'Python', 'db': 'SQL'}
# final_profile = {**user_info, **user_skills}
# print(final_profile)

# Duplicate Keys
wrong_dict = {'name': 'Amit', 'age': 20, 'age': 25}
print(wrong_dict)