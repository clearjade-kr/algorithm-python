class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        list_sum = [-3 * (10 ** 4)] * len(nums)
        list_sum[0] = nums[0]
        for i in range(1, len(nums)):
            list_sum[i] = max(list_sum[i - 1] + nums[i], nums[i])

        minus_idx = 0
        while minus_idx < len(nums) and nums[minus_idx] >= 0:
            minus_idx += 1
        if minus_idx == len(nums):
            return max(list_sum)
        
        minus_cnt = 0
        for i in range(minus_idx, len(nums)):
            if nums[i] < 0:
                minus_cnt += 1
        if minus_cnt == len(nums):
            return max(list_sum)

        list_sum_minus = [3 * (10 ** 4)] * len(nums)
        list_sum_minus[0] = nums[0]
        for i in range(1, len(nums)):
            list_sum_minus[i] = min(list_sum_minus[i - 1] + nums[i], nums[i])

        return max(max(list_sum), sum(nums) - min(list_sum_minus))