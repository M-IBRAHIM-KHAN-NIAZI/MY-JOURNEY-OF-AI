##(Pow(x, n) - LC 50)
def myPow(x, n):
    # Agar power negative ho toh x ko ulta (1/x) aur n ko positive kar do
    if n < 0:
        x = 1 / x
        n = -n

    def helper(x, n):
        # Base Case: kisi bhi number ki power 0 ho toh jawab 1 hota hai
        if n == 0:
            return 1.0

        # Recursive Step: power ko aadha (n // 2) karke neeche bhejo
        half = helper(x, n // 2)

        # Unwinding: agar n even hai toh half * half, odd hai toh ek x extra
        if n % 2 == 0:# esme phela number andr jata ha dosra bahir rehta ha OR % module hame remainder deta ha
            return half * half
        else:
            return x * half * half

    return helper(x, n)


print(myPow(2.0, 5))   # Output: 32.0
print(myPow(2.0, -2))  # Output: 0.25