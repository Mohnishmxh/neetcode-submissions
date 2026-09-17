from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while curr or stack:
            # Go as deep left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Pop the current smallest element
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            # Switch to right subtree
            curr = curr.right
            
        return -1


# Helper function to construct a binary tree from LeetCode-style list representation
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    n = len(values)
    
    while queue and i < n:
        node = queue.popleft()
        
        # Left child
        if i < n and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < n and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
        
    return root


# Driver code
if __name__ == "__main__":
    solution = Solution()

    # Example 1: root = [2, 1, 3], k = 1
    tree1 = build_tree([2, 1, 3])
    print("Example 1 Output:", solution.kthSmallest(tree1, 1))  # Output: 1

    # Example 2: root = [4, 3, 5, 2, None], k = 4
    tree2 = build_tree([4, 3, 5, 2, None])
    print("Example 2 Output:", solution.kthSmallest(tree2, 4))  # Output: 5