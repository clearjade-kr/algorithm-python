from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        import heapq

        n = len(profits)
        arr = [(capital[i], profits[i]) for i in range(n)]
        arr.sort(key=lambda x: x[0])

        heap = []
        idx = 0
        for _ in range(k):
            while idx < n and arr[idx][0] <= w:
                heapq.heappush(heap, -arr[idx][1])
                idx += 1

            if heap:
                w -= heapq.heappop(heap)

        return w
