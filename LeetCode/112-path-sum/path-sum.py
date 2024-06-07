# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        flag_check = False

        def traverse_tree(node, cur_sum):
            nonlocal flag_check
            if flag_check:
                return

            if not node:
                return

            if node.val + cur_sum == targetSum and \
                    node.right is None and node.left is None:
                flag_check = True
                return

            traverse_tree(node.right, node.val + cur_sum)
            traverse_tree(node.left, node.val + cur_sum)

        traverse_tree(root, 0)
        return flag_check
