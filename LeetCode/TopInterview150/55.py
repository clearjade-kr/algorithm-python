from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Seems like using dynamic programming
        flag_reach = [False] * len(nums)
        flag_reach[0] = True
        cur_idx = 0
        for i in range(len(nums)):
            if cur_idx >= len(nums):
                break
            jump_height = nums[i]
            if cur_idx >= i + jump_height:
                continue
            for j in range(cur_idx + 1, i + jump_height + 1):
                if j >= len(nums):
                    break
                flag_reach[j] = flag_reach[i]
            cur_idx = i + jump_height

        print(flag_reach)
        return flag_reach[-1]


if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2,2,0,1,1]
    sol.canJump(nums)

