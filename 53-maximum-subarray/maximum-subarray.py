class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        list_sum = [0] * len(nums)
        list_sum[0] = nums[0]
        for i in range(1, len(nums)):
            list_sum[i] = max(list_sum[i - 1] + nums[i], nums[i])
        return max(list_sum)
