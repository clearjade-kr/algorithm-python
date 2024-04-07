from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = len(nums) // 2
        dict_cnt = dict()
        for i in nums:
            if i in dict_cnt:
                dict_cnt[i] += 1
            else:
                dict_cnt[i] = 1

            if dict_cnt[i] > major:
                return i

    def majorityElementWithCounter(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max(counter.keys(), key=counter.get)


if __name__ == "__main__":
    sol = Solution()
    nums = [2,2,1,1,1,2,2]
    print(sol.majorityElement(nums))
