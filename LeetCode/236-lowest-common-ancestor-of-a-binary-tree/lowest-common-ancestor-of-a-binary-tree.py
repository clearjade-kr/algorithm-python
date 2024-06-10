# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        from copy import copy
        dict_nodes = {}

        if p == q:
            return p

        list_p = ""
        list_q = ""

        stack = [(root, "")]
        while stack:
            node, cur_list = stack.pop()
            if not node:
                continue
            dict_nodes[node.val] = node
            cur_list = cur_list + " " + str(node.val)
            if node == p:
                list_p = copy(cur_list)
            if node == q:
                list_q = copy(cur_list)

            stack.append((node.left, copy(cur_list)))
            stack.append((node.right, copy(cur_list)))

        list_p = list_p.split()
        list_q = list_q.split()
        min_len = min(len(list_p), len(list_q))
        idx = 0
        for i in range(min_len):
            if list_p[i] != list_q[i]:
                break
            idx = i
        return dict_nodes[int(list_p[idx])]
