# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(node):
    ret_nodes = []
    if node.left:
        ret_nodes.extend(inorder(node.left))
    ret_nodes.append(node.val)
    if node.right:
        ret_nodes.extend(inorder(node.right))
    return ret_nodes


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.next_idx = 0
        self.list_nodes = inorder(root)

    def next(self) -> int:
        ret_val = self.list_nodes[self.next_idx]
        self.next_idx += 1
        return ret_val

    def hasNext(self) -> bool:
        return self.next_idx < len(self.list_nodes)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()