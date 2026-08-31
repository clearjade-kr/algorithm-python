class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        if not nums:
            return 0

        max_len = 1
        cur_len = 1

        cur_idx = 0
        while cur_idx < len(nums):
            if cur_idx + 1 < len(nums) and nums[cur_idx] + 1 == nums[cur_idx + 1]:
                cur_len += 1
            elif cur_idx + 1 < len(nums) and nums[cur_idx] == nums[cur_idx + 1]:
                pass
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1
            cur_idx += 1

        return max(max_len, cur_len)