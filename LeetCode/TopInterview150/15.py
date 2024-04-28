from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        target = 0
        while target < len(nums) - 2:
            start, end = target + 1, len(nums) - 1
            while start < end and start < len(nums) and end >= 0:
                cur_sum = nums[start] + nums[end]
                if cur_sum + nums[target] > 0:
                    end -= 1
                elif cur_sum + nums[target] < 0:
                    start += 1
                else:
                    ret.append([nums[target], nums[start], nums[end]])
                    start += 1
                    while start < len(nums) - 1 \
                            and nums[start] == nums[start - 1]:
                        start += 1
                    end -= 1
                    while end >= 1 and nums[end] == nums[end + 1]:
                        end -= 1
            target += 1
            while target < len(nums) - 2 and nums[target] == nums[target - 1]:
                target += 1

        return ret


if __name__ == "__main__":
    sol = Solution()
    nums = [-2,0,1,1,2]
    print(sol.threeSum(nums))
