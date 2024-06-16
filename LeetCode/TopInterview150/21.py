from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret_node = None
        cur_node = None
        while list1 and list2:
            if list1.val < list2.val:
                if not ret_node:
                    ret_node = list1
                    cur_node = list1
                else:
                    cur_node.next = list1
                    cur_node = list1
                list1 = list1.next
            else:
                if not ret_node:
                    ret_node = list2
                    cur_node = list2
                else:
                    cur_node.next = list2
                    cur_node = list2
                list2 = list2.next

        if list1:
            if cur_node:
                cur_node.next = list1
            else:
                ret_node = list1
        elif list2:
            if cur_node:
                cur_node.next = list2
            else:
                ret_node = list2
        return ret_node

