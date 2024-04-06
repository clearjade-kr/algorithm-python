from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # major = len(nums) // 2
        # dict_cnt = dict()
        # for i in nums:
        #     if i in dict_cnt:
        #         dict_cnt[i] += 1
        #     else:
        #         dict_cnt[i] = 1

        #     if dict_cnt[i] > major:
        #         return i
        counter = Counter(nums)
        return max(counter.keys(), key=counter.get)