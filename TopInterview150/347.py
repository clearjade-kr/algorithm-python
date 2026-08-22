from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        dict_cnt = defaultdict(int)
        for num in nums:
            dict_cnt[num] += 1

        list_cnt = list(dict_cnt.items())
        list_cnt.sort(key = lambda x: x[1], reverse=True)

        return [cnt[0] for cnt in list_cnt[:k]]



if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,1]
    k = 1
    print(sol.topKFrequent(nums=nums, k=k))
