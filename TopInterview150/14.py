from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret_val = nums[0] + nums[1] + nums[2]
        for cur_pointer in range(len(nums) - 2):
            start, end = cur_pointer + 1, len(nums) - 1
            
            while start < end:
                cur_val = nums[cur_pointer] + nums[start] + nums[end]
                if abs(cur_val - target) < abs(ret_val - target):
                    ret_val = cur_val
                if nums[start] + nums[end] + nums[cur_pointer] < target:
                    start += 1
                elif nums[start] + nums[end] + nums[cur_pointer] > target:
                    end -= 1
                else:
                    break
        
        return ret_val
    

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,2]
    target = 3
    print(sol.threeSumClosest(nums=nums, target=target))
