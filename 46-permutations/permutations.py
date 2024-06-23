class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, nums):
            if len(path) == len(nums):
                res.append(path)
                return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                backtrack(path + [nums[i]], nums)

        res = []
        backtrack([], nums)
        return res
    