class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sort = sorted(nums)
        start, end = 0, len(nums) - 1
        while start < end:
            if nums_sort[start] + nums_sort[end] < target:
                start += 1
            elif nums_sort[start] + nums_sort[end] > target:
                end -= 1
            else:
                if nums_sort[start] == nums_sort[end]:
                    start_idx = nums.index(nums_sort[start])
                    return [start_idx, nums.index(nums_sort[end], start_idx + 1)]
                return [nums.index(nums_sort[start]), nums.index(nums_sort[end])]
