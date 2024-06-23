from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret_val = None
        cur_head = None
        raise_val = 0
        while l1 or l2:
            sum_val = 0
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            sum_val += raise_val
            if sum_val >= 10:
                sum_val %= 10
                raise_val = 1
            else:
                raise_val = 0
            new_node = ListNode(val=sum_val)
            if not ret_val:
                ret_val = new_node
                cur_head = new_node
            else:
                cur_head.next = new_node
                cur_head = new_node

        if raise_val == 1:
            new_node = ListNode(val=raise_val)
            cur_head.next = new_node

        return ret_val





