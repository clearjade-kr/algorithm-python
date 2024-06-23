from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort()
        # ret = []
        # cur_int = intervals[0]
        # for interval in intervals[1:]:
        #     if cur_int[1] < interval[0]:
        #         ret.append(cur_int)
        #         cur_int = interval
        #     else:
        #         cur_int[1] = max(interval[1], cur_int[1])
        # ret.append(cur_int)
        # return ret
        # +O(n) space, +O(n log n) time

        intervals = sorted(intervals, key=lambda it: it[0])

        stack = []
        for it in intervals:
            while stack and (stack[-1][1] >= it[0]):
                _it = stack.pop()
                it[0] = _it[0]
                it[1] = max(it[1], _it[1])
            stack.append(it)

        return stack



if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,4],[0,4]]
    print(sol.merge(intervals))
