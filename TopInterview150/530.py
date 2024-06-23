from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
#
#         def left_closest(node):
#             if node.right:
#                 return left_closest(node.right)
#             return node.val
#
#         def right_closest(node):
#             if node.left:
#                 return right_closest(node.left)
#             return node.val
#
#         def dfs(node):
#             if not node:
#                 return float('inf')
#             left = dfs(node.left)
#             right = dfs(node.right)
#             left_closest_val = float('inf')
#             if node.left:
#                 left_closest_val = node.val - left_closest(node.left)
#             right_closest_val = float('inf')
#             if node.right:
#                 right_closest_val = right_closest(node.right) - node.val
#
#             return min(left_closest_val, right_closest_val, left, right)
#
#         return dfs(root)

class Solution:
    def __init__(self):
        self.min = None
        self.pre = None

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min = float('inf')
        self.pre = None

        def dfs(root):
            if not root: return
            dfs(root.left)
            if self.pre:
                self.min = min(self.min, root.val - self.pre.val)
            self.pre = root
            dfs(root.right)

        dfs(root)
        return self.min

