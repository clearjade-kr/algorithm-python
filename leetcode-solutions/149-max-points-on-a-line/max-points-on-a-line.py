class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        combinations = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    continue
                a = points[i][1] - points[j][1]
                b = points[j][0] - points[i][0]
                c = points[i][0] * points[j][1] - points[j][0] * points[i][1]
                combinations.append((a, b, c))
        
        max_points = 0
        for i in range(len(combinations)):
            a, b, c = combinations[i]
            cur_points = 0
            for j in range(len(points)):
                if a * points[j][0] + b * points[j][1] + c == 0:
                    cur_points += 1
            max_points = max(max_points, cur_points)

        return max_points
