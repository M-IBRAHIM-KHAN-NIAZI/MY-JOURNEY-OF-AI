# A list of numbers
l = [2, 35, 12, 45, 60, 33, 10]

# Function to check if a number is divisible by 5
def divisible_by_5(num):
    if num % 5 == 0:
        return True
    return False

# Using filter
result = list(filter(divisible_by_5, l))
print(result)