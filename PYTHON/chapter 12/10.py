def func1():
    try:
        l = [1, 5, 6, 3]
        i = int(input("Enter the index: "))
        print(l[i])
        return 
    except Exception as e:
        print(f"Some error occurred: {e}")
        return 
    finally:
        print("I am always executed")

x = func1()
print(x)

