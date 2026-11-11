class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
  # Step 1: Dummy node banao aur usko asli list ke sath jod do (Safety Shield)
  dummy = ListNode(0)
  dummy.next = head

  # Step 2: Dono pointers (slow aur fast) ko dummy par khada karo
  slow = dummy
  fast = dummy

  # Step 3: Fast pointer ko (n + 1) steps aage bhej do taake gap ban jaye
  for _ in range(n + 1):#n basically problem ke shru mein diya hota ha numbers ki shakal mein e.g agr 2 diya huga eska
    fast = fast.next    #matlab ha end se 2nd last digit skip karna ha or delete karna ha or end se 1 se hi counting 
                        #shru huye gi
                        # one more thing range(3) or range(0,3)ek hi baat hoti ha python kafi smart hota 
  # Step 4: Dono ko tab tak aage chalao jab tak fast aakhir (None) par na pahunch jaye
  while fast is not None:
    slow = slow.next
    fast = fast.next

  # Step 5: Target node ko bypass (delete) kar do
  slow.next = slow.next.next

  # Step 6: Dummy ke aage wali asli list return kar do
  return dummy.next