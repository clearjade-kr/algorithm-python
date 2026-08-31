class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        target_it = newInterval.copy()
        start_idx = -1
        end_idx = len(intervals)
        for i in range(len(intervals)):
            it = intervals[i]
            if it[1] < newInterval[0]:
                start_idx = i
                continue
            elif it[0] > newInterval[1]:
                end_idx = i
                break
            else:
                target_it[0] = min(target_it[0], it[0])
                target_it[1] = max(target_it[1], it[1])

        return intervals[:start_idx + 1] + [target_it] + intervals[end_idx:]