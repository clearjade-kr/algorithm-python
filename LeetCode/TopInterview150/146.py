class ListNode:
    def __init__(self, key, val, prev_node=None, next_node=None):
        self.key = key
        self.val = val
        self.prev = prev_node
        self.next = next_node


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.cnt = 0
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.cache:
            target_node = self.cache[key]
            if target_node != self.head:
                target_node.prev.next = target_node.next
                if target_node.next:
                    target_node.next.prev = target_node.prev
                if target_node == self.tail:
                    self.tail = target_node.prev
                self.head.prev = target_node
                target_node.next = self.head
                target_node.prev = None
                self.head = target_node
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            target_node = self.cache[key]
            if target_node != self.head:
                target_node.prev.next = target_node.next
                if target_node.next:
                    target_node.next.prev = target_node.prev
                if target_node == self.tail:
                    self.tail = target_node.prev
                self.head.prev = target_node
                target_node.next = self.head
                target_node.prev = None
                self.head = target_node
            target_node.val = value
        else:
            target_node = ListNode(key=key, val=value, next_node=self.head)
            self.cache[key] = target_node
            if self.cap == 1:
                if self.head:
                    self.cache.pop(self.head.key)
                self.head = target_node
                self.tail = target_node
            elif self.head:
                self.head.prev = target_node
                self.head = target_node
                self.cnt += 1
                if self.cnt > self.cap:
                    self.cache.pop(self.tail.key)
                    self.tail = self.tail.prev
                    self.tail.next = None
                    self.cnt -= 1
            else:
                self.cnt += 1
                self.head = target_node
                self.tail = target_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == "__main__":
    # cmds = ["LRUCache","put","put","get","put","get","put","get","get","get"]
    # vals = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

    cmds = ["LRUCache","put","get","put","get","get"]
    vals = [[1],[2,1],[2],[3,2],[2],[3]]

    cache = LRUCache(vals[0][0])
    for i in range(1, len(cmds)):
        if cmds[i] == "put":
            cache.put(vals[i][0], vals[i][1])
        else:
            cache.get(vals[i][0])
