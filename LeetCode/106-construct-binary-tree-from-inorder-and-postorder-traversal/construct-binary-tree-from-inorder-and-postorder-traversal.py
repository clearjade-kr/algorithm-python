# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i

        postorder_idx = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None

            nonlocal postorder_idx
            cur_node = TreeNode(val=postorder[postorder_idx])
            postorder_idx -= 1
            if left < right:
                inorder_idx = index[cur_node.val]
                cur_node.right = build(inorder_idx + 1, right)
                cur_node.left = build(left, inorder_idx - 1)
            return cur_node

        return build(0, len(postorder) - 1)
