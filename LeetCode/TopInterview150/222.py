from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # stack = [(root, 1)]
        # ret = 0
        # while stack:
        #     node, val = stack.pop()
        #     if node.left is None and node.right is None:
        #         ret = max(ret, val)
        #         continue
        #     if node.left:
        #         stack.append((node.left, val * 2))
        #     if node.right:
        #         stack.append((node.right, val * 2 + 1))
        # return ret

        l = 0
        cur = root
        while cur:
            l += 1
            cur = cur.left
        r = 0
        cur = root
        while cur:
            r += 1
            cur = cur.right
        if l == r:
            return 2 ** l - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
