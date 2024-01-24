
# Title: Python For Loop Examples

# Example 1: Loop through a list of fruits and print each one
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Example 2: Loop through the letters in the word "banana"
for x in "banana":
    print(x)

# Example 3: Use the break statement to exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# Example 4: Use the break statement again, with break before the print statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# Example 5: Use the continue statement to skip printing "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Example 6: Use the range() function to loop through a set of numbers
for x in range(6):
    print(x)

# Example 7: Use the range() function with a start parameter
for x in range(2, 6):
    print(x)

# Example 8: Use the range() function with a start, end, and increment parameter
for x in range(2, 30, 3):
    print(x)

# Example 9: Use the else keyword in a for loop to execute code when the loop is finished
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Example 10: Break the loop when x is 3 and observe the else block behavior
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

# Example 11: Nested loops - Print each adjective for every fruit
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# Example 12: The pass statement in an empty for loop
for x in [0, 1, 2]:
    pass

products = ['iphone', 'galaxy', 'ipad', 'tv', 'coffee machine', 'kindle', 'refrigerator', 'wine cellar', 'dell laptop', 'hp laptop', 'asus laptop', 'microsoft surface', 'webcam', 'speaker', 'microphone', 'canon camera']
sales2019 = [558147, 712350, 573823, 405252, 718654, 531580, 973139, 892292, 422760, 154753, 887061, 438508, 237467, 489705, 328311, 591120]
sales2020 = [951642, 244295, 26964, 787604, 867660, 78830, 710331, 646016, 694913, 539704, 324831, 667179, 295633, 725316, 644622, 994303]

for i in range(len(products)):
    product = products[i]
    sale2019 = sales2019[i]
    sale2020 = sales2020[i]

    if sale2020 > sale2019:
        percentage = ((sale2020 - sale2019) / sale2019) * 100
        print(f"{product}: {sale2019} -> {sale2020} (sales increase: {percentage:.2f}%)")
    elif sale2020 < sale2019:
        percentage = ((sale2019 - sale2020) / sale2019) * 100
        print(f"{product}: {sale2019} -> {sale2020} (sales decrease: {percentage:.2f}%)")
    else:
        print(f"{product}: {sale2019} -> {sale2020} (no change in sales)")
