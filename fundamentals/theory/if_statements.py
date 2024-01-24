# Boolean Variables
is_male = True
is_tall = False

# If Statement with OR Condition
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You're neither a male nor tall")

# Boolean Variables
is_banana = True
is_apple = False

# If-Elif-Else Statements with AND and NOT Conditions
if is_banana and is_apple:
    print("It's a banana and an apple")
elif is_banana and not(is_apple):
    print("It's just a banana")
elif not(is_banana) and is_apple:
    print("It's just an apple")
else:
    print("It's not a banana or not an apple")

# Comparisons
# ==    equal
# !=    not equal
# >     greater than (>= greater than or equal)
# <     less than (<= less than or equal)
# in    text exists within another text
# not   negates the comparison

# Example Program 3
print('Program 1')
user_email = input('Enter your email:')
if not '@' in user_email:
    print('Invalid Email')
else:
    pass
