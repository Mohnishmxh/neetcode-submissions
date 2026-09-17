from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map values to their indices in inorder traversal for O(1) lookup
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0

        def helper(left_in: int, right_in: int) -> Optional[TreeNode]:
            nonlocal preorder_idx
            
            # Base case: if there are no elements to construct the subtree
            if left_in > right_in:
                return None

            # Pick current preorder_idx element as root
            root_val = preorder[preorder_idx]
            preorder_idx += 1
            root = TreeNode(root_val)

            # Split inorder array into left and right subtrees
            mid = inorder_index_map[root_val]

            # Build left subtree first, then right subtree
            root.left = helper(left_in, mid - 1)
            root.right = helper(mid + 1, right_in)

            return root

        return helper(0, len(inorder) - 1)