# Python Tuple Basics
#useful to group together related data,unchangeable.

# Creating Python Tuples
var = ("Geeks", "for", "Geeks")
print(var)
# Output: ('Geeks', 'for', 'Geeks')

values = (1, 2, 4, "Geek")
print(values)
# Output: (1, 2, 4, 'Geek')

tuple_constructor = tuple(("dsa", "development", "deep learning"))
print(tuple_constructor)
# Output: ('dsa', 'development', 'deep learning')

# Immutable in Tuples
# Tuples are ordered, immutable, and allow duplicate values.

# Accessing Values in Tuples
var = ("Geeks", "for", "Geeks")
print("Value in Var[0] = ", var[0])
# Output: Value in Var[0] =  Geeks

var = (1, 2, 3)
print("Value in Var[-1] = ", var[-1])
# Output: Value in Var[-1] =  3

# Operations on Tuples
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
print(tuple1 + tuple2)
# Output: (0, 1, 2, 3, 'python', 'geek')

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
tuple3 = (tuple1, tuple2)
print(tuple3)
# Output: ((0, 1, 2, 3), ('python', 'geek'))

tuple3 = ('python',) * 3
print(tuple3)
# Output: ('python', 'python', 'python')

tuple1 = (0, 1, 2, 3)
print(tuple1[1:])
# Output: (1, 2, 3)

tuple3 = (0, 1)
del tuple3
# After deletion, accessing tuple3 will result in a NameError

tuple2 = ('python', 'geek')
print(len(tuple2))
# Output: 2

tuple_obj = ("immutable", True, 23)
print(tuple_obj)
# Output: ('immutable', True, 23)

list1 = [0, 1, 2]
print(tuple(list1))
# Output: (0, 1, 2)

tup = ('geek',)
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)
# Output: Prints nested tuples in a loop
    

#enumerate creating a tuple

sells=[1000,2000,3000,150]                  # creating lists
employees=['john','ana','mary','michael']

for i in enumerate(sells):
    print(i)
