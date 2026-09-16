# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. Both nodes are None (we hit the end of both trees successfully)
        if not p and not q:
            return True
        
        # 2. One node is None while the other is not (structural mismatch)
        if not p or not q:
            return False
        
        # 3. Both nodes exist, but their values don't match
        if p.val != q.val:
            return False
        
        # 4. Recursively check that both the left subtrees and right subtrees match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)