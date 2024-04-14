from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # dp1 = [1] * len(nums)
        # dp2 = [1] * len(nums)
        #
        # dp1[0] = nums[0]
        # dp2[len(nums) - 1] = nums[-1]
        # for i in range(1, len(nums)):
        #     dp1[i] = dp1[i - 1] * nums[i]
        #     dp2[len(nums) - 1 - i] = dp2[len(nums) - i] * nums[len(nums) - i - 1]
        #
        # ans = [0] * len(nums)
        # for i in range(len(nums)):
        #     if i == 0:
        #         ans[i] = dp2[1]
        #     elif i == len(nums) - 1:
        #         ans[i] = dp1[i - 1]
        #     else:
        #         ans[i] = dp1[i - 1] * dp2[i + 1]
        #
        # return ans

            s = 1
            cz = 0
            for i in nums:
                if i != 0:
                    s *= i
                else:
                    cz +=1
            ans = []
            if cz == 1:
                for i in nums:
                    if i == 0:
                        ans.append(s)
                    else:
                        ans.append(0)
            elif cz >= 2:
                ans = [0] * len(nums)
            else:
                for i in nums:
                    ans.append(s // i)
            return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [-1,1,0,-3,3]
    print(sol.productExceptSelf(nums))

