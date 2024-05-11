class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)

        cnt_commons = 0
        cur_common = points[0]
        for point in points[1:]:
            if point[0] > cur_common[1]:
                cnt_commons += 1
                cur_common = point
            else:
                cur_common[0] = max(cur_common[0], point[0])
                cur_common[1] = min(cur_common[1], point[1])

        return cnt_commons + 1