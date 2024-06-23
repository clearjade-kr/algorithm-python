from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
        print(nums)


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    sol.rotate(nums, k)
