import math
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         list_nodes = []
#         while head:
#             list_nodes.append(head.val)
#             head = head.next
#         list_nodes.sort()
#         dummy = ListNode()
#         current = dummy
#         for val in list_nodes:
#             current.next = ListNode(val)
#             current = current.next
#         return dummy.next

class Solution:
    def merge(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if not head1 or not head2:
            return head1 or head2
        cur = dummy = ListNode()
        while head1 or head2:
            a = head1.val if head1 else math.inf
            b = head2.val if head2 else math.inf
            if a < b:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = fast = head
        tail = None
        while fast and fast.next:
            tail = slow
            slow, fast = slow.next, fast.next.next
        tail.next = None
        return self.merge(self.sortList(head), self.sortList(slow))


if __name__ == "__main__":
    # 1,2,4,5,3,6
    n6 = ListNode(6)
    n5 = ListNode(val=3, next=n6)
    n4 = ListNode(val=5, next=n5)
    n3 = ListNode(val=4, next=n4)
    n2 = ListNode(val=2, next=n3)
    n1 = ListNode(val=1, next=n2)
    solution = Solution()
    result = solution.sortList(n1)
    print(result.val)
