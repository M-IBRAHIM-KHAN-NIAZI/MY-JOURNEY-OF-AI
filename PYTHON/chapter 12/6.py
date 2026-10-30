try:
    # 1. Yeh ZeroDivisionError dega (agar b = 0 ho)
    # a = 10 / 0  
    
    # 2. Yeh TypeError dega (string aur integer ko plus nahi kar sakte)
    result = "Hello" + 5  

# except ZeroDivisionError:
    # print("Error: Cannot divide by zero!")

except TypeError:
    print("Error: Invalid data type operation!")

except Exception as e:
    print(f"An unexpected error occurred: {e}")