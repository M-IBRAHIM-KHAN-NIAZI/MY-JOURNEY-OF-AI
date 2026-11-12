# ==========================================
# LeetCode 86: Partition List (Example 1)
# ==========================================
class listnode:
    def __init__(self,value):
        self.value=value
        self.next=None

def partition(head,x): #hamari original list listnode ha jisme hamne do dummy list banaye hn 
    less_dummy=listnode(-1)  
    greater_dummy=listnode(-1)

    less=less_dummy
    greater=greater_dummy

    current=head #current = head`  `current` ek tarah se hamari original list hi hoti hai
                #(ek scanner/pointer jo `head` se shuru hokar list ke har ek node ko ek-ek karke visit aur check karta hai)
    while current is not None:
        if current.value< x:
            less.next=current
            less=less.next
        else:
            greater.next=current
            greater=greater.next
    current=current.next  #ye hamara basically current original list ka while loop chal raha hota ha jisko hamne ek step
                          # aage karna hota taake dosre dfa jab while loop chale tu ye step na aye
    greater.next=None                      

    less.next=greater_dummy.next
    return less_dummy.next                       
                                             

