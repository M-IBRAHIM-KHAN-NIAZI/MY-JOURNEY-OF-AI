# LeetCode 876: Fast & Slow pointers use karke Linked List ka middle node find karna.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def middle_node(head):
    slow = head
    fast = head
    
    # Jab tak fast aur uska agla dabba mojood hai
    while fast and fast.next:
        slow = slow.next          # Slow chala 1 step
        fast = fast.next.next     # Fast chala 2 steps
        
    # Jab fast end par hoga, slow exact middle par hoga!
    return slow


# --- LOCAL TESTING ---
# List banai: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)

# Line se joda
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

# Function call kiya
result = middle_node(head)
print(result.value)  # Output: 3 (Kyunki 3 beech wala node hai!)