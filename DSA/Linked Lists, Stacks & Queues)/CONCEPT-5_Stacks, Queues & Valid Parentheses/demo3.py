### (Evaluate Reverse Polish Notation - LC 150) ###
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []  # Numbers ko store karne ke liye khali stack
        
        for token in tokens:
            if token == "+":
                b = stack.pop()  # Doosra number jo pehle bahar aaya
                a = stack.pop()  # Pehla number jo baad mein bahar aaya
                stack.append(a + b)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                # int() use karte hain taaki division zero ki taraf truncate ho (jaise LC mangta hai)
                stack.append(int(a / b)) #we use int() instead of float division cuz in that if when we have suppose -5/-2
                #  anwer is -2.5 but it goes to -3 but in int() it will go to -2 what we need in  this problem     
            else:
                # Agar token operator nahi hai, toh matlab wo number hai (string se integer bana kar stack mein daalo)
                stack.append(int(token))
                
        # Aakhir mein stack ke andar sirf ek hi final answer bacha hoga
        return stack[0]

# --- Local Testing Block ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: ["2", "1", "+", "3", "*"] -> (2 + 1) * 3 = 9
    tokens1 = ["2", "1", "+", "3", "*"]
    print("Test 1 Result (9 expected):", sol.evalRPN(tokens1))
    
    # Test Case 2: ["4", "13", "5", "/", "+"] -> 4 + (13 / 5) = 4 + 2 = 6
    tokens2 = ["4", "13", "5", "/", "+"]
    print("Test 2 Result (6 expected):", sol.evalRPN(tokens2))    