### (Evaluate Reverse Polish Notation - LC 150) ###
class solution:
    def RPN (self,tokens):
        stack=[]

        for token in tokens:
            if token == "+":
                b=stack.pop()
                a=stack.pop()
                stack.append(a+b)
            elif token== "-" :
                b=stack.pop()
                a=stack.pop()
                stack.append(a-b)
            elif token== "*" :
                b=stack.pop()
                a=stack.pop()
                stack.append(a*b)
            elif token== "/" :
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(token))    
        return stack[0]        
if __name__ == "__main__":
    sol = solution()
    
    # Test Case 1: ["2", "1", "+", "3", "*"] -> (2 + 1) * 3 = 9
    tokens1 = ["2", "1", "+", "3", "*"]
    print("Test 1 Result (9 expected):", sol.RPN(tokens1))
    
    # Test Case 2: ["4", "13", "5", "/", "+"] -> 4 + (13 / 5) = 4 + 2 = 6
    tokens2 = ["4", "13", "5", "/", "+"]
    print("Test 2 Result (6 expected):", sol.RPN(tokens2))  
    



                
