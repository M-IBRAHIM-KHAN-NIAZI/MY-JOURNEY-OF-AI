# ==========================================
# LeetCode 19: Remove Nth Node From End of List
# ==========================================

class listnode:
    def __init__(self,value):
        self.value=value
        self.next=None

    def remove_n(head,n):
        dummy=listnode(-1)
        dummy.next=head

        slow=dummy
        fast=dummy

        for _ in range(n+1):
            fast=fast.next

        while fast is not None:
            slow=slow.next
            fast=fast.next

        slow=slow.next.next
        return dummy.next            