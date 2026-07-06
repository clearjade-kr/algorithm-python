from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # If the last part of array is increasing, change and return
        # If not, find the first increasing part and change with previous part
        # Sort other elements below
        if len(nums) < 2:
            return

        pointer = len(nums) - 1
        while pointer > 0 and nums[pointer - 1] >= nums[pointer]:
            pointer -= 1

        if pointer == 0:
            nums.sort()
        else:
            target_pointer = pointer
            while target_pointer < len(nums) - 1 and nums[target_pointer + 1] > nums[pointer - 1]:
                target_pointer += 1
            nums[pointer - 1], nums[target_pointer] = nums[target_pointer], nums[pointer - 1]
            nums[pointer:] = sorted(nums[pointer:])
            
        return
    

if __name__ == "__main__":
    sol = Solution()
    # nums = [1,3,2] # 2,1,3
    # nums = [2,3,1] # 3,1,2
    # nums = [2,3,4,1] # 2,4,1,3
    # nums = [1,2,3] # 1,3,2
    # nums = [5,1,1] # 1,1,5
    nums = [2,3,6,5,4,1]
    sol.nextPermutation(nums=nums)
    print(nums)
