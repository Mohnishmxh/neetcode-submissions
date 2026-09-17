class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        """Encodes a tree to a single comma-separated string."""
        vals = []

        def dfs(node: TreeNode | None) -> None:
            if not node:
                vals.append("N")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> TreeNode | None:
        """Decodes your encoded data back to a tree structure."""
        vals = iter(data.split(","))

        def dfs() -> TreeNode | None:
            val = next(vals)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()