from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root]) # Start with the root node in our queue
        
        while queue:
            level_size = len(queue) # How many nodes are in the current level right now
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft() # Take the front node out of the line
                current_level.append(node.val) # Save its value
                
                # Add its children to the back of the line for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Once we finish a whole level, add it to our main result list
            result.append(current_level)
            
        return result