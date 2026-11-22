def removeKdigits(num: str, k: int) -> str:
    stack = []  # Digits ko increasing order mein rakhega

    for digit in num:
        # Jab tak stack khali na ho, k > 0 ho, aur current digit top se chota ho,
        # tab tak top wale bare digit ko remove (pop) karte raho
        while stack and k > 0 and digit < stack[-1]:
            stack.pop()
            k -= 1

        stack.append(digit)

    # Agar abhi bhi k digits hatane baaki hain, toh end se k digits kaat do
    if k > 0:
        stack = stack[:-k]

    # Leading zeros hatao; agar kuch na bache toh "0" return karo
    result = "".join(stack).lstrip("0")
    return result if result else "0"

# Sabse simple local testing
print(removeKdigits("1432219", 3))  # 1219
print(removeKdigits("10200", 1))    # 200
print(removeKdigits("10", 2))       # 0
print(removeKdigits("12345", 2))    # 123