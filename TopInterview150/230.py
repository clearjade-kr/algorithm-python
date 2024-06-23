from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.min = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # self.min = []
        #
        # def dfs(node):
        #     if not node:
        #         return
        #     dfs(node.left)
        #     self.min.append(node.val)
        #     dfs(node.right)
        #
        # dfs(root)
        # return self.min[k - 1]
        self.k = k
        self.k_smallest = None
        def inorder(node):
            if not node or self.k_smallest is not None:
                return

            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.k_smallest = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.k_smallest




