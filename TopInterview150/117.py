"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        cur_list = [root]

        while cur_list:
            next_list = []
            for i in range(len(cur_list) - 1):
                cur_list[i].next = cur_list[i + 1]
            for node in cur_list:
                if node.left:
                    next_list.append(node.left)
                if node.right:
                    next_list.append(node.right)

            cur_list = next_list

        return root


if __name__ == "__main__":
    sol = Solution()
    n4 = Node(val=4)
    n5 = Node(val=5)
    n7 = Node(val=7)

    n2 = Node(val=2, left=n4, right=n5)
    n3 = Node(val=3, right=n7)
    n1 = Node(val=1, left=n2, right=n3)

    root = sol.connect(n1)
    print(root)