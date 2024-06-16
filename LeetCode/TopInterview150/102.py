from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret_list = []
        if not root:
            return []

        cur_list = [root]
        while cur_list:
            ret_list.append([node.val for node in cur_list])
            next_list = []
            for node in cur_list:
                if node.left:
                    next_list.append(node.left)
                if node.right:
                    next_list.append(node.right)

            cur_list = next_list

        return ret_list
