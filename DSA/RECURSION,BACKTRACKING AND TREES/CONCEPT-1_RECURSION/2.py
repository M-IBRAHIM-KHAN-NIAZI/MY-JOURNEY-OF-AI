#(Pow(x, n) - LC 50)
def myPow(x, n):
    if n<0:
        x=1/x
        n=-n

    def helper(x,n):
            if n==0:
                return 1

            half=helper(x,n // 2)

            if n%2==0:
                return half * half
            else:
                return x * half * half

    return helper(x,n)

print(myPow(2,5))        



