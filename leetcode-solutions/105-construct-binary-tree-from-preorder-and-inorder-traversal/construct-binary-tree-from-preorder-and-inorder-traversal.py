# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_idx = inorder.index(preorder[0])
        left_sub = inorder[:root_idx]
        right_sub = inorder[root_idx + 1:]

        def create_tree(cur_pre_idx, left_subtree, right_subtree):
            ret_node = TreeNode(val=preorder[cur_pre_idx])
            if right_subtree:
                right_pre_idx = find_right_idx(cur_pre_idx, right_subtree)
                right_in_idx = right_subtree.index(preorder[right_pre_idx])
                right_node = create_tree(right_pre_idx,
                                         right_subtree[:right_in_idx],
                                         right_subtree[right_in_idx + 1:])
                ret_node.right = right_node
            if left_subtree:
                left_pre_idx = find_left_idx(cur_pre_idx, left_subtree)
                left_in_idx = left_subtree.index(preorder[left_pre_idx])
                left_node = create_tree(left_pre_idx,
                                        left_subtree[:left_in_idx],
                                        left_subtree[left_in_idx + 1:])
                ret_node.left = left_node

            return ret_node

        def find_left_idx(cur_pre_idx, left_subtree):
            for idx in range(cur_pre_idx + 1, len(preorder)):
                if preorder[idx] in left_subtree:
                    return idx
            return None

        def find_right_idx(cur_pre_idx, right_subtree):
            for idx in range(cur_pre_idx + 1, len(preorder)):
                if preorder[idx] in right_subtree:
                    return idx
            return None

        return create_tree(0, left_sub, right_sub)