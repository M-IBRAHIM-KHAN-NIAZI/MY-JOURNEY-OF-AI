from functools import reduce

l = [3, 56, 12, 89, 23, 7]

# Function to return the maximum of two numbers
def greater(a, b):
    if a > b:
        return a
    return b

# Using reduce
max_num = reduce(greater, l)
print("The maximum number is:", max_num)