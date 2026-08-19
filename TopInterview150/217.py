from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,2,3,4]
    print(sol.containsDuplicate(nums=nums))
