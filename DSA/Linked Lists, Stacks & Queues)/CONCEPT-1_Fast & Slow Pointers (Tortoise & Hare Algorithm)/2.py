# LeetCode 876: Fast & Slow pointers use karke Linked List ka middle node find karna.

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

def middle_node(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

        
            
        
    
head = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n4=Node(5)   #jab even numbers hu tu 2 middle number hote or python second middle number return karta ha


head.next=n1
n1.next=n2
n2.next=n3
n3.next=n4



result=middle_node(head)
print(result.value) # `result` print karne par sirf memory address milta hai (jaise <__main__.Node object>), 
# isliye node ke andar ki asal value dekhne ke liye `result.value` likhte hain.
