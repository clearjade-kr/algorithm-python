class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(next=head)
        node_big_prev = dummy
        node_big = head

        while node_big and node_big.val < x:
            node_big_prev = node_big
            node_big = node_big.next

        if not node_big:
            return head
        
        node_cur_prev = node_big
        node_cur = node_big.next
        while node_cur:
            if node_cur.val < x:
                next_node = node_cur.next
                node_big_prev.next = node_cur
                node_cur.next = node_big

                node_cur_prev.next = next_node

                node_big_prev = node_cur
                node_cur = next_node
            else:
                node_cur_prev = node_cur
                node_cur = node_cur.next

        return dummy.next
