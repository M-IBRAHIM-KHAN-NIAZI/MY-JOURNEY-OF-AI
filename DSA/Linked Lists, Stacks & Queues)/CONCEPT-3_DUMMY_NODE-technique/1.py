# LeetCode 21 - Merge Two Sorted Lists
class ListNode:
    def __init__(self,value):
        self.value=value
        self.next=None

def mergedlists(list1,list2):
    dummy=ListNode(-1)
    tail=dummy

    while list1 is not None and list2 is not None:
        if list1.value<=list2.value:
            tail.next=list1
            list1=list1.next
        else:
            tail.next=list2
            list2=list2.next

    tail=tail.next        

    if list1 is not None:
        tail.next=list1
    else:
        tail.next=list2       
    return dummy.next  
       

        
