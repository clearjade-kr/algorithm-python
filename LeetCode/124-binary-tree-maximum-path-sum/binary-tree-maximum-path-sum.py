# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = -10000

        def traverse_path(node):
            nonlocal max_val
            if not node:
                return 0
            left_val = traverse_path(node.left)
            right_val = traverse_path(node.right)

            cur_max = max(node.val, node.val + left_val, node.val + right_val)
            max_val = max(max_val, cur_max, node.val + left_val + right_val)
            return cur_max

        traverse_path(root)
        return max_val