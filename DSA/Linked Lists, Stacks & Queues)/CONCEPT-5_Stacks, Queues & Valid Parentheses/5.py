###(Binary Tree Level Order Traversal - LC 102) ####
from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def tree(roots):
    if not roots:
        return []
    result=[]
    queue=deque([roots])
    while queue:
        level_size=len(queue)
        current_level=[]
        for _ in range(level_size):
            node=queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)
    return result      
 # --- Local Testing Block ---
if __name__ == "__main__":
     # Tree banate hain:
     #       3
     #      / \
     #     9  20
     #       /  \
     #      15   7
     roots = TreeNode(3)
     roots.left = TreeNode(9)
     roots.right = TreeNode(20)
     roots.right.left = TreeNode(15)
     roots.right.right = TreeNode(7)
 
     sol = tree(roots)
     
 
     print("Level Order Output ([[3], [9, 20], [15, 7]] expected):", sol)                 
              
                  
        


        
