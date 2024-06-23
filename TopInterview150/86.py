from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return head
        #
        # dummy = ListNode(next=head)
        # node_big_prev = dummy
        # node_big = head
        #
        # while node_big and node_big.val < x:
        #     node_big_prev = node_big
        #     node_big = node_big.next
        #
        # if not node_big:
        #     return head
        #
        # node_cur_prev = node_big
        # node_cur = node_big.next
        # while node_cur:
        #     if node_cur.val < x:
        #         next_node = node_cur.next
        #         node_big_prev.next = node_cur
        #         node_cur.next = node_big
        #
        #         node_cur_prev.next = next_node
        #
        #         node_big_prev = node_cur
        #         node_cur = next_node
        #     else:
        #         node_cur_prev = node_cur
        #         node_cur = node_cur.next
        #
        # return dummy.next
        d1=c1=ListNode(0)
        d2=c2=ListNode(0)
        while head:
            if head.val<x:
                d1.next=head
                d1=d1.next

            else:
                d2.next=head
                d2=d2.next

            head=head.next

        d2.next=None
        d1.next=c2.next
        return c1.next


if __name__ == "__main__":
    # Input: head = [1,4,3,2,5,2], x = 3
    n6 = ListNode(val=2)
    n5 = ListNode(val=5, next=n6)
    n4 = ListNode(val=2, next=n5)
    n3 = ListNode(val=3, next=n4)
    n2 = ListNode(val=4, next=n3)
    n1 = ListNode(val=1, next=n2)
    x = 3

    # n2 = ListNode(val=1)
    # n1 = ListNode(val=2, next=n2)
    # x = 2

    sol = Solution()
    print(sol.partition(head=n1, x=x))


