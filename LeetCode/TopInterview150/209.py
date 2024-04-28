from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 0
        start, end = 0, 0

        cur_sum = nums[0]
        while end < len(nums):
            if cur_sum < target:
                end += 1
                if end >= len(nums):
                    break
                cur_sum += nums[end]
            elif cur_sum >= target:
                if ans == 0:
                    ans = end - start + 1
                else:
                    ans = min(ans, end - start + 1)
                cur_sum -= nums[start]
                start += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 1, 2, 4, 3]
    target = 7

    # nums = [1,4,4]
    # target = 4
    # nums = [1,2,3,4,5]
    # target = 11
    print(sol.minSubArrayLen(target, nums))
