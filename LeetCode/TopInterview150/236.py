# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # from copy import copy
        # dict_nodes = {}
        #
        # if p == q:
        #     return p
        #
        # list_p = ""
        # list_q = ""
        #
        # stack = [(root, "")]
        # while stack:
        #     node, cur_list = stack.pop()
        #     if not node:
        #         continue
        #     dict_nodes[node.val] = node
        #     cur_list = cur_list + " " + str(node.val)
        #     if node == p:
        #         list_p = copy(cur_list)
        #     if node == q:
        #         list_q = copy(cur_list)
        #
        #     stack.append((node.left, copy(cur_list)))
        #     stack.append((node.right, copy(cur_list)))
        #
        # list_p = list_p.split()
        # list_q = list_q.split()
        # min_len = min(len(list_p), len(list_q))
        # idx = 0
        # for i in range(min_len):
        #     if list_p[i] != list_q[i]:
        #         break
        #     idx = i
        # return dict_nodes[int(list_p[idx])]
        if not root:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right



if __name__ == "__main__":
    sol = Solution()
    #
    # n7 = TreeNode(x=7)
    # n4 = TreeNode(x=4)
    #
    # n2 = TreeNode(x=2)
    # n2.left = n7
    # n2.right = n4
    #
    # n6 = TreeNode(x=6)
    # n5 = TreeNode(x=5)
    # n5.left = n6
    # n5.right = n2
    #
    # n0 = TreeNode(x=0)
    # n8 = TreeNode(x=8)
    # n1 = TreeNode(x=1)
    # n1.left = n0
    # n1.right = n8
    #
    # n3 = TreeNode(x=3)
    # n3.left = n5
    # n3.right = n1
    #
    # nd = sol.lowestCommonAncestor(root=n3, p=n5, q=n1)

    n8 = TreeNode(x=8)
    n_2 = TreeNode(x=-2)
    n4 = TreeNode(x=4)
    n_2.left = n8

    n0 = TreeNode(x=0)
    n0.left = n_2
    n0.right = n4

    n3 = TreeNode(x=3)
    n_1 = TreeNode(x=-1)
    n_1.left = n0
    n_1.right = n3

    nd = sol.lowestCommonAncestor(root=n_1, p=n3, q=n8)
    print(nd)
