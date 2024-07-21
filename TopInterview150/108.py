from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#
#         def create_tree(cur_val, left_tree, right_tree):
#             cur_node = TreeNode(val=cur_val)
#             if left_tree:
#                 mid_idx = len(left_tree) // 2
#                 cur_node.left = create_tree(left_tree[mid_idx], left_tree[:mid_idx],
#                                             left_tree[mid_idx + 1:])
#             if right_tree:
#                 mid_idx = len(right_tree) // 2
#                 cur_node.right = create_tree(right_tree[mid_idx], right_tree[:mid_idx],
#                                              right_tree[mid_idx + 1:])
#             return cur_node
#
#         root_idx = len(nums) // 2
#         return create_tree(nums[root_idx], nums[:root_idx], nums[root_idx + 1:])


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root = TreeNode()
        node_with_range_stack = [(root, 0, len(nums))]
        while node_with_range_stack:
            node, begin, end = node_with_range_stack.pop()
            mid = (begin + end) // 2
            node.val = nums[mid]
            if begin < mid:
                node.left = TreeNode()
                node_with_range_stack.append((node.left, begin, mid))
            if mid + 1 < end:
                node.right = TreeNode()
                node_with_range_stack.append((node.right, mid + 1, end))
        return root
