from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # root_idx = inorder.index(preorder[0])
        # left_sub = inorder[:root_idx]
        # right_sub = inorder[root_idx + 1:]
        #
        # def create_tree(cur_pre_idx, left_subtree, right_subtree):
        #     ret_node = TreeNode(val=preorder[cur_pre_idx])
        #     if right_subtree:
        #         right_pre_idx = find_right_idx(cur_pre_idx, right_subtree)
        #         right_in_idx = right_subtree.index(preorder[right_pre_idx])
        #         right_node = create_tree(right_pre_idx,
        #                                  right_subtree[:right_in_idx],
        #                                  right_subtree[right_in_idx + 1:])
        #         ret_node.right = right_node
        #     if left_subtree:
        #         left_pre_idx = find_left_idx(cur_pre_idx, left_subtree)
        #         left_in_idx = left_subtree.index(preorder[left_pre_idx])
        #         left_node = create_tree(left_pre_idx,
        #                                 left_subtree[:left_in_idx],
        #                                 left_subtree[left_in_idx + 1:])
        #         ret_node.left = left_node
        #
        #     return ret_node
        #
        # def find_left_idx(cur_pre_idx, left_subtree):
        #     for idx in range(cur_pre_idx + 1, len(preorder)):
        #         if preorder[idx] in left_subtree:
        #             return idx
        #     return None
        #
        # def find_right_idx(cur_pre_idx, right_subtree):
        #     for idx in range(cur_pre_idx + 1, len(preorder)):
        #         if preorder[idx] in right_subtree:
        #             return idx
        #     return None
        #
        # return create_tree(0, left_sub, right_sub)
        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i
        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            rootval = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(val=rootval)
            i = index[rootval]
            root.left = build(left, i - 1)
            root.right = build(i + 1, right)
            return root
        return build(0, len(preorder) - 1)


# preorder = [3,9,14,6,20,15,7]
# inorder = [14,9,6,3,15,20,7]
# inorder_rev = [7,20,15,3,6,9,14]
# finding right node of current -> same order in preorder -> inorder
# Ex) 3 -> root
# find values after current node in preorder that is after node in inorder
# preorder : [3,9,20,15,7], inorder : ([3,15,20,7]) -> 20
# 20 is right node of 3
# Similarly, find values in
# Can find values recursively


if __name__ == "__main__":
    sol = Solution()
    # preorder = [3,9,14,6,20,15,7]
    # inorder = [14,9,6,3,15,20,7]

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    node = sol.buildTree(preorder=preorder, inorder=inorder)
    print(node)

