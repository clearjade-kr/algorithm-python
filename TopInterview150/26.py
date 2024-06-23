from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[j + 1] = nums[i]
                j += 1

        # print(nums)
        return j + 1


if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(sol.removeDuplicates(nums))
