class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        once = twice = 0
        for num in nums:

            # add / remove num from one, and remove all from twice
            once = (once ^ num) & (~twice)
            # add / remove num from twice, and remove all from once
            twice = (twice ^ num) & (~once)
            
        return once