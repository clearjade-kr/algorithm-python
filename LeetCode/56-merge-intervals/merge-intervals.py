class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []
        cur_int = intervals[0]
        for interval in intervals[1:]:
            if cur_int[1] < interval[0]:
                ret.append(cur_int)
                cur_int = interval
            else:
                cur_int[1] = max(interval[1], cur_int[1])
        ret.append(cur_int)
        return ret