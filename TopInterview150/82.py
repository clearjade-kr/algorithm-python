from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # ret_node = head
        #
        # prev_node = None
        # cur_node = head
        # next_node = head.next
        # target_val = None
        #
        # while cur_node:
        #     if next_node and cur_node.val == next_node.val:
        #         if prev_node:
        #             prev_node.next = next_node
        #         else:
        #             ret_node = next_node
        #         target_val = cur_node.val
        #         cur_node = next_node
        #         if cur_node:
        #             next_node = cur_node.next
        #
        #     elif cur_node.val == target_val:
        #         if prev_node:
        #             prev_node.next = next_node
        #         else:
        #             ret_node = next_node
        #         cur_node = next_node
        #         if cur_node:
        #             next_node = cur_node.next
        #
        #     else:
        #         if next_node:
        #             target_val = cur_node.val
        #         else:
        #             break
        #         prev_node = cur_node
        #         cur_node = next_node
        #         next_node = cur_node.next
        #
        # return ret_node

        dummy = ListNode()
        dummy.next = head

        cur_node = dummy
        while cur_node.next and cur_node.next.next:
            if cur_node.next.val == cur_node.next.next.val:
                while cur_node.next and cur_node.next.next \
                        and cur_node.next.val == cur_node.next.next.val:
                    cur_node.next = cur_node.next.next
                cur_node.next = cur_node.next.next

            else:
                cur_node = cur_node.next

        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    n7 = ListNode(val=5)
    n6 = ListNode(val=4, next=n7)
    n5 = ListNode(val=4, next=n6)
    n4 = ListNode(val=3, next=n5)
    n3 = ListNode(val=3, next=n4)
    n2 = ListNode(val=2, next=n3)
    n1 = ListNode(val=1, next=n2)

    print(sol.deleteDuplicates(n1))
