# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val):
            # Base case: if the node doesn't exist, it adds 0 to our count
            if not node:
                return 0
            
            count = 0
            # If the current node is greater than or equal to the path max, it's "good"
            if node.val >= max_val:
                count = 1
                max_val = node.val  # Update the max value for the children below
            
            # Recursively check left and right subtrees, passing down the new max
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            
            return count
        
        # Start the DFS with the root node and its own value as the initial max
        return dfs(root, root.val)