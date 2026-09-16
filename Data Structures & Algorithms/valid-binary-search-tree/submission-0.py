# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low=float('-inf'), high=float('inf')):
            # Base case: an empty tree/node is valid
            if not node:
                return True
            
            # The current node's value must strictly be between low and high
            if not (low < node.val < high):
                return False
            
            # When we go left, the upper bound (high) becomes the current node's value
            # When we go right, the lower bound (low) becomes the current node's value
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        return validate(root)