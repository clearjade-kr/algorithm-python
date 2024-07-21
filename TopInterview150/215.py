from typing import List


# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         import heapq
#
#         heapq.heapify(nums)
#         for _ in range(len(nums) - k):
#             heapq.heappop(nums)
#
#         return heapq.heappop(nums)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heapify, heappushpop, heappop
        n = len(nums)
        heap = nums[:k]
        heapify(heap)

        for idx in range(k, n):
            heappushpop(heap, nums[idx])

        return heappop(heap)
