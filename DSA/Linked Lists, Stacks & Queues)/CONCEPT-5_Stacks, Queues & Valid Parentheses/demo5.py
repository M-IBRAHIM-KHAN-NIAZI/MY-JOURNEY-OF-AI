from collections import deque

# TreeNode ki choti si definition taaki VS Code mein bhi aasani se chale
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []  # Agar tree hi khali hai toh khali list return kar do

        result = []          # Final answer: har level ki list iske andar aayegi
        queue = deque([root])  # Queue shuru ki aur usmein root node daal diya

        while queue:
            level_size = len(queue)  # Is current level mein total kitne nodes hain
            current_level = []       # Is level ki values store karne ke liye list

            for _ in range(level_size):
                node = queue.popleft()  # Queue ke aage (front) se node nikalo (FIFO)
                current_level.append(node.val)  # Us node ki value level list mein daalo

                # Agar left child hai toh usko queue ke  daal do
                if node.left:
                    queue.append(node.left)

                # Agar right child hai toh usko bhi queue  mein daal do
                if node.right:
                    queue.append(node.right)

            # Ek level poora ho gaya, ab uski list ko final result mein add kar do
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
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    output = sol.levelOrder(root)

    print("Level Order Output ([[3], [9, 20], [15, 7]] expected):", output)   