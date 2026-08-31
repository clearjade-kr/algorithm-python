class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def create_tree(cur_val, left_tree, right_tree):
            cur_node = TreeNode(val=cur_val)
            if left_tree:
                mid_idx = len(left_tree) // 2
                cur_node.left = create_tree(left_tree[mid_idx], left_tree[:mid_idx],
                                            left_tree[mid_idx + 1:])
            if right_tree:
                mid_idx = len(right_tree) // 2
                cur_node.right = create_tree(right_tree[mid_idx], right_tree[:mid_idx],
                                             right_tree[mid_idx + 1:])
            return cur_node

        root_idx = len(nums) // 2
        return create_tree(nums[root_idx], nums[:root_idx], nums[root_idx + 1:])
