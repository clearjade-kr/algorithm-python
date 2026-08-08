from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_0, cnt_1, cnt_2 = nums.count(0), nums.count(1), nums.count(2)
        point_0 = 0
        point_1 = cnt_0
        point_2 = cnt_0 + cnt_1

        while point_0 < cnt_0 or point_1 < cnt_0 + cnt_1 or point_2 < len(nums):
            while point_0 < cnt_0 and nums[point_0] == 0 :
                point_0 += 1

            while point_1 < cnt_0 + cnt_1 and nums[point_1] == 1:
                point_1 += 1

            while point_2 < len(nums) and nums[point_2] == 2:
                point_2 += 1

            if point_0 < cnt_0 and nums[point_0] != 0:
                nums[point_0] = 0
            if point_1 < cnt_0 + cnt_1 and nums[point_1] != 1:
                nums[point_1] = 1
            if point_2 < len(nums) and nums[point_2] != 2:
                nums[point_2] = 2


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,2,1,1,0,0,0]
    sol.sortColors(nums=nums)
    print(nums)
