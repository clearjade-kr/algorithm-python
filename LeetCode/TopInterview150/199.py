from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret_list = []
        if not root:
            return ret_list

        cur_nodes = [root]
        while cur_nodes:
            ret_list.append(cur_nodes[-1].val)
            num_cur = len(cur_nodes)
            for i in range(num_cur):
                node = cur_nodes.pop(0)
                if node.left:
                    cur_nodes.append(node.left)
                if node.right:
                    cur_nodes.append(node.right)

        return ret_list
