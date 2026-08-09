from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left : all values before 'left' index will be 0
        # mid : starting point of not sorted indices
        # right : all values after 'right' index will be 2
         
        left, mid, right = 0, 0, len(nums) - 1
        while mid <= right:
            # if nums[mid] is 1 -> already sorted, moving mid one more
            if nums[mid] == 1:
                mid += 1
            # if nums[mid] is 0 -> change value with left and move both one more
            elif nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            # if nums[mid] is 2 -> change value with right and move only right one less
            # since the value changed does not guarantee sorted 
            elif nums[mid] == 2:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,2,1,1,0,0,0]
    sol.sortColors(nums=nums)
    print(nums)
