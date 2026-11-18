###(Implement Queue using Stacks - LC 232) ###
class MyQueue:

    def __init__(self):
        self.input_stack = []   # Naye elements yahan append honge (Push ke liye)
        self.output_stack = []  # Elements yahan se pop/peek honge (FIFO order ke liye)

    def push(self, x: int) -> None:
        # Naye element ko hamesha input stack mein daal do
        self.input_stack.append(x)

    def pop(self) -> int:
        # Pehle ensure karo ke output stack mein elements available hon
        self._move()
        return self.output_stack.pop()

    def peek(self) -> int:
        # Queue ke sabse pehle element ko bina remove kiye dekhna
        self._move()
        return self.output_stack[-1]

    def empty(self) -> bool: #we use it as a safety to prevent error
        # Agar dono stacks khali hain, toh queue bhi khali hai
        return not self.input_stack and not self.output_stack

    def _move(self):
        # Helper function: Agar output stack khali hai, toh input ke saare elements 
        # ulta karke output stack mein daal do (LIFO ko FIFO mein badalne ka jaadu)
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

 # --- Local Testing Block ---
if __name__ == "__main__":
    q = MyQueue()
    
    q.push(10)
    q.push(20)
    q.push(30)
    
    print("Peek element (10 expected):", q.peek())
    print("Popped element (10 expected):", q.pop())
    
    q.push(40)
    
    print("Peek element after push (20 expected):", q.peek())
    print("Is queue empty? (False expected):", q.empty())

