from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()
        #
        # if not nums:
        #     return 0
        #
        # max_len = 1
        # cur_len = 1
        #
        # cur_idx = 0
        # while cur_idx < len(nums):
        #     if cur_idx + 1 < len(nums) and nums[cur_idx] + 1 == nums[cur_idx + 1]:
        #         cur_len += 1
        #     elif cur_idx + 1 < len(nums) and nums[cur_idx] == nums[cur_idx + 1]:
        #         pass
        #     else:
        #         max_len = max(max_len, cur_len)
        #         cur_len = 1
        #     cur_idx += 1
        #
        # return max(max_len, cur_len)
        s = set(nums)
        q = 0
        while s:
            n = s.pop()
            l = n - 1
            while l in s:
                s.remove(l)
                l -= 1
            h = n + 1
            while h in s:
                s.remove(h)
                h += 1
            q = max(q, h-l-1)
        return q


if __name__ == "__main__":
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(sol.longestConsecutive(nums))

