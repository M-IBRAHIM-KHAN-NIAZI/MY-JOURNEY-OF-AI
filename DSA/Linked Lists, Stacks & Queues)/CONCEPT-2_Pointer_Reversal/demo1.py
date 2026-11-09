# LeetCode 206: Reverse Linked List (Simplest Approach)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Tail: Aakhri node kisi se join nahi hota

def reverse_list(head):
    prev = None       # Shuru mein prev ko None rakhte hain
    current = head    # Current pointer shuruwati node par hoga
    
    while current is not None:
        # Step 1: Agla rasta save karo taake connection tootne par khoye na
        next_node = current.next
        
        # Step 2: Connection ulta kar do (aage jane ke bajaye peechhe jodh do)
        current.next = prev
        
        # Step 3: Dono pointers ko ek-ek step aage khiska do
        prev = current
        current = next_node
        
    # Jab loop khatam hoga, toh 'prev' naya head ban chuka hoga
    return prev

# --- Local Testing ---
head = Node(1)
n1 = Node(2)
n2 = Node(3)

# List banayi: 1 -> 2 -> 3 -> None
head.next = n1
n1.next = n2

# Function call karke list reverse ki
new_head = reverse_list(head)

# Check karne ke liye print kiya
print(new_head.value)       # Output: 3 (Ab naya head 3 hai)
print(new_head.next.value)  # Output: 2