from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []

        ret_list = []
        cur_list = deque([root])
        cur_dir = 1
        while cur_list:
            list_vals = []
            len_cur = len(cur_list)
            for _ in range(len_cur):
                node = cur_list.popleft()
                list_vals.append(node.val)
                if node.left:
                    cur_list.append(node.left)
                if node.right:
                    cur_list.append(node.right)
            ret_list.append(list_vals[::cur_dir])
            cur_dir *= -1
        return ret_list


