class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        ret_node = head

        prev_node = None
        cur_node = head
        next_node = head.next
        target_val = None

        while cur_node:
            if next_node and cur_node.val == next_node.val:
                if prev_node:
                    prev_node.next = next_node
                else:
                    ret_node = next_node
                target_val = cur_node.val
                cur_node = next_node
                if cur_node:
                    next_node = cur_node.next

            elif cur_node.val == target_val:
                if prev_node:
                    prev_node.next = next_node
                else:
                    ret_node = next_node
                cur_node = next_node
                if cur_node:
                    next_node = cur_node.next

            else:
                if next_node:
                    target_val = cur_node.val
                else:
                    break
                prev_node = cur_node
                cur_node = next_node
                next_node = cur_node.next

        return ret_node
