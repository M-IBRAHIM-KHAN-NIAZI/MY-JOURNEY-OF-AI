#LeetCode 206: Reverse Linked List (Simplest Approach)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse(head):
    prev=None
    current=head

    while current is not None:
        next_node=current.next

        current.next=prev

        prev=current
        current=next_node
    return prev
    

head = Node(1)
n1 = Node(2)
n2 = Node(3)

# List banayi: 1 -> 2 -> 3 -> None
head.next = n1
n1.next = n2 

new_head=reverse(head)
print(new_head.value)