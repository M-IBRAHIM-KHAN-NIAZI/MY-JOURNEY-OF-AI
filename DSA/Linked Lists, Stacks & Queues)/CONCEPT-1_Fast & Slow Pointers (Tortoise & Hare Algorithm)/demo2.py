# 1. Dabbe ka blueprint (VS Code mein Node batane ke liye)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# 2. Cycle check karne ka sabse simple function
def has_cycle(head):
    slow = head
    fast = head
    
    # Jab tak fast aur fast ka agla dabba mojood hai (Safety check)
    while fast and fast.next:
        slow = slow.next          # Slow chala 1 step aage
        fast = fast.next.next     # Fast chala 2 steps aage
        
        # Agar dono pointers same memory address par mil gaye
        if slow == fast:
            return True           # Cycle mil gayi!
            
    return False                  # List khatam ho gayi, koi cycle nahi hai


# --- LOCAL TESTING (LeetCode Example 1) ---
# List banai: 3 -> 2 -> 0 -> -4
n1 = Node(3)
n2 = Node(2)
n3 = Node(0)
n4 = Node(-4)

# Inhein aapas mein jodh diya
n1.next = n2
n2.next = n3
n3.next = n4

# Cycle banai: aakhri node (-4) ko wapas n2 (value 2) se jodh diya
n4.next = n2

# Function call kiya
result = has_cycle(n1)#sirf head matlab starting point dena hota
print(result)  # Output: True aayega!