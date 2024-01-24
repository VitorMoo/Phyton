"""Data types"""

# Variable Declaration and Data Types
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


# Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# Convert from int to float
a = float(x)

# Convert from float to int
b = int(y)

# Convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Basic Arithmetic Operations
revenue = 2000
cost = 500
profit = revenue - cost

# Using the .format method
print("The store's revenue was {}. The store's cost was {}. The store's profit was {}"
    .format(revenue, cost, profit))

# Using f-string
print(f"The revenue was {revenue}. The store's cost was {cost}. The store's profit was {profit}")


# Changing Variable Types
revenue = int(input("Enter revenue:"))
cost = int(input("Enter cost:"))

profit = revenue - cost
print(profit)


# Type of Variables in Python
revenue = 1000
print(type(revenue))

revenue = 1000.00
print(type(revenue))

revenue = '1.000'
print(type(revenue))

receives_bonus = True
print(type(receives_bonus))


# Additional Type Conversion Examples
# Convert string to integer
num_str = "123"
num_int = int(num_str)

# Convert float to string
pi = 3.14
pi_str = str(pi)

# Convert boolean to string
is_python_fun = True
is_python_fun_str = str(is_python_fun)

print(num_int)
print(pi_str)
print(is_python_fun_str)

# Convert string to float
temperature_str = "25.5"
temperature_float = float(temperature_str)

print(temperature_float)


# Type Inference in Python
# Python is dynamically typed, meaning you don't need to explicitly declare the type of a variable
dynamic_type_example = 42
print(type(dynamic_type_example))

dynamic_type_example = "Hello, Python!"
print(type(dynamic_type_example))


# Complex Numbers
# Complex numbers have a real and imaginary part
complex_num = 2 + 3j
print(complex_num)

# Access real and imaginary parts
real_part = complex_num.real
imag_part = complex_num.imag

print(f"Real Part: {real_part}, Imaginary Part: {imag_part}")
