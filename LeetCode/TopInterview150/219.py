from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # if len(nums) < 2:
        #     return False
        # head_idx = 0
        # tail_idx = min(len(nums), k + 1)
        # set_nums = set()
        # for i in range(tail_idx):
        #     set_nums.add(nums[i])
        # if len(set_nums) != tail_idx:
        #     return True
        # while True:
        #     if tail_idx == len(nums):
        #         return False
        #     else:
        #         set_nums.remove(nums[head_idx])
        #         head_idx += 1
        #         if nums[tail_idx] in set_nums:
        #             return True
        #         else:
        #             set_nums.add(nums[tail_idx])
        #             tail_idx += 1

        if len(set(nums)) != len(nums):
            win = []
            for i in range(len(nums)):
                if nums[i] in win:
                    return True
                else:
                    win += [nums[i]]
                    if len(win) == k+1:
                        win.remove(win[0])
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [2,2]
    k = 3
    print(sol.containsNearbyDuplicate(nums, k))
