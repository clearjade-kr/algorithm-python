class Solution:
    def jump(self, nums: List[int]) -> int:
        # -- My previous solution --
        # dp = [-1] * len(nums)
        # dp[0] = 0
        #
        # for i in range(len(nums)):
        #     for j in range(i + 1, i + nums[i] + 1):
        #         if j >= len(nums):
        #             break
        #         elif dp[j] != -1:
        #             continue
        #         dp[j] = dp[i] + 1
        #
        # # print(dp)
        # return dp[-1]

        # -- Better solution found --
        # IDEA : find the furthest position that I can get from current position
        # If I can reach specific position,
        # then I can reach any position before at same number of jump.
        jumps = 0
        end = 0

        reach = 0
        for pos in range(len(nums) - 1):
            reach = max(reach, pos + nums[pos])
            if pos == end:
                end = reach
                jumps += 1
        return jumps