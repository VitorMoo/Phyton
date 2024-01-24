"strings in phyton"

# Basic string operations
phrase = "hello world"
print(phrase)
print(phrase + " again")

# Case manipulation
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())

# Length and indexing
print(len(phrase))
print(phrase[0])

# String methods
print(phrase.index("w"))
print(phrase.replace("world", "folks"))


# Stripping whitespace
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

# Splitting a string
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']


# Searching in strings
txt = "The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)

# Slicing strings
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])



# Escaping single quotes
single_quoted_string = 'It\'s a beautiful day.'
print(single_quoted_string)

# Escaping double quotes
double_quoted_string = "She said, \"Hello!\""
print(double_quoted_string)

# Newline character
multiline_string = "This is a line.\nThis is a new line."
print(multiline_string)

# Tab character
tabbed_string = "This is\ttabbed."
print(tabbed_string)

# Backslash itself
backslash_string = "This is a backslash: \\"
print(backslash_string)


# Using f-string
revenue = 2000
cost = 500
profit = revenue - cost
print(f"The revenue was {revenue}. The store's cost was {cost}. The store's profit was {profit}")

# String formatting
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
