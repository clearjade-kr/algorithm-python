from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
                cnt += 1
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[end] == "_":
                end -= 1
                continue

            if nums[start] != "_":
                start += 1
                continue

            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        # print(nums)
        return len(nums) - cnt

    # Inspiring solution
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     j = 0
    #     for i in range(len(nums)):
    #         if nums[i] != val:
    #             nums[j]=nums[i]
    #             j+=1
    #     return j


if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(sol.removeElement(nums, val))

