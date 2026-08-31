class Solution:
    def rob(self, nums: List[int]) -> int:
        list_max = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                list_max[i] = nums[i]
            elif i == 1:
                list_max[i] = max(nums[i], nums[i - 1])
            else:
                list_max[i] = max(list_max[i - 1], list_max[i - 2] + nums[i])
        return list_max[-1]
