# dictionary is a cheangeable,unordered collection of unique key:value pairs
#fast because they use hashing, allow us to acess a value quickly

# Python Dictionary Basics

# Creating a Dictionary
my_dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("Original Dictionary:")
print(my_dict)

# Accessing Elements
print("\nAccessing a value using key:")
print(my_dict['name'])
#or 
print("\nAccessing a value using key:")
print(my_dict.get('name'))

# Adding Elements
my_dict[4] = 'Python'
print("\nDictionary after adding an element:")
print(my_dict)

# Accessing Elements of a Nested Dictionary
nested_dict = {'Dict1': {1: 'Geeks'}, 'Dict2': {'Name': 'For'}}
print("\nAccessing a nested dictionary:")
print(nested_dict['Dict1'])
print(nested_dict['Dict1'][1])
print(nested_dict['Dict2']['Name'])

# Deleting Elements
del my_dict[1]
print("\nDictionary after deleting an element:")
print(my_dict)

# Dictionary Methods

# keys() - Returns a list containing all the keys of the dictionary
print("\nDictionary Keys:")
print(my_dict.keys())

# values() - Returns a list containing all the values of the dictionary
print("\nDictionary Values:")
print(my_dict.values())

# items() - Returns a list of tuples, where each tuple contains a key-value pair from the dictionary
print("\nDictionary Items:")
print(my_dict.items())

# Clearing the Dictionary
my_dict.clear()
print("\nDictionary after clearing all elements:")
print(my_dict)
