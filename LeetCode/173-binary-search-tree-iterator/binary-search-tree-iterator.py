# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.list_nodes = []
        self.next_idx = 0

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.list_nodes.append(node)
            inorder(node.right)

        inorder(root)

    def next(self) -> int:
        ret_val = self.list_nodes[self.next_idx].val
        self.next_idx += 1
        return ret_val

    def hasNext(self) -> bool:
        return self.next_idx < len(self.list_nodes)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()