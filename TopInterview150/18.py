from typing import List


"""
Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        len_nums = len(nums)
        ret_list = []
        nums.sort()
        a = 0
        while a < len_nums - 3:
            b = a + 1
            while b < len_nums - 2:
                c, d = b + 1, len_nums - 1
                while c < d:
                    if nums[a] + nums[b] + nums[c] + nums[d] < target:
                        c += 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d -= 1
                    else:
                        ret_list.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while c < len_nums - 1 and nums[c - 1] == nums[c]:
                            c += 1
                        d -= 1
                        while d > 0 and nums[d + 1] == nums[d]:
                            d -= 1
                
                b += 1
                while b < len_nums - 2 and nums[b - 1] == nums[b]:
                    b += 1
            a += 1
            while a < len_nums - 3 and nums[a - 1] == nums[a]:
                a += 1
        return ret_list
    

if __name__ == "__main__":
    sol = Solution()
    nums = [1,0,-1,0,-2,2]
    target = 0

    print(sol.fourSum(nums, target))
