from typing import List


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#
#         def find_start():
#             left = 0
#             right = len(nums) - 1
#             while left < right:
#                 mid = (left + right) // 2
#                 if nums[mid] < nums[right]:
#                     right = mid
#                 else:
#                     left = mid + 1
#             return left
#
#         def binary_search(left, right):
#             while left <= right:
#                 mid = (left + right) // 2
#                 if nums[mid] == target:
#                     return mid
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return -1
#
#         start_point = find_start()
#         nums = nums[start_point:] + nums[:start_point]
#         target_idx = binary_search(0, len(nums) - 1)
#         if target_idx == -1:
#             return -1
#         return (start_point + binary_search(0, len(nums) - 1)) % len(nums)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target > nums[r] or target < nums[m]:
                    r = m-1
                else:
                    l = m+1
        return -1
