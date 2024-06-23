# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(path, nums):
#             if len(path) == len(nums):
#                 res.append(path)
#                 return
#             for i in range(len(nums)):
#                 if nums[i] in path:
#                     continue
#                 backtrack(path + [nums[i]], nums)

#         res = []
#         backtrack([], nums)
#         return res
    

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]

        res = []

        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(n)

            res.extend(perms)
            nums.append(n)

        return res
