class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def is_same(p, q):
            if not (p or q):
                return True
            if not (p and q):
                return False

            if p.val != q.val:
                return False

            if not (p.left or p.right or q.left or q.right):
                return p.val == q.val

            return is_same(p.left, q.left) and is_same(p.right, q.right)

        return is_same(p, q)
