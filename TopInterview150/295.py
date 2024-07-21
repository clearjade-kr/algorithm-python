import heapq


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap or num > -self.min_heap[0]:
            heapq.heappush(self.min_heap, -num)
        else:
            heapq.heappush(self.max_heap, num)

    def findMedian(self) -> float:
        if not self.min_heap and self.max_heap:
            return self.max_heap[0]

        if len(self.min_heap) == len(self.max_heap):
            return (-self.min_heap[0] + self.max_heap[0]) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return -self.min_heap[0]
        else:
            return self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()