from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def traverse_tree(node, cur_sum):
            if not node:
                return
            nonlocal ret
            if node.right is None and node.left is None:
                ret += cur_sum * 10 + node.val
                return

            cur_sum = cur_sum * 10 + node.val
            traverse_tree(node.left, cur_sum)
            traverse_tree(node.right, cur_sum)

        traverse_tree(root, 0)
        return ret


