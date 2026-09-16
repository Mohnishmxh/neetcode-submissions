# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize our tracker using 'self' so it stays saved across recursive calls
        self.diameter = 0
        
        def dfs(node):
            # Base case: if node is None, height is 0
            if not node:
                return 0
            
            # Get the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # The path length through the current node is left + right edges
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the height of the current node to its parent
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.diameter