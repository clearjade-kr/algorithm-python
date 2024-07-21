from typing import List


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         list_sum = [0] * len(nums)
#         list_sum[0] = nums[0]
#         for i in range(1, len(nums)):
#             list_sum[i] = max(list_sum[i - 1] + nums[i], nums[i])
#         return max(list_sum)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        list_sum = [nums[0]]
        for n in nums[1:]:
            list_sum.append(list_sum[-1] + n)

        max_sum = list_sum[0]
        min_sum = 0

        for i in range(len(list_sum)):
            max_sum = max(max_sum, list_sum[i] - min_sum)
            min_sum = min(min_sum, list_sum[i])

        return max_sum
