from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dict_nodes = {}
        for i in range(len(lists)):
            node = lists[i]
            while node:
                if node.val not in dict_nodes:
                    dict_nodes[node.val] = []
                dict_nodes[node.val].append(node)
                node = node.next
        head = ListNode()
        node = head
        for key in sorted(dict_nodes.keys()):
            for i in range(len(dict_nodes[key])):
                node.next = dict_nodes[key][i]
                node = node.next

        return head.next

