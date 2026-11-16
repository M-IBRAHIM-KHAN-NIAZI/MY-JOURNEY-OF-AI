#LEET CODE 20:VALID BRACKETS
class solution:
    def isValid(self,s):
        stack=[]
        mapping = {")": "(", "}": "{", "]": "["}

        for characters in s:
            if characters in mapping:
                top_element=stack.pop() if stack else "#"

                if mapping[characters]!=top_element:
                    return False
            else:
                stack.append(characters)

        return not stack        


        
if __name__ == "__main__":
    sol = solution()
    print(f"Test 1 '()[]{{}}' (Expect True): {sol.isValid('()[]{}')}")
    print(f"Test 2 '(]' (Expect False): {sol.isValid('(]')}")
    print(f"Test 3 '([)]' (Expect False): {sol.isValid('([)]')}")