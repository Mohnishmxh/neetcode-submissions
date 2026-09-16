# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            # If both p and q are smaller than current, LCA must be in the left subtree
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            
            # If both p and q are greater than current, LCA must be in the right subtree
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            
            # If they split (one is smaller, one is larger) or one equals curr, 
            # we have found our Lowest Common Ancestor!
            else:
                return curr
        
        return None