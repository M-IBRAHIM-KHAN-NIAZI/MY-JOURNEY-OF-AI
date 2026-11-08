# LeetCode 141: Fast & Slow pointers use karke check karte hain ke Linked List mein cycle (loop) hai ya nahi.

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None  #jo cheez fix rehne hoti ha ose arguments mein nahi likhte or simple estrah likhte

def has_cycle(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if fast==slow:

            return True
    return False    
        
            
        
    
head = Node(3)
n1 = Node(2)
n2 = Node(0)
n3 = Node(-4)   

head.next=n1
n1.next=n2
n2.next=n3

n3.next=n1

result=has_cycle(head)
print(result)

