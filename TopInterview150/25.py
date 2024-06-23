from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        ret_node = head
        len_list = 0
        node_cnt = head
        while node_cnt:
            len_list += 1
            node_cnt = node_cnt.next

        for i in range(len_list // k):
            if i == 0:
                prev_tail = None

                prev_node = None
                cur_node = head
                next_node = cur_node.next
            else:
                prev_tail = cur_head

            cur_head = cur_node

            for _ in range(k):
                cur_node.next = prev_node

                prev_node = cur_node
                cur_node = next_node
                if cur_node:
                    next_node = cur_node.next
                else:
                    next_node = None

            cur_head.next = cur_node
            if prev_tail:
                prev_tail.next = prev_node

            if i == 0:
                ret_node = prev_node

        return ret_node


if __name__ == "__main__":
    sol = Solution()

    # n5 = ListNode(val=5)
    # n4 = ListNode(val=4, next=n5)
    # n3 = ListNode(val=3, next=n4)
    # n2 = ListNode(val=2, next=n3)
    n2 = ListNode(val=2)
    n1 = ListNode(val=1, next=n2)

    print(sol.reverseKGroup(n1, 2))
