# 1. Yeh function hai jo check karega
def has_cycle(head):
    slow = head
    fast = head
    
    # Jab tak fast aur fast ka agla dabba mojood hai
    while fast and fast.next:
        slow = slow.next          # Slow chala 1 step aage
        fast = fast.next.next     # Fast chala 2 steps aage
        
        # Agar dono aik hi jagah par aa gaye
        if slow == fast:
            return True           # Matlab gol ghum kar takra gaye, cycle hai!
            
    return False                  # List khatam ho gayi, koi cycle nahi hai