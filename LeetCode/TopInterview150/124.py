from math import inf
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_val = -inf

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # def traverse_path(node):
        #     if not node:
        #         return 0
        #     left_val = traverse_path(node.left)
        #     right_val = traverse_path(node.right)
        #
        #     cur_max = max(node.val, node.val + left_val, node.val + right_val)
        #     self.max_val = max(self.max_val, cur_max, node.val + left_val + right_val)
        #     return cur_max
        #
        # traverse_path(root)
        # return self.max_val

        def dfs(root):
            if not root:
                return 0

            l = max(dfs(root.left), 0)
            r = max(dfs(root.right), 0)
            self.max = max(self.max, l + r + root.val)

            return max(l, r) + root.val

        dfs(root)
        return self.max


