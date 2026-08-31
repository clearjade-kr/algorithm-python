# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        orig_arr = []
        while head:
            orig_arr.append(head)
            head = head.next

        ret_arr = []
        for node in orig_arr:
            ret_arr.append(Node(x=node.val))

        for i in range(len(ret_arr) - 1):
            ret_arr[i].next = ret_arr[i + 1]

        for i in range(len(orig_arr)):
                node = orig_arr[i]
                target_node = ret_arr[i]

                if node.random:
                    idx = orig_arr.index(node.random)
                    target_node.random = ret_arr[idx]

        if not ret_arr:
            return None
        return ret_arr[0]