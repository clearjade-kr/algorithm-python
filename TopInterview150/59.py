from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        cur_val = 1
        while left <= right and top <= bottom:
            # Filling top row
            for i in range(left, right + 1):
                matrix[top][i] = cur_val
                cur_val += 1
            top += 1

            # Filling right row
            for i in range(top, bottom + 1):
                matrix[i][right] = cur_val
                cur_val += 1
            right -= 1

            # Filling bottom row
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = cur_val
                cur_val += 1
            bottom -= 1

            # Filling left row
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = cur_val
                cur_val += 1
            left += 1

        return matrix


if __name__ == "__main__":
    sol = Solution()
    mat = sol.generateMatrix(4)
    for row in mat:
        print(row)
