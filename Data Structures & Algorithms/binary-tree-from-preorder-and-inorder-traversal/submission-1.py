from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_idx = 0
        in_idx = 0
        n = len(preorder)

        def build(stop: Optional[int]) -> Optional[TreeNode]:
            nonlocal pre_idx, in_idx
            
            # Base cases: out of nodes or reached parent boundary
            if pre_idx >= n or inorder[in_idx] == stop:
                return None
            
            val = preorder[pre_idx]
            pre_idx += 1
            node = TreeNode(val)

            # Left subtree stops when inorder reaches current node's value
            node.left = build(val)
            
            # Skip the root value in inorder
            in_idx += 1
            
            # Right subtree stops when inorder reaches the current parent's stop value
            node.right = build(stop)

            return node

        return build(None)