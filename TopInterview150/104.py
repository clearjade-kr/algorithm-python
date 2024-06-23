from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ret_val = 0
        q = [(1 , root)]
        while q:
            cur_h, cur_node = q.pop()
            if not cur_node.left and not cur_node.right:
                ret_val = max(ret_val, cur_h)
                continue

            if cur_node.left:
                q.append((cur_h + 1, cur_node.left))
            if cur_node.right:
                q.append((cur_h + 1, cur_node.right))

        return ret_val