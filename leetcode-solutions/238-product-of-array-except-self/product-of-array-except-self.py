class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt_zero = nums.count(0)
        if cnt_zero > 1:
            return [0] * len(nums)
        elif cnt_zero == 1:
            product = 1
            for num in nums:
                if num != 0:
                    product *= num
            return [product if num == 0 else 0 for num in nums]
        else:
            product = 1
            for num in nums:
                product *= num
            return [product // num for num in nums]