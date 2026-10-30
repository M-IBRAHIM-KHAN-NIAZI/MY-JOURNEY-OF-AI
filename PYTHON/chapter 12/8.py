try:
    # 1. ZeroDivisionError: Kisi bhi number ko 0 se divide karna
    # x = 10 / 0
    
    # 2. TypeError: Mukhtalif data types ko aapas mein jodna
    # y = "Hello" + 5
    
    # 3. ValueError: Ghalat value pass karna (jaise text ko integer mein convert karna)
    # z = int("abc")
    
    # 4. NameError: Aisi variable ko use karna jo define hi na ho
    print(a)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except TypeError:
    print("Error: Invalid data type operation!")
except ValueError:
    print("Error: Invalid value conversion!")
except NameError:
    print("Error: Variable is not defined!")