from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        orig_head = head
        orig_tail = head
        cur_node = head
        len_list = 0
        while cur_node:
            len_list += 1
            if not cur_node.next:
                orig_tail = cur_node
            cur_node = cur_node.next

        if len_list <= 1:
            return orig_head

        k %= len_list
        if k == 0:
            return orig_head

        target_head = orig_head
        for _ in range(len_list - k - 1):
            target_head = target_head.next

        ret_node = target_head.next
        target_head.next = None
        orig_tail.next = orig_head
        return ret_node

