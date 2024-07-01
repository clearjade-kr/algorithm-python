class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_nodes = []
        while head:
            list_nodes.append(head.val)
            head = head.next
        list_nodes.sort()
        dummy = ListNode()
        current = dummy
        for val in list_nodes:
            current.next = ListNode(val)
            current = current.next
        return dummy.next