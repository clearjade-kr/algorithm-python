# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        preorder = []
        
        def preorder_traverse(node):
            preorder.append(node)
            if node.left:
                preorder_traverse(node.left)
            if node.right:
                preorder_traverse(node.right)
        
        preorder_traverse(root)
        
        for n, nx in zip(preorder, preorder[1:]):
            n.left = None
            n.right = nx

        
