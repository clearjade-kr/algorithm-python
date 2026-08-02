from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # O(n) time complexity, O(1) space complexity required
        # Time complexity constraint would say simple for loop is all

        # Using cyclic sort mechanism
        # Check and swap the values to fit with value i in index i-1 position
        # Result we want: [1,2,3,4,...]
        # We only need to check value for 1~N (len(nums)) in list since if bigger value is in nums,
        # it definitely means there is an empty spot in 1~N
        N = len(nums)
        for i in range(N):
            while 1 <= nums[i] <= N and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(N):
            if nums[i] != i + 1:
                return i + 1

        return N + 1



if __name__ == "__main__":
    sol = Solution()
    nums = [3,4,-1,1]
    print(sol.firstMissingPositive(nums=nums))
