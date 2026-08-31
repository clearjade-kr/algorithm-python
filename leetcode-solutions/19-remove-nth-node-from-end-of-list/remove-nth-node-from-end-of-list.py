class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        orig_head = head
        cur_node = head
        len_list = 0
        while cur_node:
            len_list += 1
            cur_node = cur_node.next

        if len_list == 1:
            return None
        if len_list == n:
            return head.next

        prev_node = None
        cur_node = head

        for _ in range(len_list - n):
            prev_node = cur_node
            cur_node = cur_node.next

        if prev_node:
            prev_node.next = cur_node.next
        else:
            return head.next

        return orig_head