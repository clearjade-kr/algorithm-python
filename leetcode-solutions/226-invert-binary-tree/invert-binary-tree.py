class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def change(node):
            if not node:
                return

            if not (node.left or node.right):
                return

            node.left, node.right = node.right, node.left
            change(node.left)
            change(node.right)

        change(root)
        return root
