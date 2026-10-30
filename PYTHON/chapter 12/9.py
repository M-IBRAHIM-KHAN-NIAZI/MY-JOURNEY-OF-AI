a=int(input("enter your number ibrahim khan niazi: "))
b = int(input("Enter second number: "))


if b == 0:
        raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
        print(f"The division a/b is {a/b}")