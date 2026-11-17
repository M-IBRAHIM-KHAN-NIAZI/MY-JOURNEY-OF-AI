 #(Min Stack - LC 155)
class min_stack:
    def __init__(self):
        self.stack=[]
        self.stack_min=[]

    def push (self,val):
        self.stack.append(val) 
        if not self.stack_min or val <= self.stack_min[-1]:
            self.stack_min.append(val)  
        else:
            self.stack_min.append(self.stack_min[-1])

    def pop(self):
        self.stack.pop()
        self.stack_min.pop()

    def top (self) :
        return self.stack[-1]

    def minstack(self):
        return self.stack_min[-1]



# --- Local Testing Block ---
if __name__ == "__main__":
    obj = min_stack()
    
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    
    print("Minimum element (-3 expected):", obj.minstack())
    
    obj.pop()
    
    print("Top element after pop (0 expected):", obj.top())
    print("Minimum element after pop (-2 expected):", obj.minstack())
    

        
