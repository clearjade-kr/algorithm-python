class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        dp[0] = 0

        for i in range(len(nums)):
            for j in range(i + 1, i + nums[i] + 1):
                if j >= len(nums):
                    break
                elif dp[j] != -1:
                    continue
                dp[j] = dp[i] + 1

        # print(dp)
        return dp[-1]