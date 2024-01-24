# List Declaration
numbers = [1, 2, 3, 4, 5, 6]

# Print the Entire List
print(numbers)

# Accessing Elements
print(numbers[2])       # Print the element at index 2
print(numbers[1:])      # Print elements from index 1 to the end
print(numbers[1:4])     # Print elements from index 1 to 3 (4 not included)

# Modifying List
numbers[1] = 100       # Modifying the element at index 1
print(numbers[1])

# List Functions
friends = ["jim", "mike", "dwight", "pam", "carl"]

# Print Friends List
print(friends)

# List Concatenation
friends.extend(numbers) # Add the entire 'numbers' list at the end
print(friends)

# Append Single Element
friends.append("vitor") # Add a single element at the end of the list
print(friends)

# Insert Element at Specific Index
friends.insert(2, "kelly")  # Insert "kelly" at index 2
print(friends)

# Remove Element
friends.remove(100)    # Remove the element with the value 100
print(friends)

# Remove Last Element
friends.pop()
print(friends)

# List Methods
print(friends.index("jim"))  # Show the position of "jim" in the list
print(friends.count("mike")) # Show how many times "mike" appears

# Copying a List
friends2 = friends.copy()
print(friends2)

# Clearing the List
friends.clear()        # Remove all elements from the list
print(friends)

# Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Accessing element in the second row, third column

# Sorting a List
fruits = ["apple", "banana", "orange", "kiwi"]
fruits.sort()
print(fruits)

# Reversing a List
fruits.reverse()
print(fruits)

# List Slicing with Steps
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Using `in` to Check Membership
print("apple" in fruits)  # Check if "apple" is in the list
