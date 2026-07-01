# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        first = head
        second = head.next

        ret_head = first
        if second:
            ret_head = second
        prev_tail = None
    
        while first and second:
            temp_next = second.next
            second.next = first
            first.next = temp_next
            if prev_tail:
                prev_tail.next = second

            prev_tail = first
            first = first.next
            second = first.next if first else None

        return ret_head


if __name__ == "__main__":
    sol = Solution()
    fourth = ListNode(val=4, next=None)
    third = ListNode(val=3, next=fourth)
    second = ListNode(val=2, next=third)
    first = ListNode(val=1, next=second)
    print(sol.swapPairs(head=first))
