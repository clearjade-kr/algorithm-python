from typing import List


def findMinArrowShots(points: List[List[int]]) -> int:
    points.sort()

    cnt_commons = 1
    cur_common = points[0]
    for point in points[1:]:
        if point[0] > cur_common[1]:
            cnt_commons += 1
            cur_common = point
        else:
            cur_common = [max(cur_common[0], point[0]), min(cur_common[1], point[1])]

    return cnt_commons

with open("user.out", "w") as f:
    for case in map(loads, stdin):
        f.write(str(findMinArrowShots(case))+"\n")
exit(0)