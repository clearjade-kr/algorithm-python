# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ret_head = head
        cur_node = head
        left_end = None
        for i in range(left - 1):
            if i == left - 2:
                left_end = cur_node
            cur_node = cur_node.next

        right_end = None
        list_rev = []
        for i in range(right - left + 1):
            list_rev.append(cur_node)
            cur_node = cur_node.next
            if i == right - left:
                right_end = cur_node

        for i in range(len(list_rev) - 1, 0, -1):
            list_rev[i].next = list_rev[i - 1]

        if list_rev:
            list_rev[0].next = right_end
        if left_end:
            left_end.next = list_rev[-1]
        elif list_rev:
            ret_head = list_rev[-1]

        return ret_head
