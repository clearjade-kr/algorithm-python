from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(n)]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        val = 1
        x, y = 0, 0
        dir = 0
        while val <= n ** 2:
            matrix[x][y] = val
            val += 1
            next_x, next_y = x + dx[dir], y + dy[dir]
            if not (0 <= next_x < n and 0 <= next_y < n and matrix[next_x][next_y] == -1):
                dir += 1
                dir %= 4
            x, y = x + dx[dir], y + dy[dir]

        return matrix


if __name__ == "__main__":
    sol = Solution()
    mat = sol.generateMatrix(4)
    for row in mat:
        print(row)
