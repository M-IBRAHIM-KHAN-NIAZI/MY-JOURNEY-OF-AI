# LEETCODE 146 =LRU CACHE
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRU_CACHE:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache={}

        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def remove(self,node):
        prev_node=node.prev
        next_node=node.next

        prev_node.next=next_node
        next_node.prev=prev_node

    def add(self,node):
        original_first=self.head.next
        self.head.next=node
        node.prev=self.head

        node.next=original_first
        original_first.prev=node

    def get (self,key):
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.add(node) 
            return node.val
        return -1

    def put(self,key,value):
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            node.val=value
            self.add(node)
        else:

            if len(self.cache)>= self.capacity:
                     


                     lru=self.tail.prev
                     self.remove(lru)
                     del self.cache[lru.key]
         
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add(new_node)
   # --- Local Testing Block ---
if __name__ == "__main__":
       print("--- LRU Cache Local Testing Start ---")
       
       # Capacity 2 ka cache banate hain (yani maximum 2 items aa sakte hain)
       lru = LRU_CACHE(2)
       
       lru.put(1, 1) # Cache mein key=1, val=1 dala
       lru.put(2, 2) # Cache mein key=2, val=2 dala
       
       # F-string ka istemaal
       print(f"Get 1 (Expect 1): {lru.get(1)}")    # Returns 1 (Kyunki key 1 maujood hai, aur yeh most recent ban gaya)
       
       lru.put(3, 3) # Capacity full (2) hai, toh sabse purana (Least Recent / key 2) delete ho jayega!
       print(f"Get 2 (Expect -1): {lru.get(2)}")   # Returns -1 (Kyunki key 2 delete ho chuki hai)
       
       lru.put(4, 4) # Capacity phir full hai, ab sabse purana (key 1) delete ho jayega!
       print(f"Get 1 (Expect -1): {lru.get(1)}")   # Returns -1 (Kyunki key 1 bhi delete ho chuki hai)
       print(f"Get 3 (Expect 3): {lru.get(3)}")    # Returns 3 (Kyunki key 3 abhi bhi andar hai)
       print(f"Get 4 (Expect 4): {lru.get(4)}")    # Returns 4 (Kyunki key 4 abhi-abhi dali hai)
       
       print("--- Local Testing Successfully Finished! ---")
                                    
            

            













                