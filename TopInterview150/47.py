from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
            N = len(nums)
            nums.sort()
            used = [False] * N
            ret_list = []

            def backtrack(path):
                if len(path) == N:
                    ret_list.append(path.copy())
                    return

                for i in range(N):
                    if used[i]:
                        continue
                    
                    # If the current value has duplicate and prior one not used, pass
                    # Removes reversed duplicates like A_2, A_1 in the path
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    used[i] = True
                    path.append(nums[i])
                    backtrack(path)

                    path.pop()
                    used[i] = False
            
            backtrack([])
            return ret_list


if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2]
    # 1,1,2
    # 1,2,1
    # 2,1,1
    ret = sol.permuteUnique(nums=nums)
    for list in ret:
        print(list)
