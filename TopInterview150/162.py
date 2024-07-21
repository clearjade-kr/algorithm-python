from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def merge(start, end):
            if start == end:
                return start

            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                return merge(start, mid)
            else:
                return merge(mid + 1, end)

        return merge(0, len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    print(sol.findPeakElement(nums))
