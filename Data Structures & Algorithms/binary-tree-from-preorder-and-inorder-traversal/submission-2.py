class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        idx_map = {val: i for i, val in enumerate(inorder)}
        preorder.reverse()

        def build(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None

            root_val = preorder.pop()
            root = TreeNode(root_val)
            mid = idx_map[root_val]

            
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)