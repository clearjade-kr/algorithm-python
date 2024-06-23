from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def left_max(node):
            if node.right:
                return left_max(node.right)
            return node.val

        def right_min(node):
            if node.left:
                return right_min(node.left)
            return node.val

        def dfs(node):
            if not node:
                return True
            if node.left and left_max(node.left) >= node.val:
                return False
            if node.right and right_min(node.right) <= node.val:
                return False
            return dfs(node.left) and dfs(node.right)

        return dfs(root)