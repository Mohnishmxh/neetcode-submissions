# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base cases
        if not subRoot:
            return True  # An empty subtree is always a subtree
        if not root:
            return False # If the main tree runs out, subRoot isn't in it
        
        # 1. Check if the tree starting at the CURRENT node matches subRoot
        if self.isSameTree(root, subRoot):
            return True
        
        # 2. Otherwise, check if subRoot is hidden further down the left or right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Helper function from our previous problem
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)