def patteran(n):
    if (n==0):
        return
    print("*" * n)
    patteran(n-1)

patteran(5)