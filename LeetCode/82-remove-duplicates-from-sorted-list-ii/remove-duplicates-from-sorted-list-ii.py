class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
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