from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(start, end):
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        left = binary_search(0, len(nums) - 1)
        if left == -1:
            return [-1, -1]
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1

        right = left
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1

        return [left, right]


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(sol.searchRange(nums, target))
