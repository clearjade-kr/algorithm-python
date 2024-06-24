class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()

        def dfs(remain, path, next_idx):
            if remain == 0:
                ret.append(path)
                return

            for i in range(next_idx, len(candidates)):
                if candidates[i] > remain:
                    break

                dfs(remain - candidates[i], path + [candidates[i]], i)

        dfs(target, [], 0)
        return ret
