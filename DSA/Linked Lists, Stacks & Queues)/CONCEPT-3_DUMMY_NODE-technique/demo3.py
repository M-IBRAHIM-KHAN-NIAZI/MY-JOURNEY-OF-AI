# ==========================================
# LeetCode 86: Partition List (Example 1)
# ==========================================


class listnode:

  def __init__(self, value=0, next=None):
    self.value = value
    self.next = next


def partition(head, x):
  # 1. Do farzi (dummy) lists banate hain:
  # - less_dummy: x se chote numbers ke liye (< x)
  # - greater_dummy: x se bade ya barabar numbers ke liye (>= x)
  less_dummy = listnode(0)
  greater_dummy = listnode(0)

  # Pointers jo aage chal kar nayi lists banayenge
  less = less_dummy
  greater = greater_dummy

  current = head

  # 2. Asli list par loop chala kar nodes ko alag-alag baant lo
  while current is not None:
    if current.value < x:
      less.next = current  # Agar value choti hai, less list mein jodh do
      less = less.next
    else:
      greater.next = current  # Agar value badi/barabar hai, greater list mein jodh do
      greater = greater.next
    current = current.next

  # 3. Bade list ke aakhir mein None lagana zaroori hai taake cycle na bane
  greater.next = None

  # 4. Choti list ke aakhir mein badi list ko jodh do
  less.next = greater_dummy.next# Choti list ke aakhir ko badi list ki poori chain (head) 
                                #se jodh do (pehla node judne se poori list sath aa jati hai)


  # 5. Final updated list wapas return kar do
  return less_dummy.next# 'less_dummy' ek placeholder/dummy node hai, isliye '.next' use karte hain 
# taake dummy ko chhod kar asli required elements wali original list mil jaye.


# ==========================================
# SIMPLE MANUAL TESTING (Example 1)
# ==========================================

# 1. Nodes banaye (List: 1 -> 4 -> 3 -> 2 -> 5 -> 2)
head = listnode(1)
n1 = listnode(4)
n2 = listnode(3)
n3 = listnode(2)
n4 = listnode(5)
n5 = listnode(2)

# 2. Nodes ko aapas mein jodh diya
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# 3. Partition function call kiya (x = 3 ke liye)
x = 3
new_head = partition(head, x)

# 4. Saari values ko simple loop se print karwa liya
print("Updated List Values:")
current = new_head #hm yaha current = new_head esliye banate ye vala current new jo list banayi ospe chale ga 
                    #or phele vala purane pe
while current is not None:
  print(current.value, end=" -> ")
  current = current.next
print("None")