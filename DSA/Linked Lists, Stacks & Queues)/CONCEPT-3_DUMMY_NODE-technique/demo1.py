class ListNode:

  def __init__(self, value):
    self.value = value
    self.next = None


class Solution: #you can write code without making this class and we write self in def just beacuse the function is 
                                                               #in class
  def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode: #we are using here type hints we can write code
    # ----------------------------------------------------------------- without it if you want
    # STEP 1: DUMMY NODE SETUP (The Permanent Anchor & Builder)
    # -----------------------------------------------------------------
    # Ek farzi dabba (-1) bana liya taake nayi list ka Head kabhi khoye na.
    # Yeh hamara permanent anchor ban jata hai.
    dummy = ListNode(-1)

    # 'tail' ek working pointer hai jo shuru mein dummy par khada hai
    # aur hamesha nayi list ke aakhri dabbe (tail) par nazar rakhta hai.
    tail = dummy

    # -----------------------------------------------------------------
    # STEP 2: COMPARISON LOOP (Dabbay aapas mein compare karna)
    # -----------------------------------------------------------------
    # Jab tak dono lists mein dabbe bache hain, chhota dabba select karo.
    while list1 is not None and list2 is not None:
      if list1.val <= list2.val:
        tail.next = list1  # List 1 ka dabba chhota hai, usko aage jodh do
        list1 = list1.next  # List 1 ko ek kadam aage badha do or khiska do as we have to do in while loop
      else:
        tail.next = list2  # List 2 ka dabba chhota hai, usko aage jodh do
        list2 = list2.next  # List 2 ko ek kadam aage badha do

      # Builder (tail) ko aage khiska kar naye jude hue dabbe par le aao
      tail = tail.next

    # -----------------------------------------------------------------
    # STEP 3: HANDLING LEFTOVERS (Bache hue dabbe seedha jodh do)
    # -----------------------------------------------------------------
    # Agar ek list khatam ho gayi aur doosri mein abhi bhi dabbe bache hain,
    # toh unhe ek-ek karke check karne ki zaroorat nahi. Poori ki poori list
    # seedha tail ke aage utha kar laga do!
    if list1 is not None:
      tail.next = list1
    else:
      tail.next = list2

    # -----------------------------------------------------------------
    # STEP 4: THE FINAL ESCAPE (Returning the Real List)
    # -----------------------------------------------------------------
    # Farzi dabbe (-1) ko peechhe chhod do, aur uske aage wali asli nayi
    # sorted list (dummy.next) ko wapas return kar do!
    return dummy.next