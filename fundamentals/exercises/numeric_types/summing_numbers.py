def my_sum(*args):# * allows a function to receive zero or more positional arguments
    total=0         
    for i in args:
        total+=i
    return total


print(my_sum(1,8))