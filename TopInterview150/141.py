# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Truly inaccurate example to show. Why head is explained as a list?
        # set_nodes = set()
        # while head:
        #     if head in set_nodes:
        #         return True
        #     set_nodes.add(head)
        #     head = head.next
        # return False
        slow , fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True

        return False

