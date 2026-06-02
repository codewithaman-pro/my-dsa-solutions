# HOW TO CREATE A LIST
# friends = ['Amit', 'Rahul', 'Priya', 'Sneha']
# print(friends)

# HOW TO RETRIEVE DATA FROM LIST (INDEXING)
# friends= ['Amit', 'Rahul', 'Priya', 'Nick',]
# print(friends[0])
# print(friends[2])
# print(friends[-1])

# HOW TO MODIFY IN LIST
# friends = ['Amit', 'Rahul', 'Riya', 'Pappu']
# friends[1]='Rohit'
# print(friends)

# appliances = ['Light: OFF', "Fan: ON", 'AC: OFF', 'TV: OFF']
# appliances[2] = 'AC: ON'
# print('Updated Appliances:' , appliances)


# BY SLICING
# marks = [75, 45, 40, 90, 88]
# marks[1:3] = [82, 85]
# print('Updated Marks:' , marks)

# APPEND(element) -> ADD AT THE END WITHOUT DISRUPT ANY VALUES
# todo_list = ['Gym', 'Red Book', 'Code']
# todo_list.append('Groceries')
# print("After Append:", todo_list)

# INSERT(index, element) -> Make space in between two or more values
# players = ['Kohli', 'Rohit', 'Rahul', ]
# players.insert(1, 'Gill')
# print('After Insert:' , players)

# ADD ANOTHER LIST IN FIRST LIST
#extend() -> while remaining at the same memory locatin as the original list, 
# it appends(add) all the elements of the second list to the first list, one by one. 
# No new list is created in memory.
# batch_a = ['Amit', 'Sumit']
# batch_b = ['Rohit', 'Monu']
# batch_a.extend(batch_b)
# print('Batch A after extend:', batch_a)

# + OPERATOR(Concatenation) -> It adds two lists but it doesn't change in first list.
# It makes exactly a new third list in memory 
# list_x = [1,2]
# list_y = [4,5]
# combined_list = list_x + list_y
# print('Combined:', combined_list)
# print('Original_list:', list_x)

# Example append() vs extend()
# my_data = [10, 20, 30]
# my_data.append([40,50])
# print('After append:',my_data)
# my_data = [10,20,30]
# my_data.extend([40,50])
# print('After extend:',my_data)

# HOW TO DELETE FROM A LIST 
# remove(), pop(), clear()
# 1. remove(value) -> when you know name but not index ->
# if two items in list then remove() removes only first item and remaining second item
# playlist = ['Song A', 'Song B', 'Song C', 'Song B']
# playlist.remove('Song B')
# print('After Remove:', playlist)
 
# 2. pop(index) -> when you know index position.
# If index is not provided, it removes the last item from the list and retuirns it.
# cart = ['Mobile', 'Laptop', 'Watch']
# deleted_item = cart.pop(1)
# print('Deleted item was:', deleted_item)
# print('Updated Cart:', cart)

# 3. clear() -> It removes all the items from the list and makes it empty.
# session_users = ['Amit', 'Rahul', 'Priya']
# session_users.clear() 
# print('After Clear:', session_users)

# difference between clear() vs del
# list_a = [1,2,3]
# list_b = [5,6,7]
# list_a.clear()
# print(list_a)
# del list_b
# print(list_b) # This will raise an error because list_b is deleted from memory and no longer exists.

# Example
# my_friends = ['Amit', 'Rahul', 'Priya', 'Sneha']
# my_friends.pop(3)
# print('Poped:', my_friends)

# LIST SLICING -> It is used to retrieve a portion of the list by specifying a range of indices.
# Formula: list[start : stop : step]
# numbers = [1,2,3,4,5,6,7]
# sub_list1 = numbers[2:5]
# print(sub_list1)
# sub_list2 = numbers[:4]
# print(sub_list2)
# sub_list3 = numbers[3:]
# print(sub_list3)
# print(numbers[::2])
# # 2. Reverse Slicing
# print(numbers[::-1])
# print(numbers[5:1:-1])
# print(numbers[1:6:2])
# print(numbers[::3])
# print(numbers[0:6:3])

# List Reversal & Sorting: sort() vs sorted(list)
# 1. sort() -> It sorts the list in  place and changes the original list.
# marks = [40, 30, 50, 20]
# marks.sort()
# print('Sorted marks:', marks)
# 2. sorted() -> It returns a new sorted list and does not change the original list.
# ages = [23, 18, 26, 22]
# new_ages = sorted(ages)
# print('Sorted ages:', new_ages)
# print('Original ages:', ages)

# list_x = [1, 2, 3]
# list_y = list_x
# list_y.append(99)
# print('List Y:', list_y)
# print('List_X:', list_x)

# HOW TO MAKE REAL COPY OF A LIST USING SLICING
# LIST_X = [1, 2, 3]
# LIST_Y = LIST_X[:]
# LIST_Y.append(88)
# print('LIST_Y:', LIST_Y)
# print('LIST_X:', LIST_X)

# TASK: COPYING CHECK KRNA
# my_original = ['A', 'B', 'C',]
# my_backup = my_original[:]
# my_backup.append('D')
# print('Original :', my_original)
# print('Backup:', my_backup)

# LIST COMPREHENSION -> It is a concise way to create a list using a old list without using loops.
# Normal Method
# numbers = [1, 2, 3, 4, 5]
# squares = []
# for x in numbers:
#     squares.append(x**2)
# print(squares)

# Pro Method
# numbers = [1, 2, 3, 4, 5]
# squares = [x * x for x in numbers]
# print(squares)

# Pro Method with condition
# numbers = [1, 2, 3, 4, 5]
# even_squares = [x*x for x in numbers if x % 2 == 0]
# print(even_squares)

# Nested List Comprehension -> It is used to create a list of lists using list comprehension.
# matrix = [
#     [1, 2, 3], # Row 0
#     [4, 5, 6], # Row 1
#     [7, 8, 9]  # Row 2
#     ]
# print(matrix[1][1]) # Output 5
# print(matrix[2][2]) # Output 9


# zip() and enumerate() functions
# enumerate() -> We need loop with index
# fruits = ['Apple', 'banana', 'Mango']
# for index, fruit in enumerate(fruits):
#     print(f'Index: {index}, Fruit: {fruit}')

# zip() -> We need to Loop through two or more lists together
names = ['Amit', 'Rahul', 'Priya']
ages = [25, 34, 38]
for name, age in zip(names, ages):
    print(f'Name: {name}, Age: {age}')

