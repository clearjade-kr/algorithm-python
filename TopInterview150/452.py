from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # points.sort()
        #
        # cnt_commons = 1
        # cur_common = points[0]
        # for point in points[1:]:
        #     if point[0] > cur_common[1]:
        #         cnt_commons += 1
        #         cur_common = point
        #     else:
        #         cur_common = [max(cur_common[0], point[0]), min(cur_common[1], point[1])]
        #
        # return cnt_commons
        result = 1
        points.sort(key=lambda elt: elt[1])
        interval = points[0]
        for point in points[1:]:
            if interval[1] < point[0]:
                result += 1
                interval = point

        return result


if __name__ == "__main__":
    sol = Solution()
    points = [[10,16],[2,8],[1,6],[7,12],[1,8]]
    print(sol.findMinArrowShots(points))
