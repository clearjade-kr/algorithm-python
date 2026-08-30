from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
    

if __name__ == "__main__":
    sol = Solution()
    # nums = [-1,0,3,5,9,12]
    # target = 2
    # nums = [5]
    # target = 5
    nums = [0,1,2]
    target = 1

    print(sol.search(nums=nums, target=target))
