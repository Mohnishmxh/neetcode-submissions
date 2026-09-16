class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Helper function to convert a tree into a unique string
        def serialize(node):
            if not node:
                return "#"  # Represents a null/empty node
            # Use commas/brackets to prevent mismatch issues with numbers (e.g., node 12 vs node 1 and 2)
            return f"^{node.val},{serialize(node.left)},{serialize(node.right)}"
        
        # Convert both trees to strings
        root_str = serialize(root)
        subRoot_str = serialize(subRoot)
        
        # Check if subRoot's string exists inside root's string
        return subRoot_str in root_str