class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_sum = float('-inf')

        def get_max_gain(node: TreeNode | None) -> int:
            nonlocal max_sum
            if not node:
                return 0

            # Discard any negative branch contributions by capping at 0
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)

            # Price of the path if this node is the apex (connecting left and right)
            current_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path_sum)

            # Return the single best extending path to the parent
            return node.val + max(left_gain, right_gain)

        get_max_gain(root)
        return max_sum