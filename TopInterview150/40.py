from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ret_list = []
        def dfs(remain, cur_list, idx):
            if remain == 0:
                ret_list.append(cur_list)
                return
            elif sum(candidates[idx:]) < remain:
                return

            for i in range(idx, len(candidates)):
                if i != idx and candidates[i - 1] == candidates[i]:
                    continue
                elif candidates[i] > remain:
                    break

                dfs(remain=remain - candidates[i], cur_list=cur_list + [candidates[i]], idx=i + 1)

        dfs(remain=target, cur_list=[], idx=0)
        return ret_list
    

if __name__ == "__main__":
    sol = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    # candidates = [1,1]
    # target = 2
    # candidates = [1,1,1,1,1,1]
    # target = 6
    # candidates = [1]
    # target = 1
    print(sol.combinationSum2(candidates=candidates, target=target))
