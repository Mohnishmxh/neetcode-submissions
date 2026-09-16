class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        curr = root
        prev = None
        
        while curr or stack:
            # 1. Dive as far left as possible, pushing nodes to our stack
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. Pop the leftmost (smallest available) node
            curr = stack.pop()
            
            # 3. If the current value is less than or equal to the previous, it's not a BST
            if prev is not None and curr.val <= prev:
                return False
            
            prev = curr.val
            
            # 4. Move to the right child
            curr = curr.right
            
        return True