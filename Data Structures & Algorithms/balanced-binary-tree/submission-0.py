# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            # Base case: an empty node has a height of 0 and is balanced
            if not node:
                return 0
            
            # Check left subtree height
            left_height = dfs(node.left)
            if left_height == -1:
                return -1  # If left side is already unbalanced, bubble -1 up
            
            # Check right subtree height
            right_height = dfs(node.right)
            if right_height == -1:
                return -1  # If right side is already unbalanced, bubble -1 up
            
            # If the difference between left and right height is greater than 1, it's unbalanced
            if abs(left_height - right_height) > 1:
                return -1
            
            # Otherwise, return the actual height of the current node
            return 1 + max(left_height, right_height)
        
        # If dfs doesn't return -1, the tree is balanced
        return dfs(root) != -1