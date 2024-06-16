from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret = []

        start_idx = 0
        cur_idx = 0
        while cur_idx < len(nums):
            if not (cur_idx < len(nums) - 1 and nums[cur_idx + 1] == nums[cur_idx] + 1):
                if cur_idx - start_idx >= 1:
                    ret.append('%d->%d' % (nums[start_idx], nums[cur_idx]))
                else:
                    ret.append('%d' % nums[cur_idx])
                start_idx = cur_idx + 1
            cur_idx += 1

        return ret


if __name__ == "__main__":
    sol = Solution()
    # nums = [0,1,2,4,5,7]
    nums = [0, 2, 4, 8, 16]
    print(sol.summaryRanges(nums))
