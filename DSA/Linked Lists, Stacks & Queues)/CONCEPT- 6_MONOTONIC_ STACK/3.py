##(Remove K Digits - LC 402) ##
def removeKdigits(num: str, k: int) -> str:
    stack=[]

    for digit in num:
        while stack and k>0 and digit<stack[-1]:
            stack.pop()
            k-=1
        stack.append(digit)

    if k>0:
        stack=stack[:-k]  

    result="".join(stack).lstrip('0')
    return result if result else "0"

print(removeKdigits("1432219", 3))  # 1219
print(removeKdigits("10200", 1))    # 200
print(removeKdigits("10", 2))       # 0
print(removeKdigits("12345", 2))    # 123           
