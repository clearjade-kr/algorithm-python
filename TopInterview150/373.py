from typing import List


# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         import heapq
#
#         if not nums1 or not nums2:
#             return []
#
#         n1, n2 = len(nums1), len(nums2)
#         heap = [(nums1[0] + nums2[0], 0, 0)]
#         visited = set()
#         res = []
#
#         while heap and len(res) < k:
#             heapq.heapify(heap)
#             val, i, j = heapq.heappop(heap)
#             if i >= n1 or j >= n2:
#                 continue
#
#             if (i, j) in visited:
#                 continue
#
#             res.append([nums1[i], nums2[j]])
#             visited.add((i, j))
#
#             if i + 1 < n1 and (i + 1, j) not in visited:
#                 heap.append((nums1[i + 1] + nums2[j], i + 1, j))
#
#             if j + 1 < n2 and (i, j + 1) not in visited:
#                 heap.append((nums1[i] + nums2[j + 1], i, j + 1))
#
#         return res
#


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq

        if not nums1 or not nums2 or k <= 0:
            return []

        # Min-heap to store the pairs
        min_heap = []
        for j in range(min(k, len(nums2))):
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))

        # Result list
        result = []

        # Extract the smallest pairs from the heap
        while min_heap and len(result) < k:
            sum_val, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            # If there is a next element in the row, add the next pair into the heap
            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))

        return result
